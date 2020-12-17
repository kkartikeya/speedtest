FROM python:3

LABEL maintainer="kk@kkartikeya.com"

RUN mkdir /app
ADD speedtest.py /app/

RUN pip install speedtest-cli prometheus_client

EXPOSE 9102/tcp

CMD [ "python", "/app/speedtest.py" ]
