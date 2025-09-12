## Docker-based development workflow
.PHONY: help up reset baseline clean check-docker

# Default docker compose project
DOCKER_PROJECT ?= kni_docker

# Check if Docker daemon is running
check-docker:
	@echo "🔍 Checking Docker daemon..."
	@if ! docker info >/dev/null 2>&1; then \
		echo "❌ Docker daemon is not running!"; \
		echo "🚀 Starting Docker Desktop..."; \
		open -a Docker; \
		echo "⏳ Waiting for Docker to start (this may take 30-60 seconds)..."; \
		echo "💡 You can also start Docker manually: open -a Docker"; \
		echo "🔄 Retrying in 15 seconds..."; \
		sleep 15; \
		if ! docker info >/dev/null 2>&1; then \
			echo "❌ Docker still not ready. Please wait a bit longer and try again."; \
			echo "💡 You can check Docker status with: docker info"; \
			exit 1; \
		fi; \
	fi
	@echo "✅ Docker daemon is running"

help:
	@echo "Docker development commands:"
	@echo "  make up            - Start application (normal mode)"
	@echo "  make reset         - Reset to baseline state"
	@echo "  make baseline      - Create baseline from current state"
	@echo "  make clean         - Clean Docker containers and volumes"

# --- Main Commands ---

up: check-docker
	@echo "🚀 Starting application (normal mode)..."
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.local up -d --build
	@echo "✅ Application started at http://localhost:8002"
	@echo "📊 Admin interface: http://localhost:8002/admin"

reset: check-docker
	@echo "🗑️  Resetting to baseline state..."
	@echo "⚠️  This will delete all data and reset to baseline!"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@echo "🛑 Stopping containers and removing volumes..."
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.local down --volumes --remove-orphans 2>/dev/null || true
	@docker volume prune -f 2>/dev/null || true
	@echo "🚀 Starting with baseline data..."
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) LOAD_BASELINE=true docker compose -f docker-compose.local.yml --env-file .env.local up -d --build
	@echo "✅ Application reset to baseline at http://localhost:8002"
	@echo "📊 Admin interface: http://localhost:8002/admin"

baseline: check-docker
	@echo "🔄 Creating baseline from current state..."
	@echo "⚠️  This will overwrite the current baseline data!"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@echo "🗑️  Removing old baseline data..."
	@rm -rf baselineData/
	@echo "📁 Recreating baseline data directory..."
	@mkdir -p baselineData/media/original_images baselineData/media/images
	@echo "🔄 Restarting container to refresh mount..."
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.local restart web
	@echo "⏳ Waiting for container to be ready..."
	@sleep 5
	@echo "📦 Creating new baseline data..."
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.local exec -T web python manage.py postgres_backup --baseline --include-media || echo "❌ Failed to create baseline"
	@echo "✅ Baseline data updated successfully!"
	@echo "📊 New baseline includes:"
	@echo "   - Database: baselineData/baseline.sql"
	@echo "   - Media: baselineData/media/"

clean:
	@echo "🧹 Cleaning Docker containers and volumes..."
	@lsof -ti:8002 | xargs kill -9 2>/dev/null || echo "No processes found on port 8002"
	@COMPOSE_PROJECT_NAME=$(DOCKER_PROJECT) docker compose -f docker-compose.local.yml --env-file .env.local down --volumes --remove-orphans 2>/dev/null || true
	@docker volume prune -f 2>/dev/null || true
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	@echo "✅ Cleanup complete"