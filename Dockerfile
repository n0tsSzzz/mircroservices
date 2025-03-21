FROM python:3.13.2-alpine3.21

WORKDIR /code

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . .

RUN uv sync --frozen --no-cache

EXPOSE 6080

CMD [".venv/bin/uvicorn", "main:app", "--port", "6080", "--host", "0.0.0.0"]