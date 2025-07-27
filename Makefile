# Define a versão do Python usada no projeto (para referência)
PYTHON_VERSION ?= 3.11

# Diretórios e variáveis
LIBRARY_DIRS = mylibrary
BUILD_DIR ?= build

# Configurações de testes
PYTEST_HTML_OPTIONS = --html=$(BUILD_DIR)/report.html --self-contained-html
PYTEST_TAP_OPTIONS = --tap-combined --tap-outdir $(BUILD_DIR)
PYTEST_COVERAGE_OPTIONS = --cov=$(LIBRARY_DIRS)
PYTEST_OPTIONS ?= $(PYTEST_HTML_OPTIONS) $(PYTEST_TAP_OPTIONS) $(PYTEST_COVERAGE_OPTIONS)

# MyPy typechecking
MYPY_OPTS ?= --python-version 3.11 --show-column-numbers --pretty --html-report $(BUILD_DIR)/mypy

# Poetry
PIP ?= pip3
POETRY_OPTS ?=
POETRY ?= poetry $(POETRY_OPTS)
RUN_PYPKG_BIN = $(POETRY) run

# Cores (só funcionarão corretamente em Bash/Git Bash)
COLOR_ORANGE = \033[33m
COLOR_RESET = \033[0m

# Exibe ajuda com lista básica de comandos
.PHONY: help
help:
	@echo "Comandos disponíveis:"
	@echo "  make deps           - Instala todas as dependencias com Poetry"
	@echo "  make build          - Gera o pacote com Poetry"
	@echo "  make publish        - Publica o pacote no repositorio (Poetry)"
	@echo "  make test           - Executa os testes com Pytest"
	@echo "  make check          - Roda os linters (flake8, black, mypy)"
	@echo "  make migrate        - Roda as migracoes (dentro do container)"
	@echo "  make seed           - Roda o seed do banco de dados"
	@echo "  make format-py      - Formata o codigo com Black"
	@echo "  make version-python - Mostra a versao do Python configurada"

# Mostrar versão do Python usada
.PHONY: version-python
version-python:
	@echo $(PYTHON_VERSION)

# Testes
.PHONY: test
test:
	$(RUN_PYPKG_BIN) pytest $(PYTEST_OPTIONS) tests/*.py

# Build e publicação
.PHONY: build
build:
	$(POETRY) build

.PHONY: publish
publish:
	$(POETRY) publish $(POETRY_PUBLISH_OPTIONS_SET_BY_CI_ENV)

# Dependências
.PHONY: deps
deps:
	$(PIP) install --upgrade pip poetry
	$(POETRY) install

# Qualidade de código
.PHONY: check
check: check-py

.PHONY: check-py
check-py: check-py-flake8 check-py-black check-py-mypy

.PHONY: check-py-flake8
check-py-flake8:
	$(RUN_PYPKG_BIN) flake8 .

.PHONY: check-py-black
check-py-black:
	$(RUN_PYPKG_BIN) black --check --line-length 118 --fast .

.PHONY: check-py-mypy
check-py-mypy:
	$(RUN_PYPKG_BIN) mypy $(MYPY_OPTS) $(LIBRARY_DIRS)

.PHONY: format-py
format-py:
	$(RUN_PYPKG_BIN) black .

# Django: migração e seed
.PHONY: migrate
migrate:
	docker-compose exec web poetry run python manage.py migrate --noinput

.PHONY: seed
seed:
	poetry run python manage.py seed