# Scalable and Secure Containerized Backend

Repository to test a backend architecture that can be spin up on AWS Elastic Beanstalk or on any device with Docker installed.

The backend consists in:

- A PostgreSQL database.
- An Nginx load balancer.
- Flask containers running behind the load balancer and served over Gunicorn to enable multi-threading.
- A Redis container to coordinate websocket connections/messages while having multiple Flask processes running at the same time.

To start the development containers :

```
docker-compose up --build
```

To also create the tables the first time (or after clearing the volumes) :

```
docker-compose up -d --build ; docker-compose exec flask<ANY_NUMBER_HERE_IF_MULTIPLE_INSTANCES> bash -c "python application.py create_all"
```

To bring them down and clear the volumes :

```
docker-compose down -v
```
