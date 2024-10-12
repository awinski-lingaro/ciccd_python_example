FROM python:3.11-slim-buster

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry

RUN poetry install
COPY . /app
ENV PYTHONPATH=$PYTHONPATH:/app
CMD ["poetry", "run", "python", "greetings_app/entrypoints/app.py"]