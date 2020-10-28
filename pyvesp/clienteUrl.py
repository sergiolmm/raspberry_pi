import socket
import struct
import sys
import _thread

addr = '185.201.11.211'
port = 80

print('Iniciando o cliente ')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((addr,port))
except socket.error:
    print("erro ao conecatar")
    quit()



msg =  (
        'GET https://slmm.com.br/ws/exe1/index2.php?id=3&tipo=json HTTP/1.1\r\n'
        '\r\n'
        )

sock.send(msg.encode())
data = sock.recv(2048)
print(data.decode())
print('\r\n')
sock.close()
