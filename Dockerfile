FROM python:3.10-slim AS builder

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY app/ app/

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --extras "cpu"

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . /app

EXPOSE 8080

ENV FLASK_APP=app/run.py \
    FLASK_RUN_HOST=0.0.0.0 \
    PYTHONPATH=/app

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app.run:app"]
