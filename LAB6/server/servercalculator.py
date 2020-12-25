import socket
import sys
import time
import errno
from multiprocessing import Process
import math

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode('\nWelcome to the Server\n'))

    while True:
        data = s_sock.recv(2048).decode("utf-8").split(".")

        if data[0] == "L":
            calculation = math.log(float(data[1]))
            print(" calculation for Log is : " + (str(calculation)))
        elif data[0] == "S":
            calculation = math.sqrt(float(data[1]))
            print(" calculation for Square Root is : " + (str(calculation)))
        elif data[0] == "E":
            calculation = math.exp(float(data[1]))
            print(" calculation for Exponent is : " + (str(calculation)))
        else:
            print(" - The client has request to quit. ")
            sys.exit()

        s_sock.sendall(str.encode(str(calculation)))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("Server is listening...")
    s.listen(3)

    try:
	while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()
            except socket.error:
                print(" - Socket error received")
    except Exception as e:
        print(' - Exception occurred!')
        print(e)

