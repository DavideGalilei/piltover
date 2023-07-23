FROM python:3.11-bookworm

WORKDIR /app

RUN python -m venv venv

RUN venv/bin/pip install -U pip setuptools
RUN venv/bin/pip install poetry

COPY poetry.lock .
COPY pyproject.toml .
RUN venv/bin/poetry install --no-dev

COPY piltover piltover

RUN echo $(ls venv/lib/*/site-packages) | grep uvl && exit 1

ENV DISABLE_HR=1
CMD ["venv/bin/python", "-m", "piltover"]
