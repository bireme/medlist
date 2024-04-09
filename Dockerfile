########### BASE STAGE ###########
FROM python:3.6.9-alpine AS base

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy base requirements
COPY ./requirements.txt /app/

# install base dependencies
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    python3-dev \
    && apk add mariadb-dev \
    && pip install --upgrade pip setuptools && pip install --no-cache-dir -r /app/requirements.txt \
    && apk del .build-deps

EXPOSE 8000

WORKDIR /app
