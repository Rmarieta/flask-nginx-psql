FROM python:3.9.16

RUN apt-get update && \
    apt-get install -y postgresql-client-13 && \
    apt-get install -y htop

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "application.py"]
