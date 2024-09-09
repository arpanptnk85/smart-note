FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./user_service

RUN mkdir -p /app/logs

LABEL maintainer="Arpan Patnaik"

EXPOSE 8001

ENV MONGO_URI=mongodb://mongo-service:27017/smart-note

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]