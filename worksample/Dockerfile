FROM python:3.11-slim-buster
ENV LANG C.UTF-8

# Python settings
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


RUN apt-get -y update && apt-get -y autoremove

RUN mkdir /app

WORKDIR /app

RUN apt-get install -y python python-pip python-dev && apt-get clean

COPY . .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV ENV prod
