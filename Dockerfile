FROM python:3.8

ENV AWS_DEFAULT_REGION ap-northeast-1

RUN apt update
RUN apt upgrade -y

RUN apt install -y httpie

RUN pip install chalice