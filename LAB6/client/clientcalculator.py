import sys
import socket

ClientSocket = socket.socket()
host = '192.168.0.117'
port = 8888

print('Waiting for connection')
try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print(str(e))

Response = ClientSocket.recv(1024)
print(Response)

while True:

	print("\n\n -  The following mathematical functions can be choosen : \n\n L - Logarithmic \n S - Square Root \n E - Exponent \n\n")
	print(" - Enter Q if you want to quit \n")

	Input = input(' - Enter mathematical function or Q : ')

	if Input == 'Q':
		print(" - Requesting to Quit from the server ")
		ClientSocket.send(str.encode(Input))
		sys.exit()

	value = input(' - Enter a value : ')
	Input = Input + "." + value

	ClientSocket.send(str.encode(Input))

	Response = ClientSocket.recv(1024)
	print(" - The calculation is : " + Response.decode('utf-8'))

ClientSocket.close()
