#!/usr/bin/python

import socket
import os.path
import argparse

parser = argparse.ArgumentParser(description='Port Scanner')
parser.add_argument('-S', '--server', help='Enter a Hostname or IP address.')
args = parser.parse_args()

def scan_port(port, server):
    data = ('Successful Conncection on port {} at host {}'.format(port, server))
    s = socket.socket()
    socket.setdefaulttimeout(2)
    try:
        s.connect((server, port))
        print(data)
        if not os.path.exists('DataLog.txt'):
            with open('DataLog.txt', 'w+') as newfile:
                newfile.write(data)
                newfile.close()

        elif os.path.exists('DataLog.txt'):
            with open('Datalog.txt') as currentfile:
                currentfile.write(data)
                currentfile.close()
    except:
        print('Unable to connect on port {}'.format(port))

if __name__ == '__main__':
    for i in range(1024):
        scan_port(i, args.server)
