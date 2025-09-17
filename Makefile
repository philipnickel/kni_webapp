# Simplified Makefile for local/docker workflows

.PHONY: dev baseline clean

ENV_FILE ?= .env.dev
COMPOSE := docker compose --env-file $(ENV_FILE)
WEB := $(COMPOSE) exec web

# Start local development stack, run migrations, and sync baseline content
dev:
	@echo "🚀 Starting Docker services using $(ENV_FILE)..."
	@$(COMPOSE) up -d --build
	@echo "🔄 Applying database migrations..."
	@$(WEB) python manage.py migrate
	@echo "👤 Ensuring local superuser philip exists..."
	@$(WEB) python manage.py shell -c "\
from django.contrib.auth import get_user_model;\
User = get_user_model();\
user, created = User.objects.update_or_create(\
    username='philip',\
    defaults={'email': 'philip@example.com', 'is_staff': True, 'is_superuser': True}\
);\
user.set_password('admin123');\
user.save();\
print('Created' if created else 'Updated', 'superuser philip')\
"
	@echo "🌐 Syncing baseline content (optional)..."
	@$(WEB) bash -c 'if [ -n "$$BASELINE_SOURCE" ] && [ -n "$$BASELINE_ROOT_PAGE_ID" ]; then \
		python manage.py baseline_pull --flush; \
	else \
		echo "⚠️  Baseline sync skipped – set BASELINE_SOURCE and BASELINE_ROOT_PAGE_ID"; \
	fi'
	@echo "✅ Development environment ready."

# Force a fresh baseline sync (useful for staging/production via ENV_FILE=.env.prod)
baseline:
	@echo "🟢 Ensuring Docker services are running..."
	@$(COMPOSE) up -d
	@echo "🔄 Replacing local content from configured baseline source..."
	@$(WEB) bash -c 'if [ -n "$$BASELINE_SOURCE" ] && [ -n "$$BASELINE_ROOT_PAGE_ID" ]; then \
		python manage.py baseline_pull --flush; \
	else \
		echo "⚠️  Baseline sync skipped – set BASELINE_SOURCE and BASELINE_ROOT_PAGE_ID"; \
	fi'
	@echo "✅ Baseline sync complete."

# Tear down Docker resources and remove build artefacts
clean:
	@echo "🧹 Stopping Docker services..."
	@$(COMPOSE) down --volumes --remove-orphans 2>/dev/null || true
	@echo "🗑️  Removing generated files..."
	@rm -rf staticfiles/ media/ logs/ frontend_static/ node_modules/
	@find . -name '__pycache__' -type d -prune -exec rm -rf {} +
	@find . -name '*.pyc' -delete
	@echo "✅ Cleanup complete."
