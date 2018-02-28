#!/usr/bin/python
import socket
from thread import start_new_thread
import threading

print_lock = threading.Lock()

def threaded(c):
	while 1:
		data = c.recv(1024)
		if not data:
			print('Bye')
			print_lock.release()
			break
		c.send(data[::-1])
	c.close()

def main():
	s = socket.socket()
	host = socket.gethostname()
	port = 4000
	s.bind((host, port))
	s.listen(100)
	while 1:
		c, addr = s.accept()
		print_lock.acquire()
		print('Connected to:', addr[0], ':', addr[1])
		start_new_thread(threaded, (c,))
	s.close()

if __name__ == '__main__':
	main()
