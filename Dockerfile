FROM python:3.14

WORKDIR /src

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml uv sync
