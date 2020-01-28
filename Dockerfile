FROM python:3.8.1

RUN apt update && \
    apt install -y netcat-openbsd


ENV INSTALL_PATH /mhero-flask
RUN mkdir -p $INSTALL_PATH


WORKDIR $INSTALL_PATH


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /mhero-flask/docker-entrypoint.sh

CMD ["/bin/bash", "/mhero-flask/docker-entrypoint.sh"]
