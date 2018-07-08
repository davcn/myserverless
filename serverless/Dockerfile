FROM node:latest

WORKDIR /home/serverless
COPY .aws .aws
COPY hello.py .
COPY serverless.yml .
COPY requirements.txt .

# install yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash

# install python tooling
RUN apt-get update -y && apt-get install -y python-dev python-pip && pip install --upgrade pip

# install other utils
RUN apt-get update -y && apt-get install -y screen

RUN npm install -g serverless
RUN npm install serverless-python-requirements 


# install aws-cli
RUN pip install awscli
RUN pip install -r requirements.txt

