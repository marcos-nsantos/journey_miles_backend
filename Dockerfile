FROM python:3.11.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .