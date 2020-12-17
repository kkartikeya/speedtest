#!/usr/bin/python

import os
import time
from prometheus_client import start_http_server, Gauge

def speedTest():
    a = os.popen("python /Users/kk/Library/Python/3.7/bin/speedtest-cli --simple").read()
    lines = a.split('\n')
    ts = time.time()

    #if speedtest could not connect set the speeds to 0
    if "Cannot" in a:
        p = 100
        d = 0
        u = 0
    #extract the values for ping down and up values
    else:
        p = lines[0][6:11]
        d = lines[1][10:14]
        u = lines[2][8:12]

    return p, d, u

def main():
    start_http_server(9102)
    g_ping = Gauge('internet_speed_ping', 'Ping(ms)')
    g_download = Gauge('internet_speed_download', 'Download speed(Mbps)')
    g_upload = Gauge('internet_speed_upload', 'Upload speed(Mbps)')
    while True:
        ping, download, upload = speedTest()
        g_ping.set(ping)
        g_download.set(download)
        g_upload.set(upload)

        time.sleep(300)

if __name__ == '__main__':
    main()
