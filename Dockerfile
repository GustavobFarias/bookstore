FROM python:3.11-slim

# Variáveis de ambiente para Python e Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="$POETRY_HOME/bin:$PATH"

# Instala dependências e Poetry
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        curl build-essential libpq-dev gcc && \
    curl -sSL https://install.python-poetry.org | python - && \
    /opt/poetry/bin/poetry --version && \
    apt-get purge --auto-remove -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
ENV PATH="/opt/poetry/bin:$PATH"

WORKDIR /app

# Copia arquivos para cache das dependências
COPY poetry.lock pyproject.toml /app/

# Instala dependências sem dev para produção
RUN poetry install --no-dev

# Copia o código
COPY . /app/

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
