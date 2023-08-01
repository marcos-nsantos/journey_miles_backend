run-server:
	poetry run python -m manage runserver 0.0.0.0:8000

migrate:
	poetry run python -m manage migrate

make-migrations:
	poetry run python -m manage makemigrations
