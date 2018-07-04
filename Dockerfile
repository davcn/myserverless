FROM python:2.7

WORKDIR /usr/src/app
EXPORT AWS_DEFAULT_REGION=us-east-1
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
