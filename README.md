# Scalable and Secure Containerized Backend

Repository to test a backend architecture that can be spin up on AWS Elastic Beanstalk or on any device with Docker installed.

## Content

The backend consists in:

- A PostgreSQL database.
- An Nginx load balancer.
- Flask containers running behind the load balancer and served over Gunicorn to enable multi-threading.
- A Redis container to coordinate websocket connections/messages while having multiple Flask processes running at the same time.

## Build the Containers

To use this code, first rename `.env.example` to `.env` and set your own values.

To build the containers, there are multiple options. The `run.sh` shell script provides commands that can be run to spin up all the containers with some additional options.

The `run.sh` script can be executed with:

```
bash ./run.sh [-e <environment>] [-v] [-d]
```

The 3 flags are optional and do the following:

- `-e`/`--env` is either of `debug`, `dev` or `prod` (default) and determines which `docker-compose.<env>.yml` to run. The `debug` environment has logging and development servers, as opposed to the `prod` environment.
- `-v`: if present, will first remove the volumes associated with the containers. For example to remove the content of the database while testing. If not present, will simply bring down all the containers before starting new ones.
- `-d`: if present, will run in detach mode. If not, will finish the execution with `docker-compose logs -f` which displays container logs in real-time in the current shell.

Example (running the backend in `debug` mode and not in detach mode):

```
bash ./run.sh -e debug -v
```

Then the API can be accessed from `http://localhost:1015/` since the Nginx load balancer is listening on that port.
