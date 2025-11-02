.PHONY: setup lint type test format run build clean help

help:
	@echo "Available targets:"
	@echo "  setup   - Install dev dependencies and setup pre-commit"
	@echo "  lint    - Run ruff linter"
	@echo "  type    - Run mypy type checker"
	@echo "  test    - Run pytest tests"
	@echo "  format  - Format code with ruff"
	@echo "  run     - Example CLI invocation (prints help)"
	@echo "  build   - Build Docker image"
	@echo "  clean   - Remove cache and build artifacts"

setup:
	pip install -e ".[dev]"
	pip install -r requirements-dev.txt
	pre-commit install

lint:
	ruff check src/ tests/

type:
	mypy src/ tests/

test:
	pytest tests/ -v

format:
	ruff format src/ tests/
	ruff check --fix src/ tests/

run:
	python -m radar_data.interface.cli.runner --help

build:
	docker build -t radar-data-pipeline:latest .

clean:
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist .coverage htmlcov

