import socket
import sys

ClientSocket = socket.socket()
host = '192.168.56.102'
port = 8558

print ('Waiting for connection...')
try:
	ClientSocket.connect((host, port))
except socket.error as e:
	print (str(e))

while True:
	print ('\nWelcome to the Python Calculator!')
	print ('1. Logarithmic')
	print ('2. Square Root')
	print ('3. Exponential')
	print ('4. Power')
	print ('0. Exit')

	Input = input('Input the number to choose the type of calculation: ')
	ClientSocket.send(Input.encode())

	if Input == '1':
		print ('\nLog Function')
		no1 = input('\nEnter a Number: ')
		no2 = input('\nEnther a Base: ')
		ClientSocket.sendall(str.encode('\n'.join([str(no1), str(no2)])))
		total = ClientSocket.recv(1024)
		print ('Answer for log' + no1 + ' base' + no2 + ' is: ' + str(total.decode()))

	elif Input == '2':
		root = True
		while root:
			print ('\nSquare Root Function')
			no1 = input('\nEnter a Number: ')
			if float(no1) < 0:
				print ('\nNegative Number Cannot Be Square Root')
			else:
				root = False
				ClientSocket.send(no1.encode())
				total = ClientSocket.recv(1024)
			print ('Answer for square root ' + no1 + ' is: ' + str(total.decode()))

	elif Input == '3':
		print ('\nExponential Function')
		no1 = input('\nEnter a Number: ')
		ClientSocket.send(no1.encode())
		total = ClientSocket.recv(1024)
		print ('Answer for exponential ' + no1 + ' is: ' + str(total.decode()))

	elif Input == '4':
		print ('\nPower of Function')
		no1 = input('\nEnter a Number: ')
		no3 = input('\nEnter the Power: ')
		ClientSocket.sendall(str.encode('\n'.join([str(no1), str(no3)])))
		total = ClientSocket.recv(1024)
		print ('Answer for ' + no1 + ' to the power of ' + no3 + ' is: ' + str(total.decode()))

	elif Input == '0':
		ClientSocket.close()
		sys.exit()

	else:
		print ('\nInvalid input\nPlease try again!')

	input ('\nPress Enter to Continue...')
