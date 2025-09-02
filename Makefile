PY=python
PIP=pip

.PHONY: help install install-dev migrate makemigrations run test test-cov superuser collectstatic check

help:
	@echo "Common targets:"
	@echo "  install        Install production requirements"
	@echo "  install-dev    Install dev requirements (pytest, coverage)"
	@echo "  migrate        Run database migrations"
	@echo "  makemigrations Create new migrations from models"
	@echo "  run            Run development server"
	@echo "  test           Run test suite"
	@echo "  test-cov       Run tests with coverage report"
	@echo "  superuser      Create a Django superuser"
	@echo "  collectstatic  Collect static files"
	@echo "  e2e-mcp       Run MCP smoke test (requires node/npm)"

install:
	$(PIP) install -r requirements.txt

install-dev: install
	$(PIP) install -r requirements-dev.txt

migrate:
	$(PY) manage.py migrate

makemigrations:
	$(PY) manage.py makemigrations

run:
	$(PY) manage.py runserver

test:
	pytest -q

test-cov:
	coverage run -m pytest -q && coverage report -m

superuser:
	$(PY) manage.py createsuperuser

collectstatic:
	$(PY) manage.py collectstatic --noinput

e2e-mcp:
	# Start Django dev server in background
	$(PY) manage.py runserver 0.0.0.0:8000 & echo $$! > .pid-django
	# Give it a moment to boot
	sleep 2
	# Start Playwright MCP server in background (headless)
	npx -y @executeautomation/playwright-mcp-server --headless --host 127.0.0.1 --port $${MCP_PORT:-3030} & echo $$! > .pid-mcp
	# Give MCP a moment to boot
	sleep 3
	# Run smoke script that verifies both are reachable
	MCP_PORT=$${MCP_PORT:-3030} node scripts/e2e-mcp.js; status=$$?; \
	  kill $$(cat .pid-mcp) $$(cat .pid-django) 2>/dev/null || true; \
	  rm -f .pid-mcp .pid-django; \
	  exit $$status
