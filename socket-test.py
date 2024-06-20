#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af_inet is ipv 4 , sock_stream is a port 

skt.connect((HOST, PORT))



# nc -nvlp 7777 , then run the 