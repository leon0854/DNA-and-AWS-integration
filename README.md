AWS Serverless Architecture based Cisco DNA Demo Platform

With this AWS serverless modularized architecture, developers only need to code for data collection. All the other function is in charge by AWS build-in function.



Every Python function is micro function on AWS Lambda, you can package every Python to ZIP file and upload it to Lambda.


Logstash conf folder contain all the input/filter/output code, Lambda will input REST API data into AWS logstash, AWS logstash output them to AWS Elasticsearch
