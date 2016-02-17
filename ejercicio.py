#!/usr/bin/python
# -*- coding: utf-8 -*-
#Lucia Villa Martinez

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)
sumandouno = True
while True:
	print 'Waiting for connections'
	(recvSocket, address) = mySocket.accept()
	print 'HTTP request received:'
	peticion = recvSocket.recv(1301)
	try:
		entero = peticion.split()[1][1:]
	except KeyError:
		continue 
	if sumandouno == True:
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
		recvSocket.send("<html><body><h1> Bienvenido al sumador, introduzca su segundo sumando ")
		recvSocket.send("</h1></body></html>")
		recvSocket.send("\r\n")
		sumandouno = False
		primersumando = int(entero)
	else:
		resultado = primersumando + int(entero)
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
		recvSocket.send("<html><body><h1> El resultado de su suma es: ")
		recvSocket.send(str(resultado))
		recvSocket.send("</h1></body></html>")
		recvSocket.send("\r\n")
		sumandouno = True
	recvSocket.close()
