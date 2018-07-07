FROM python:2.7

WORKDIR /home
ENV AWS_DEFAULT_REGION=us-east-1

COPY serverless.yml .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
