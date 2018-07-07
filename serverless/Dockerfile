FROM node

WORKDIR /home/serverless
COPY .aws .aws
COPY hello.py .
COPY serverless.yml .
RUN npm install -g serverless
RUN npm install serverless-python-requirements

