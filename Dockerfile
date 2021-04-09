FROM python:slim

RUN apt update
RUN apt upgrade -y
RUN apt install -y git