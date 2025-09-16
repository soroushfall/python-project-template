install:
	python -m pip install --upgrade pip setuptools wheel
	python -m pip install -e ".[dev]"

lint:
	ruff check .
	black --check .
	ruff format --check .

typecheck:
	mypy src

test:
	pytest

format:
	black .
	ruff check --fix .

audit:
	pip-audit || true

run:
	python -m sample.cli hello Soroush
