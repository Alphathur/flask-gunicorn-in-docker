FROM python:3.6.5

MAINTAINER alphathur

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app
RUN pip3 install -r /app/requirements.txt
ADD . /app

EXPOSE 8000
CMD ["gunicorn", "--config", "gunicorn_config.py", "app.main:app"]
