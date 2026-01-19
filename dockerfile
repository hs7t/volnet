FROM python:3.13

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install --no-root

COPY . .

RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "fastapi", "run", "--port", "8000", "--host", "0.0.0.0"]
