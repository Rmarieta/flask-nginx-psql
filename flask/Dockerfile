FROM python:3.9.16

RUN apt-get update && \
    apt-get install -y postgresql-client-13 && \
    apt-get install -y htop

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

# create the user
RUN adduser --disabled-password --gecos '' flaskuser
USER flaskuser

# CMD python application.py
# CMD python application.py run --debug --host 0.0.0.0

# without Flask-SocketIO
# CMD gunicorn --access-logfile '-' -w 3 -t 4 -b 0.0.0.0:5000 application:application
# with Flask-SocketIO, gunicorn does not support sticky sessions, workers must be 1. gevent takes care of multi-threading, threads must be 1
CMD gunicorn --access-logfile '-' --log-level 'debug' -k gevent -w 1 -b 0.0.0.0:5000 application:application
