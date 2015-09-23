import os
import SocketServer

port 	= 8888
host 	= '0.0.0.0'
logfile = 'log.txt'

print 'listening on port %s and logging to %s' % (port, logfile)

class tcpServer(SocketServer.ThreadingTCPServer) :
	allow_reuse_address = True

class tcpServerHandler(SocketServer.BaseRequestHandler) :
	def handle(self):
		try:
			fname = open( logfile, 'wb' )
			while True:
				inputString = self.request.recv(1024).strip()
				if inputString:
					fname.write( inputString )
				else:
					fname.close()
					break
		except Exception, e:
			print "Exception wile receiving message: ", e

server = tcpServer( (host, port), tcpServerHandler )
server.serve_forever()