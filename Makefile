install:
	poetry install

lint:
	poetry run flake8 gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

test-coverage:
	poetry run pytest --cov --cov-report xml:coverage.xml
