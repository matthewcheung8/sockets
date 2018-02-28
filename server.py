#!/usr/bin/python
import socket

s = socket.socket()

host = socket.gethostname()

port = 4000

s.bind((host, port))

s.listen(100)

while 1:
	c, addr = s.accept()
	print 'Got connection from ', addr
	c.send('Thanks for connecting')
	c.close()
