.PHONY: help setup run admin clean

help:
	@echo "JCleemann Byg - Available commands:"
	@echo ""
	@echo "  make setup     - Install dependencies and setup database"
	@echo "  make run       - Start development server (default port 8000)"
	@echo "  make run PORT=3000 - Start server on custom port"
	@echo "  make admin     - Create admin user"
	@echo "  make clean     - Clean up generated files"
	@echo ""
	@echo "Quick start: make setup && make run"

setup:
	@echo "Setting up JCleemann Byg..."
	pip install -r requirements.txt
	python manage.py migrate
	@echo "✅ Setup complete! Run 'make run' to start the server."

run:
	$(eval PORT := $(or $(PORT),8000))
	@echo "Starting server at http://localhost:$(PORT)"
	@echo "Admin panel: http://localhost:$(PORT)/admin (testadmin/test123)"
	python manage.py runserver $(PORT)

admin:
	python manage.py createsuperuser

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf media/images/* media/original_images/*
	@echo "✅ Cleanup complete"