FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./user_service

LABEL maintainer="Arpan Patnaik"

EXPOSE 8001

CMD ["flask", "--app", "user_service", "run", "--host", "0.0.0.0", "--port", "8001"]