FROM ubuntu:latest
RUN mkdir /app
WORKDIR /app
RUN apt-get update 
RUN apt-get install python3 -y
COPY . . /app/
CMD python3 mathOps.py
