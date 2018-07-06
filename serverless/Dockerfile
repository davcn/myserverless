FROM node

WORKDIR /home
COPY .aws .
COPY hello.py .
COPY serverless.yml .
RUN npm install -g serverless
