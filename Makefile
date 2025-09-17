# =============================================================================
# KNI Webapp - Simplified Makefile
# Single Docker Compose file with environment-based configuration
# =============================================================================

.PHONY: help dev clean logs shell backup baseline load-baseline

# Project configuration
PROJECT_NAME ?= kni_webapp

help:
	@echo "🏗️  KNI Webapp - Available Commands"
	@echo ""
	@echo "📚 DEVELOPMENT:"
	@echo "  make dev          - Start development environment (hot-reload)"
	@echo "  make dev-setup    - Full development setup (migrations, superuser, baseline)"
	@echo "  make dev-logs     - View development logs"
	@echo "  make dev-shell    - Access development container shell"
	@echo "  make dev-stop     - Stop development environment"
	@echo "  make dev-clean    - Clean development environment (removes volumes)"
	@echo ""
	@echo "📚 DATA MANAGEMENT:"
	@echo "  make backup       - Create database backup"
	@echo "  make baseline     - Create new baseline backup (replaces existing)"
	@echo "  make load-baseline - Load baseline data"
	@echo ""
	@echo "📚 MAINTENANCE:"
	@echo "  make clean        - Clean up containers, volumes, and generated files"
	@echo "  make clean-files  - Clean up only generated files (keep containers running)"
	@echo ""
	@echo "🌐 ACCESS:"
	@echo "  Development: http://localhost:8000"
	@echo "  Mailhog:     http://localhost:8025"

# Development commands
dev:
	@echo "🚀 Starting development environment..."
	@if [ ! -f .env.dev ]; then \
		echo "📝 Creating .env.dev from template..."; \
		cp env.dev.template .env.dev; \
		echo "✅ Created .env.dev - customize as needed"; \
	fi
	@docker compose --env-file .env.dev up -d --build
	@echo "⏳ Waiting for services to start..."
	@sleep 10
	@echo "✅ Development environment ready!"
	@echo "🌐 Application: http://localhost:8000"
	@echo "📊 Admin: http://localhost:8000/admin"
	@echo "📧 Mailhog: http://localhost:8025"

dev-logs:
	@echo "📋 Development logs:"
	@docker compose --env-file .env.dev logs -f

dev-shell:
	@echo "🐚 Accessing development container shell..."
	@docker compose --env-file .env.dev exec web bash

dev-setup:
	@echo "🔧 Setting up development environment..."
	@if [ ! -f .env.dev ]; then \
		echo "📝 Creating .env.dev from template..."; \
		cp env.dev.template .env.dev; \
		echo "✅ Created .env.dev - customize as needed"; \
	fi
	@echo "🚀 Starting development services..."
	@docker compose --env-file .env.dev up -d --build
	@echo "⏳ Waiting for database to be ready..."
	@sleep 15
	@echo "🗄️  Running database migrations..."
	@docker compose --env-file .env.dev exec web python manage.py migrate
	@echo "👤 Creating superuser (optional)..."
	@docker compose --env-file .env.dev exec web python manage.py createsuperuser --noinput --username admin --email admin@localhost || true
	@echo "🎯 Loading baseline data (optional)..."
	@if ls backups/baseline_*.json 1> /dev/null 2>&1; then \
		docker compose --env-file .env.dev exec web python manage.py native_restore --name baseline --include-media --flush; \
		echo "✅ Baseline data loaded!"; \
	else \
		echo "⚠️  No baseline data found - skipping"; \
	fi
	@echo "✅ Development environment setup complete!"
	@echo "🌐 Application: http://localhost:8000"
	@echo "📊 Admin: http://localhost:8000/admin (admin/admin)"
	@echo "📧 Mailhog: http://localhost:8025"

dev-stop:
	@echo "🛑 Stopping development environment..."
	@docker compose --env-file .env.dev down
	@echo "✅ Development environment stopped!"

dev-clean:
	@echo "🧹 Cleaning development environment..."
	@docker compose --env-file .env.dev down --volumes --remove-orphans
	@echo "✅ Development environment cleaned!"


# Data management
backup:
	@echo "💾 Creating database backup..."
	@docker compose --env-file .env.dev exec -T web python manage.py native_backup --include-media
	@echo "✅ Backup created successfully!"

baseline:
	@echo "🔄 Creating new baseline backup..."
	@echo "⚠️  This will replace the existing baseline backup!"
	@read -p "Continue? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@echo "🗑️  Removing old baseline backup..."
	@rm -f backups/baseline_*.json backups/baseline_*.metadata.json
	@echo "📦 Creating new baseline backup..."
	@docker compose --env-file .env.dev exec -T web python manage.py native_backup --name baseline --include-media
	@echo "✅ New baseline backup created successfully!"

load-baseline:
	@echo "🎯 Loading baseline data..."
	@docker compose --env-file .env.dev exec -T web python manage.py native_restore --name baseline --include-media --flush
	@echo "✅ Baseline data loaded!"

# Maintenance
clean:
	@echo "🧹 Cleaning up containers, volumes, and generated files..."
	@echo "🛑 Stopping all services..."
	@docker compose --env-file .env.dev down --volumes --remove-orphans 2>/dev/null || true
	@docker compose down --volumes --remove-orphans 2>/dev/null || true
	@echo "🛑 Stopping any remaining containers..."
	@docker stop $$(docker ps -q --filter "name=kni_webapp") 2>/dev/null || true
	@docker stop $$(docker ps -q --filter "name=mailhog") 2>/dev/null || true
	@echo "🗑️  Removing containers..."
	@docker container prune -f 2>/dev/null || true
	@echo "🗑️  Removing unused images..."
	@docker image prune -f 2>/dev/null || true
	@echo "🗑️  Removing unused networks..."
	@docker network prune -f 2>/dev/null || true
	@echo "🗑️  Removing generated files and directories..."
	@rm -rf staticfiles/
	@rm -rf node_modules/
	@rm -rf logs/
	@rm -rf media/
	@rm -rf data/
	@echo "⚠️  Preserving backups/ directory (contains baseline data)"
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name ".DS_Store" -delete 2>/dev/null || true
	@find . -name "Thumbs.db" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete!"

clean-files:
	@echo "🗑️  Cleaning generated files and directories..."
	@rm -rf staticfiles/
	@rm -rf node_modules/
	@rm -rf logs/
	@rm -rf media/
	@rm -rf backups/
	@rm -rf data/
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name ".DS_Store" -delete 2>/dev/null || true
	@find . -name "Thumbs.db" -delete 2>/dev/null || true
	@echo "✅ Generated files cleaned!"


# Legacy aliases for backward compatibility
up: dev
logs: dev-logs
shell: dev-shell