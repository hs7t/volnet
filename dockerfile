FROM python:3.13

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install
RUN poetry run fastapi run --port 8000

EXPOSE 8000
