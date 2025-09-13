"""
Health check endpoints for monitoring application status
"""
import logging
import time
from django.core.cache import cache, caches
from django.db import connection, connections
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
from django.conf import settings
import redis
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


def check_database():
    """Check database connectivity and response time"""
    try:
        start_time = time.time()
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        return {
            "status": "healthy",
            "response_time_ms": round(response_time, 2),
            "connection_vendor": connection.vendor,
            "connection_name": connection.settings_dict.get('NAME', 'unknown')
        }
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }


def check_redis():
    """Check Redis connectivity and response time"""
    try:
        redis_url = getattr(settings, 'REDIS_URL', None)
        if not redis_url:
            return {"status": "not_configured"}

        start_time = time.time()

        # Test default cache
        cache_key = "health_check_test"
        cache.set(cache_key, "test_value", 10)
        retrieved_value = cache.get(cache_key)
        cache.delete(cache_key)

        if retrieved_value != "test_value":
            raise Exception("Cache set/get test failed")

        response_time = (time.time() - start_time) * 1000

        # Get Redis info
        redis_client = redis.from_url(redis_url)
        redis_info = redis_client.info()

        return {
            "status": "healthy",
            "response_time_ms": round(response_time, 2),
            "redis_version": redis_info.get('redis_version', 'unknown'),
            "used_memory_human": redis_info.get('used_memory_human', 'unknown'),
            "connected_clients": redis_info.get('connected_clients', 'unknown')
        }
    except Exception as e:
        logger.error(f"Redis health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e)
        }


def check_cache_backends():
    """Check all configured cache backends"""
    cache_status = {}

    for cache_name in settings.CACHES.keys():
        try:
            start_time = time.time()
            cache_backend = caches[cache_name]
            test_key = f"health_check_{cache_name}"

            cache_backend.set(test_key, "test", 10)
            retrieved = cache_backend.get(test_key)
            cache_backend.delete(test_key)

            response_time = (time.time() - start_time) * 1000

            cache_status[cache_name] = {
                "status": "healthy" if retrieved == "test" else "unhealthy",
                "response_time_ms": round(response_time, 2),
                "backend": settings.CACHES[cache_name].get('BACKEND', 'unknown')
            }
        except Exception as e:
            logger.error(f"Cache {cache_name} health check failed: {str(e)}")
            cache_status[cache_name] = {
                "status": "unhealthy",
                "error": str(e)
            }

    return cache_status


@never_cache
@require_http_methods(["GET"])
def health_check(request):
    """Basic health check endpoint"""
    try:
        # Quick database check
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        return JsonResponse({
            "status": "healthy",
            "timestamp": time.time(),
            "version": getattr(settings, 'VERSION', '1.0.0'),
            "debug": settings.DEBUG
        })
    except Exception as e:
        logger.error(f"Basic health check failed: {str(e)}")
        return JsonResponse({
            "status": "unhealthy",
            "error": str(e),
            "timestamp": time.time()
        }, status=503)


@never_cache
@require_http_methods(["GET"])
def health_check_detailed(request):
    """Detailed health check with all services"""
    start_time = time.time()

    health_data = {
        "status": "healthy",
        "timestamp": time.time(),
        "version": getattr(settings, 'VERSION', '1.0.0'),
        "debug": settings.DEBUG,
        "checks": {
            "database": check_database(),
            "redis": check_redis(),
            "cache_backends": check_cache_backends(),
        }
    }

    # Determine overall status
    failed_checks = []
    for check_name, check_data in health_data["checks"].items():
        if isinstance(check_data, dict) and check_data.get("status") == "unhealthy":
            failed_checks.append(check_name)
        elif isinstance(check_data, dict):
            # Check cache backends specifically
            for cache_name, cache_data in check_data.items():
                if isinstance(cache_data, dict) and cache_data.get("status") == "unhealthy":
                    failed_checks.append(f"{check_name}.{cache_name}")

    if failed_checks:
        health_data["status"] = "unhealthy"
        health_data["failed_checks"] = failed_checks

    # Add response time
    health_data["response_time_ms"] = round((time.time() - start_time) * 1000, 2)

    status_code = 200 if health_data["status"] == "healthy" else 503

    return JsonResponse(health_data, status=status_code)


@never_cache
@require_http_methods(["GET"])
def readiness_check(request):
    """Kubernetes readiness probe endpoint"""
    try:
        # Check critical services only
        db_status = check_database()
        redis_status = check_redis()

        if db_status.get("status") == "unhealthy":
            return JsonResponse({
                "status": "not_ready",
                "reason": "database_unavailable",
                "timestamp": time.time()
            }, status=503)

        if redis_status.get("status") == "unhealthy":
            return JsonResponse({
                "status": "not_ready",
                "reason": "redis_unavailable",
                "timestamp": time.time()
            }, status=503)

        return JsonResponse({
            "status": "ready",
            "timestamp": time.time()
        })
    except Exception as e:
        logger.error(f"Readiness check failed: {str(e)}")
        return JsonResponse({
            "status": "not_ready",
            "error": str(e),
            "timestamp": time.time()
        }, status=503)


@never_cache
@require_http_methods(["GET"])
def liveness_check(request):
    """Kubernetes liveness probe endpoint - minimal check"""
    return JsonResponse({
        "status": "alive",
        "timestamp": time.time()
    })