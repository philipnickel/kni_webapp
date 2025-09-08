.PHONY: help setup run run-tenant admin clean migrate-public migrate-tenants seed-johann verify-tenant ensure-tenant reset-db fix-migrations

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
	@echo "Quick start (tenant): make setup && make reset-db && make run"

setup:
	@echo "Setting up JCleemann Byg..."
	pip install -r requirements.txt
	python manage.py migrate
	@echo "✅ Setup complete! Run 'make run' to start the server."

run:
	$(eval PORT := $(or $(PORT),8000))
	@echo "Checking for existing processes on port $(PORT)..."
	@lsof -ti:$(PORT) | xargs kill -9 2>/dev/null || true
	@echo "Starting server at http://localhost:$(PORT)"
	@echo "- Super admin:   http://localhost:$(PORT)/django-admin/"
	@echo "- Tenant admin:  http://johann.localhost:$(PORT)/admin/ (JCleemannByg / admin123)"
	@echo "- Tenant site:   http://johann.localhost:$(PORT)/"
	python manage.py runserver 0.0.0.0:$(PORT)

run-tenant:
	@echo "Starting tenant server at http://johann.localhost:8004"
	python manage.py runserver 0.0.0.0:8004

admin:
	python manage.py createsuperuser

migrate-public:
	python manage.py migrate --noinput

migrate-tenants:
	python manage.py migrate_schemas --tenant --noinput

seed-johann:
	python manage.py seed_tenant johann --admin-user JCleemannByg --admin-password admin123 --admin-email johann@example.com || true

verify-tenant:
	@echo "Checking tenant homepage..."
	curl -sS -I -H 'Host: johann.localhost' http://127.0.0.1:8004/ | head -n 1
	@echo "Checking projects page..."
	curl -sS -I -H 'Host: johann.localhost' http://127.0.0.1:8004/projekter/ | head -n 1
	@echo "Checking admin..."
	curl -sS -I -H 'Host: johann.localhost' http://127.0.0.1:8004/admin/ | head -n 1

ensure-tenant:
	$(eval PORT := $(or $(PORT),8000))
	python manage.py ensure_tenant_site --schema=johann --hostname=johann.localhost --port=$(PORT)

reset-db:
	@echo "⚠️  Resetting database completely..."
	@echo "Dropping database kni_webapp (if exists)..."
	@dropdb kni_webapp 2>/dev/null || true
	@echo "Creating fresh database..."
	@createdb kni_webapp
	@echo "Running fresh migrations..."
	python manage.py migrate --noinput
	@echo "Creating Johann tenant..."
	python manage.py seed_tenant johann --admin-user JCleemannByg --admin-password admin123 --admin-email johann@example.com || true
	@echo "✅ Database reset complete!"

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf media/images/* media/original_images/*
	@echo "✅ Cleanup complete"
