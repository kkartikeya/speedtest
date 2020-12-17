FROM ubuntu:focal

LABEL maintainer = "kk@kkartikeya.com"

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git-core python3 python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install speedtest-cli prometheus_client

EXPOSE 9102 / tcp

RUN mkdir / app
ADD speedtest.py / app /

CMD ["python3", "/app/speedtest.py"]
