FROM node

WORKDIR /home/serverless
COPY .aws .
COPY hello.py .
COPY serverless.yml .
RUN npm install -g serverless
RUN npm install -g serverless-python-requirements

