FROM python:3.6
WORKDIR /app
COPY . /app
RUN python3 -m unittest