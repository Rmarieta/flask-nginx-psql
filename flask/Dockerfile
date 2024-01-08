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
# CMD gunicorn --access-logfile '-' --workers 1 --threads 4 --bind flask:5000 application:application
# with Flask-SocketIO
CMD gunicorn --access-logfile '-' --worker-class eventlet --workers 1 --threads 4 --bind flask:5000 application:application
