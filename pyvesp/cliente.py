import socket
import struct
import sys
import _thread

addr = '192.168.15.13'
port = 8080

print('Iniciando o cliente ')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((addr,port))
except socket.error:
    print("erro ao conecatar")
    quit()

print("Para sair digite Ctrl+X")
msg= input()
while msg != '\x18':
    sock.send(msg.encode())
    data = sock.recv(1024)
    print("From : " + str(addr) + ' Dados '+ data.decode() + '\r\n')
    msg = input()

msg = 'fim'
sock.send(msg.encode())

sock.close()
