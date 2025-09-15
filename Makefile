# =============================================================================
# KNI Webapp - Simplified Makefile
# Single Docker Compose file with environment-based configuration
# =============================================================================

.PHONY: help dev prod clean logs shell backup load-baseline

# Project configuration
PROJECT_NAME ?= kni_webapp

help:
	@echo "🏗️  KNI Webapp - Available Commands"
	@echo ""
	@echo "📚 DEVELOPMENT:"
	@echo "  make dev          - Start development environment"
	@echo "  make dev-logs     - View development logs"
	@echo "  make dev-shell    - Access development container shell"
	@echo ""
	@echo "📚 PRODUCTION:"
	@echo "  make prod         - Start production environment"
	@echo "  make prod-logs    - View production logs"
	@echo ""
	@echo "📚 DATA MANAGEMENT:"
	@echo "  make backup       - Create database backup"
	@echo "  make load-baseline - Load baseline data"
	@echo ""
	@echo "📚 MAINTENANCE:"
	@echo "  make clean        - Clean up containers and volumes"
	@echo ""
	@echo "🌐 ACCESS:"
	@echo "  Development: http://localhost:8000"
	@echo "  Production:  http://localhost:80"

# Development commands
dev:
	@echo "🚀 Starting development environment..."
	@docker compose up -d --build
	@echo "⏳ Waiting for services to start..."
	@sleep 5
	@echo "✅ Development environment ready!"
	@echo "🌐 Application: http://localhost:8000"
	@echo "📊 Admin: http://localhost:8000/admin"

dev-logs:
	@echo "📋 Development logs:"
	@docker compose logs -f

dev-shell:
	@echo "🐚 Accessing development container shell..."
	@docker compose exec web bash

# Production commands (requires .env.dokploy file)
prod:
	@echo "🚀 Starting production environment..."
	@if [ ! -f .env.dokploy ]; then \
		echo "❌ .env.dokploy file not found!"; \
		echo "📝 Please create .env.dokploy with production settings"; \
		exit 1; \
	fi
	@docker compose --env-file .env.dokploy up -d --build
	@echo "⏳ Waiting for services to start..."
	@sleep 10
	@echo "✅ Production environment ready!"
	@echo "🌐 Application: http://localhost:80"

prod-logs:
	@echo "📋 Production logs:"
	@docker compose --env-file .env.dokploy logs -f

# Data management
backup:
	@echo "💾 Creating database backup..."
	@docker compose exec web python manage.py native_backup --include-media
	@echo "✅ Backup created successfully!"

load-baseline:
	@echo "🎯 Loading baseline data..."
	@docker compose exec web python manage.py native_restore --name baseline --include-media --flush
	@echo "✅ Baseline data loaded!"

# Maintenance
clean:
	@echo "🧹 Cleaning up containers and volumes..."
	@docker compose down --volumes --remove-orphans
	@docker compose --env-file .env.dokploy down --volumes --remove-orphans 2>/dev/null || true
	@docker system prune -f
	@echo "✅ Cleanup complete!"

# Legacy aliases for backward compatibility
up: dev
logs: dev-logs
shell: dev-shell