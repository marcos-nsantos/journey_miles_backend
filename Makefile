run-server:
	poetry run python -m manage runserver

migrate:
	poetry run python -m manage migrate

make-migrations:
	poetry run python -m manage makemigrations
