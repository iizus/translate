FROM python

RUN apt update
RUN apt upgrade -y

RUN pip install chalice