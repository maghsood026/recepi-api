FROM python:3.7-alpine

MAINTAINER Maghsood026@yahoo.com

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app

WORKDIR /app

COPY ./app /app

RUN adduser -D maghsood

USER maghsood
