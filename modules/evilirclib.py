import socket
import sys

class IrcLib(object):
	def __init__:
		pass

	def connect(self, server, port, nick, pass):
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.settimeout(4)
		try: 
			conn.connect((server, int(port)))
			#print '[+] connection to %s on port %s established' % (server, port)

			conn.send('NICK %s\r\n' % nick)
			conn.send('USER %s %s %s :%s\r\n' % (nick, nick, server, nick))
			return conn
		
		except socket.error, e:
			#print '[-] connection to %s on port %s failed with error: %s' % (server, port, e)

	def pingProtection(self, conn):
		data = conn.recv(1024)
		self.checkPing(conn, data)


	def checkPing(self, conn, data):
		if 'PING' in data:
			data = data.split(':')
			#print '[+] PING recieved, sending %s' % data[1]
			conn.send('PONG :%s\r\n' % data[1]) 

	def exitConnection(self, conn):
		conn.close()
		sys.exit()

	
