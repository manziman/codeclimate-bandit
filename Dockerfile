FROM python:3-alpine

RUN apk update &&\
    apk add bash

RUN pip3 install bandit

SHELL [ "/bin/bash" ]

VOLUME /code

WORKDIR /code
COPY ./run.sh /scripts/run.sh

COPY config.json /config.json

ENTRYPOINT /scripts/run.sh