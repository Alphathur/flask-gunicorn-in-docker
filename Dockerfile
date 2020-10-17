FROM python:3.6.5

MAINTAINER alphathur

RUN mkdir -p /app
RUN mkdir -p /logs
COPY * ./app

WORKDIR /app
RUN pip install -r /card_api/app/requirements.txt
EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:9000","--timeout", "1200", "--keep-alive", "60", "--reload", "service.main:app"]
