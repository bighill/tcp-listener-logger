#!/usr/bin/env python

import SocketServer
import logging

host    = '0.0.0.0'
port    = 8889
logfile = 'log.txt'

logging.basicConfig(level=logging.INFO,
    filename=logfile,
    format='%(asctime)s %(message)s',
    filemode='a')

class tcpServerHandler(SocketServer.BaseRequestHandler):
 
    def handle(self):
        data = self.client_address[0] + ' '
        data+= self.request.recv(1024).strip()
        logging.info( str(data) )

if __name__ == "__main__":
    try:
        server = SocketServer.TCPServer((host,port), tcpServerHandler)
        server.serve_forever(poll_interval=0.5)

    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")