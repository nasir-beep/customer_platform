FROM python:3.11-slim

RUN apt-get update && apt-get install -y openjdk-21-jre-headless && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyspark==3.5.1

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /opt/project

CMD tail -f /dev/null
