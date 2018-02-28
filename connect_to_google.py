#!/usr/bin/python

import socket
import sys

try:
	s = socket.socket()
	print "Socket successfully created"
except socket.error as err:
	print "socket creation failed with err %s" %(err)

port = 80

try:
	host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
	print "error resolving host"
	sys.exit()

s.connect((host_ip, port))

print "successfully connected to google on port == %s " %(host_ip)
