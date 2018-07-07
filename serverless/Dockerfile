FROM node

RUN apt-get install python-pip 

WORKDIR /home/serverless
COPY .aws .aws
COPY hello.py .
COPY serverless.yml .
COPY requirements.txt .

RUN npm install -g serverless
RUN npm install serverless-python-requirements
RUN pip install --no-cache-dir -r requirements.txt

