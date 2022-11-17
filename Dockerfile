FROM python:3.10.0

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean
RUN apt-get update -o Acquire::CompressionTypes::Order::=gz

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential
RUN apt-get install -y cron


RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
