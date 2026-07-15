FROM bitnami/spark:3.5

USER root

RUN install_packages python3 python3-pip

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /opt/project

USER 1001