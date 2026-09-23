FROM python:3.13-slim

WORKDIR /app

COPY api-tests/ .

RUN pip install pytest requests allure-pytest

CMD ["pytest"]