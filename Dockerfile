FROM python:3.8

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD apt update && apt install postgresql

COPY . /app
WORKDIR /app/

EXPOSE 5000

CMD gunicorn  main:app