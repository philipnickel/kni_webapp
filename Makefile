## Docker-based development workflow
.PHONY: help docker-up docker-down docker-logs docker-shell create-baseline clean

# Default docker compose project
DOCKER_PROJECT ?= kni_docker

help:
	@echo "Docker development commands:"
	@echo "  make docker-up     - Start application with baseline data"
	@echo "  make docker-down   - Stop application"
	@echo "  make docker-logs   - View application logs"
	@echo "  make docker-shell  - Shell into web container"
	@echo "  make create-baseline - Update baseline data from current state"
	@echo "  make clean         - Remove caches and temp files"

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	@echo "✅ Cleanup complete"

create-baseline:
	@echo "Creating baseline from current Docker container..."
	COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.docker exec web python manage.py postgres_backup --baseline --include-media || echo "⚠️  Container not running. Start with 'make docker-up' first."

# --- Docker commands ---

docker-up:
	COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.docker up -d --build
	@echo "✅ Application started at http://localhost:8001"

docker-down:
	COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.docker down || true

docker-logs:
	COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.docker logs -f web

docker-shell:
	COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.docker exec web sh || true
