#!/usr/bin/python

import sys
import time
import json
import subprocess
from prometheus_client import start_http_server, Gauge

cmd = ['/usr/local/bin/speedtest', '--json']
def speedTest():

    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    p.wait()

    stdout, stderr = p.communicate()
    result = stdout

    if result != None:
        resultjson = json.loads(stdout)
        return resultjson["ping"], resultjson["download"], resultjson["upload"]
    else:
        return 0,0,0

def main():
    start_http_server(9102)
    g_latency = Gauge('internet_speed_latency', 'Ping(ms)')
    g_download = Gauge('internet_speed_download', 'Download speed(Mbps)')
    g_upload = Gauge('internet_speed_upload', 'Upload speed(Mbps)')
    while True:
        latency, download, upload = speedTest()
        g_latency.set(latency)
        g_download.set(download)
        g_upload.set(upload)

        time.sleep(300)

if __name__ == '__main__':
    main()
