import socket
import time
from threading import Thread

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 12345

count = 0

print "Waiting for partner..."

while count == 0:
	try:
		s.connect(("localhost", port))
		count+=1
	except:
		pass

print "Partner connected"

def listen():
	global s
	while True:
		data = s.recv(1024)
		print "Localhost > "+str(data)


def Send():
	global s

	while True:
		msg = raw_input(">")
		s.send(msg)

if __name__ == "__main__":
	Thread(target=listen).start()
	Thread(target=Send).start()