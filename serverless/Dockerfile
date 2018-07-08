FROM node

RUN apt-get update && apt-get install -y python-pip

WORKDIR /home/serverless
COPY .aws .aws
COPY hello.py .
COPY serverless.yml .
COPY requirements.txt .

RUN npm install -g serverless &&
	npm install serverless-python-requirements &&
	pip install --upgrade setuptool &&
	pip install -r requirements.txt

