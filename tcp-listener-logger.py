import os
import SocketServer
port = 8888
host = '0.0.0.0'

class MyTCPServer(SocketServer.ThreadingTCPServer):
	allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		try:
			fname = open('./data.xml', 'wb')
			while True:
				strng = self.request.recv(1024).strip()
				if strng:
					fname.write(strng)
				else:
					fname.close()
					break
		except Exception, e:
			print "Exception wile receiving message: ", e

server = MyTCPServer((host, port), MyTCPServerHandler)
server.serve_forever()