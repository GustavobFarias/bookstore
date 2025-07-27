FROM python:3.11-slim

ENV POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH" \
    POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && apt-get install -y curl build-essential libpq-dev gcc \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-dev

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]