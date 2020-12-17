FROM ubuntu:focal

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git-core python3 python3-pip

RUN pip3  install --upgrade pip 
RUN pip3 install speedtest-cli  prometheus_client  twitter
