FROM python:3.6
MAINTAINER Dat Truong <mr.anhdat@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN mkdir /config
RUN mkdir /src

COPY ./requirements.txt /config/
RUN pip install -r /config/requirements.txt