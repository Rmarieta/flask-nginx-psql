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

CMD gunicorn --access-logfile '-' --workers 2 --threads 3 --bind flask:5000 application:application
