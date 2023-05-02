.PHONY: all install requirements format test

all: format test

install:
	python -m pip install -r requirements-dev.txt

requirements:
	python -m piptools compile --no-emit-index-url --resolver=backtracking -q -o requirements.txt pyproject.toml
	python -m piptools compile --extra dev --no-emit-index-url --resolver=backtracking -q -o requirements-dev.txt pyproject.toml

format:
	python -m black .

test:
	python -m pytest
