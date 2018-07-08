FROM amaysim/serverless:1.27.1

WORKDIR /home/serverless
COPY .aws .aws
COPY hello.py .
COPY serverless.yml .
COPY requirements.txt .

#RUN npm install -g serverless
#RUN npm install serverless-python-requirements 
RUN pip install -r requirements.txt

