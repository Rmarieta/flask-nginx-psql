# Scalable and Secure Containerized Backend

Repository to test a backend architecture that can be spin up on AWS Elastic Beanstalk or on any device with Docker installed.

The backend consists in:

- A PostgreSQL database.
- An Nginx load balancer.
- Flask containers running behind the load balancer and served over Gunicorn to enable multi-threading.
- A Redis container to coordinate websocket connections/messages while having multiple Flask processes running at the same time.

To use this code, first rename `.env.example` to `.env` and set your own values.

To start the containers, a `run.sh` shell script is provided. It can be run with the following options: 

- `-e`/`--env` : which has to be provided and is either of `debug`, `dev` and `prod`. This will determine which `docker-compose` will be used.
- `-v`/`--volumes` : if provided, first clears the volumes associated with the containers to start fresh.
- `-d`/`--detach` : if provided, runs `docker-compose` in detached mode.

For example, to run the `debug` version and start with empty volumes:

```
bash ./run.sh -e debug -v
```

Then, to bring the containers down and clear the volumes, do:

```
docker-compose -f docker-compose.debug.yml down -v
```
