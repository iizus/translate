# FROM python:slim
FROM python

ENV DISPLAY host.docker.internal:0

RUN apt update
RUN apt upgrade -y
# RUN apt install -y git

RUN pip install PySimpleGUI