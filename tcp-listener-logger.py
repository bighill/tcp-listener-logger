#!/usr/bin/env python

'''
tcp-listener-logger
'''

import SocketServer
import logging

#
# configuration variables
#
host        = '0.0.0.0'
port        = 8888
logFile     = 'log.txt'
logFormat   = '%(asctime)s %(message)s'

#
# console message
#
print ""
print "tcp-listener-logger is listening on %s:%s" % ( host, port )
print "Results will be logged to %s" % logFile

#
# all of the business logic happens below
#

logging.basicConfig(level=logging.INFO, filename=logFile, format=logFormat, filemode='a')

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