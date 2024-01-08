# Scalable and Secure Containerized Backend

Repository to test a backend architecture that can be spin up on AWS Elastic Beanstalk or on any device with Docker installed.

The backend consists in:

- A PostgreSQL database.
- An Nginx load balancer.
- Flask containers running behind the load balancer and served over Gunicorn.
