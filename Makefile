run-server:
	poetry run python -m core.manage runserver

migrate:
	poetry run python -m core.manage migrate

make-migrations:
	poetry run python -m core.manage makemigrations

check:
	poetry run python -m core.manage check
