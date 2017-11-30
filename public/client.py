import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
nick = raw_input("Please, enter you nickname: ")
print "You may now start messaging"
while 1:
	text = raw_input("Your message here: ")
	text = nick + "> " + text
	sock.sendto(text,('255.255.255.255',12345))
