Magic Cards
========================

This project contains a MySQL server with data on magic cards, a web service
for serving cards and receiving move commands and finally a RabbitMQ consumer
to move cards.

Usage:
------

This application can be run using Docker composer and using the API endpoint at
port 5000.

Starting the services:
```
$ docker-composer up
```

Moving all cards from SQL to text file
```
$ curl -d '' localhost:5000/moveall
```

Moving a given expansion ID to text file
```
$ curl localhost:5000/movecards/1
```

Get information on a single card by GathererId
```
$ curl localhost:5000/card/1
```


Implementation:
---------------

The web application issues messages to RabbitMQ whenever a move is required. It
also provides information on a single card present in the especified text file.

The consumer service listens to RabbitMQ `moving_cards` queue, saving the card
information to the provided text file.


Contents:
---------

+ src/app.py
    Web service implementation.

+ src/consumer.py
    RabbitMQ consumer for moving cards.

+ src/dao.py
    Utility functions for SQL and text files.

+ src/requirements.txt
    List of python libraries needed.

+ src/run.sh
    Simple script for running both the web and consumer.

+ src/settings.py
    Configuration variables.

+ src/tests.py
    Unit testing.

+ docker-compose.yml
    Docker composer configuration for the 3 required containers.

+ Dockerfile
    Docker configuration for web/consumer container.

Requirements:
-------------

+ Python, tested on v3.5.2.
+ Flask, for web service.
+ pika, for RabbitMQ.
+ mysqlclient, for MySQL.

Make sure to check the `requirements.txt` file for further information.
