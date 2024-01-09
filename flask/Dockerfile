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
# CMD gunicorn --access-logfile '-' --workers 3 --threads 4 --bind 0.0.0.0:5000 application:application
# with Flask-SocketIO, gunicorn does not support sticky sessions, workers must be 1. eventlet takes care of multi-threading, threads must be 1
CMD gunicorn --access-logfile '-' --log-level 'debug' --worker-class eventlet --workers 1 --bind 0.0.0.0:5000 application:application
