# Nameko Mailgun service
## What it is?
Simple microservice sending an email with confirmation to the client everytime the payment is trigered.
## How to run it?
Project has few dependencies so firstly install:
```
pip install nameko
pip install faker
pip install pytest
```
Yo will also need [rabbitmq](https://www.rabbitmq.com/download.html) and [mailgun](https://www.mailgun.com/)

Run your rabbitmq in terminal and type
```
nameko run payments
```
## To do!
Service testing!!!

Api key should be environmental variable
