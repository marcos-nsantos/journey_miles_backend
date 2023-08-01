FROM python:3.11.4-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --no-cache --update --virtual .build-deps \
    build-base \
    python3-dev \
    make \
    && rm -rf /var/cache/apk/*

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]