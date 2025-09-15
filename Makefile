# =============================================================================
# KNI Webapp - Unified Makefile
# =============================================================================
.PHONY: help dev-up prod-up dokploy-up load-baseline backup baseline clean check-docker

# Project configuration
DOCKER_PROJECT ?= kni_webapp

# =============================================================================
# Help
# =============================================================================

help:
	@echo "🏗️  KNI Webapp - Available Commands"
	@echo ""
	@echo "📚 DEVELOPMENT:"
	@echo "  make dev-up        - Start local development environment"
	@echo ""
	@echo "📚 PRODUCTION:"
	@echo "  make prod-up       - Start production environment"
	@echo "  make dokploy-up    - Start Dokploy-optimized production environment"
	@echo ""
	@echo "📚 DATA MANAGEMENT:"
	@echo "  make load-baseline - Load baseline backup (Django native restore)"
	@echo "  make backup        - Create database backup (Django native JSON)"
	@echo "  make baseline      - Create named 'baseline' backup"
	@echo ""
	@echo "📚 MAINTENANCE:"
	@echo "  make clean         - Clean up everything (preserves backups)"
	@echo ""
	@echo "🌐 ACCESS:"
	@echo "  http://localhost:8080      - Application"
	@echo "  http://localhost:8080/admin - Admin (admin / admin123)"

check-docker:
	@if ! docker info >/dev/null 2>&1; then \
		echo "❌ Docker daemon is not running!"; \
		echo "🚀 Starting OrbStack..."; \
		orbctl start; \
		echo "⏳ Waiting for OrbStack to start..."; \
		sleep 10; \
		if ! docker info >/dev/null 2>&1; then \
			echo "❌ OrbStack still not ready. Please start OrbStack manually or run 'orbctl start'."; \
			exit 1; \
		fi; \
	fi

# =============================================================================
# Main Commands
# =============================================================================

dev-up: check-docker
	@echo "🚀 Starting local development environment..."
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_dev docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file .env.development up -d --build
	@echo "⏳ Waiting for services..."
	@sleep 8
	@echo "✅ Development environment started!"
	@echo "🌐 Application: http://localhost:8080"
	@echo "📊 Admin: http://localhost:8080/admin"

prod-up: check-docker
	@echo "🚀 Starting production environment..."
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_prod docker compose -f docker-compose.yml --env-file .env.production up -d --build
	@echo "⏳ Waiting for services..."
	@sleep 10
	@echo "✅ Production environment started!"
	@echo "🌐 Application: http://localhost:8000"
	@echo "📊 Admin: http://localhost:8000/admin"

dokploy-up: check-docker
	@echo "🚀 Starting Dokploy production environment..."
	@COMPOSE_PROJECT_NAME=kni-webapp docker compose -f docker-compose.yml --env-file .env.dokploy up -d --build
	@echo "⏳ Waiting for services..."
	@sleep 10
	@echo "✅ Dokploy environment started!"
	@echo "🌐 Application will be available at your configured domain"
	@echo "📊 Admin: https://your-domain.com/admin"

load-baseline:
	@echo "🎯 Loading baseline backup (Django native)..."
	@if docker ps --format "table {{.Names}}" | grep -q "$(DOCKER_PROJECT)_dev-web"; then \
		echo "📋 Loading in local development environment..."; \
		echo "⚠️  Development mode - using flush for clean restore"; \
		COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_dev docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file .env.development exec -T web python manage.py native_restore --name baseline --include-media --flush; \
	elif docker ps --format "table {{.Names}}" | grep -q "$(DOCKER_PROJECT)_prod-web"; then \
		echo "📋 Loading in production environment..."; \
		echo "⚠️  Production mode - will prompt before overwriting data"; \
		COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_prod docker compose -f docker-compose.yml --env-file .env.production exec -T web python manage.py native_restore --name baseline --include-media; \
	elif docker ps --format "table {{.Names}}" | grep -q "kni-webapp-web"; then \
		echo "📋 Loading in Dokploy environment..."; \
		echo "⚠️  Dokploy mode - will prompt before overwriting data"; \
		COMPOSE_PROJECT_NAME=kni-webapp docker compose -f docker-compose.yml --env-file .env.dokploy exec -T web python manage.py native_restore --name baseline --include-media; \
	else \
		echo "❌ No Docker containers running. Please start the environment first:"; \
		echo "  Development: make dev-up"; \
		echo "  Production: make prod-up"; \
		echo "  Dokploy: make dokploy-up"; \
		exit 1; \
	fi
	@echo "✅ Baseline loaded successfully (Django native)!"

backup:
	@echo "💾 Creating database backup (Django native)..."
	@if docker ps --format "table {{.Names}}" | grep -q "$(DOCKER_PROJECT)_dev-web"; then \
		echo "📋 Creating backup in local development environment..."; \
		COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_dev docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file .env.development exec -T web python manage.py native_backup --include-media; \
	elif docker ps --format "table {{.Names}}" | grep -q "$(DOCKER_PROJECT)_prod-web"; then \
		echo "📋 Creating backup in production environment..."; \
		COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_prod docker compose -f docker-compose.yml --env-file .env.production exec -T web python manage.py native_backup --include-media; \
	elif docker ps --format "table {{.Names}}" | grep -q "kni-webapp-web"; then \
		echo "📋 Creating backup in Dokploy environment..."; \
		COMPOSE_PROJECT_NAME=kni-webapp docker compose -f docker-compose.yml --env-file .env.dokploy exec -T web python manage.py native_backup --include-media; \
	else \
		echo "❌ No Docker containers running. Please start the environment first:"; \
		echo "  Development: make dev-up"; \
		echo "  Production: make prod-up"; \
		echo "  Dokploy: make dokploy-up"; \
		exit 1; \
	fi
	@echo "✅ Database backup created successfully (Django native)!"

baseline:
	@echo "🔄 Creating new baseline backup (Django native)..."
	@echo "⚠️  This will create a new baseline backup!"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@echo "📦 Capturing current database state as baseline backup..."
	@if docker ps --format "table {{.Names}}" | grep -q "$(DOCKER_PROJECT)_dev-web"; then \
		echo "📋 Creating baseline backup from local development..."; \
		COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_dev docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file .env.development exec -T web python manage.py native_backup --name baseline --include-media; \
	elif docker ps --format "table {{.Names}}" | grep -q "$(DOCKER_PROJECT)_prod-web"; then \
		echo "📋 Creating baseline backup from production..."; \
		COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_prod docker compose -f docker-compose.yml --env-file .env.production exec -T web python manage.py native_backup --name baseline --include-media; \
	elif docker ps --format "table {{.Names}}" | grep -q "kni-webapp-web"; then \
		echo "📋 Creating baseline backup from Dokploy..."; \
		COMPOSE_PROJECT_NAME=kni-webapp docker compose -f docker-compose.yml --env-file .env.dokploy exec -T web python manage.py native_backup --name baseline --include-media; \
	else \
		echo "❌ No Docker containers running. Please start the environment first:"; \
		echo "  Development: make dev-up"; \
		echo "  Production: make prod-up"; \
		echo "  Dokploy: make dokploy-up"; \
		exit 1; \
	fi
	@echo "✅ New baseline backup created (Django native)!"
	@echo "📊 Django native JSON backup - database-agnostic and robust!"

clean: check-docker
	@echo "🧹 Cleaning up everything..."
	@echo "⚠️  This will stop all containers and remove volumes"
	@echo "✅ Backup data will be preserved"
	@read -p "Continue? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@echo "🛑 Stopping containers..."
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_dev docker compose -f docker-compose.yml -f docker-compose.dev.yml --env-file .env.development down --volumes --remove-orphans 2>/dev/null || true
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT)_prod docker compose -f docker-compose.yml --env-file .env.production down --volumes --remove-orphans 2>/dev/null || true
	@COMPOSE_PROJECT_NAME=kni-webapp docker compose -f docker-compose.yml --env-file .env.dokploy down --volumes --remove-orphans 2>/dev/null || true
	@echo "🧹 Cleaning up Docker resources..."
	@docker system prune -f 2>/dev/null || true
	@echo "🗑️  Cleaning Python cache..."
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cleanup complete!"
	@echo "📁 Backup data preserved in backups/"