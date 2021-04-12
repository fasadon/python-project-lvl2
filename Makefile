install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest gendiff tests/test.py

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/test.py

selfcheck:
	poetry check

check: selfcheck test lint


.PHONY: install test lint selfcheck build
