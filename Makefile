.PHONY: help setup run run-tenant admin clean migrate-public migrate-tenants seed-johann verify-tenant ensure-tenant reset-db docker-build docker-up docker-down docker-logs docker-shell docker-test

# Use virtualenv python/pip explicitly to avoid PATH issues
PY := ./venv/bin/python
PIP := ./venv/bin/pip

help:
	@echo "JCleemann Byg - Available commands:"
	@echo ""
	@echo "  make setup     - Install dependencies and setup database"
	@echo "  make reset-db  - Reset database and run all migrations"
	@echo "  make run       - Migrate tenants, ensure tenant site, start server (default 8000)"
	@echo "  make run PORT=3000 - Start server on custom port and ensure tenant site"
	@echo "  make run-tenant - Start tenant server on port 8004 (legacy option)"
	@echo "  make admin     - Create admin user"
	@echo "  make migrate-public  - Run public schema migrations"
	@echo "  make migrate-tenants - Run tenant schema migrations only"
	@echo "  make seed-johann    - Seed/ensure Johann tenant content"
	@echo "  make verify-tenant  - Curl-check tenant site & admin"
	@echo "  make clean     - Clean up generated files"
	@echo ""
	@echo "Docker commands:"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-up     - Start Docker containers"
	@echo "  make docker-down   - Stop Docker containers"
	@echo "  make docker-logs   - View Docker logs"
	@echo "  make docker-shell  - Shell into running web container"
	@echo "  make docker-test   - Build and test Docker setup locally"
	@echo ""
	@echo "Quick start (local): make setup && make reset-db && make run"
	@echo "Quick start (docker): make docker-test"

setup:
	@echo "Setting up JCleemann Byg..."
	$(PIP) install -r requirements.txt
	$(PY) manage.py migrate
	@echo "✅ Setup complete! Run 'make run' to start the server."

run:
	$(eval PORT := $(or $(PORT),8000))
	@echo "Checking for existing processes on port $(PORT)..."
	@lsof -ti:$(PORT) | xargs kill -9 2>/dev/null || true
	@echo "Starting server at http://localhost:$(PORT)"
	@echo "- Super admin:   http://localhost:$(PORT)/django-admin/"
	@echo "- Tenant admin:  http://johann.localhost:$(PORT)/admin/ (JCleemannByg / admin123)"
	@echo "- Tenant site:   http://johann.localhost:$(PORT)/"
	$(PY) manage.py runserver 0.0.0.0:$(PORT)

run-tenant:
	@echo "Starting tenant server at http://johann.localhost:8004"
	$(PY) manage.py runserver 0.0.0.0:8004

admin:
	$(PY) manage.py createsuperuser

migrate-public:
	$(PY) manage.py migrate --noinput

migrate-tenants:
	$(PY) manage.py migrate_schemas --tenant --noinput

seed-johann:
	$(PY) manage.py seed_tenant johann --admin-user JCleemannByg --admin-password admin123 --admin-email johann@example.com || true

verify-tenant:
	@echo "Checking tenant homepage..."
	curl -sS -I -H 'Host: johann.localhost' http://127.0.0.1:8004/ | head -n 1
	@echo "Checking projects page..."
	curl -sS -I -H 'Host: johann.localhost' http://127.0.0.1:8004/projekter/ | head -n 1
	@echo "Checking admin..."
	curl -sS -I -H 'Host: johann.localhost' http://127.0.0.1:8004/admin/ | head -n 1

ensure-tenant:
	$(eval PORT := $(or $(PORT),8000))
	$(PY) manage.py ensure_tenant_site --schema=johann --hostname=johann.localhost --port=$(PORT)

reset-db:
	@echo "⚠️  Resetting database completely..."
	@echo "Dropping database kni_webapp (if exists)..."
	@dropdb kni_webapp 2>/dev/null || true
	@echo "Creating fresh database..."
	@createdb kni_webapp
	@echo "Running fresh migrations..."
	$(PY) manage.py migrate --noinput
	@echo "Creating Johann tenant..."
	$(PY) manage.py seed_tenant johann --admin-user JCleemannByg --admin-password admin123 --admin-email johann@example.com || true
	@echo "✅ Database reset complete!"

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf media/images/* media/original_images/*
	@echo "✅ Cleanup complete"

# Docker commands
docker-build:
	@echo "Building Docker image..."
	docker build -t kni-webapp --target production .
	@echo "✅ Docker image built successfully!"

docker-up:
	@echo "Starting Docker containers..."
	docker-compose up -d
	@echo "✅ Containers started!"
	@echo "- Web: http://localhost:8000"
	@echo "- Health: http://localhost:8000/health/"
	@echo "- Admin: http://localhost:8000/admin/"

docker-down:
	@echo "Stopping Docker containers..."
	docker-compose down
	@echo "✅ Containers stopped!"

docker-logs:
	@echo "Showing Docker logs..."
	docker-compose logs -f

docker-shell:
	@echo "Opening shell in web container..."
	docker-compose exec web /bin/bash

docker-test:
	@echo "Testing Docker setup locally..."
	docker-compose up -d --build
	@echo "⏳ Waiting for containers to be ready..."
	@sleep 10
	@echo "Testing health endpoint..."
	@curl -f http://localhost:8000/health/ || (echo "❌ Health check failed" && exit 1)
	@echo "✅ Docker setup is working!"
	@echo "Visit: http://localhost:8000"
