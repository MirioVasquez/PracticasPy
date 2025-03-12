FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django_app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy dependency definitions
COPY django_app/Pipfile django_app/Pipfile.lock ./
RUN pip install --upgrade pip && pip install pipenv && pipenv install --system

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY django_app/stackrecord .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]