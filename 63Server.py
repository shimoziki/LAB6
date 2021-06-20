
import socket
import sys
import math
import errno

from multiprocessing import Process

def ProcessStart(s_sock):
	while True:
		input = s_sock.recv(1024).decode()

		if input == '1':
			no1, no2 = [float(i) for i in s_sock.recv(2048).decode('utf-8').split('\n')]
			calculate = math.log(float(no1),float(no2))

		elif input == '2':
			no1 = s_sock.recv(1024).decode()
			calculate = math.sqrt(float(no1))

		elif input == '3':
			no1 = s_sock.recv(1024).decode()
			calculate = math.exp(float(no1))

		elif input == '4':
			no1, no3 = [float(i) for i in s_sock.recv(2048).decode('utf-8').split('\n')]
			calculate = math.pow(no1,no3)

		elif input == '0':
			s_sock.close()
			break
		s_sock.sendall(str(calculate).encode())

if __name__ == '__main__':

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host =''
	port = 8558
	print ("listening...")

	try:
		s.bind((host, port))
	except socket.error as e:
		print (str(e))
		sys.exit(0)

	s.listen(5)
	while True:
		try:
			s_sock, s_addr = s.accept()
			print ('Successfully Connected!')
			p = Process(target=ProcessStart, args=(s_sock,))
			p.start()
		except socket.error:
			print ('got a socket error')
	s.close()
