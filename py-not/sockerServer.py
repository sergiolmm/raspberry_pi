import struct
import socket
import sys
import _thread



def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255',1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def sendHTTP(msg):
    resp = (
        'HTTP/1.1 200 OK\r\n'
        'Content-type: text/html\r\n'
        'Connection: close\r\n'
        '\r\n'
        '\r\n' + msg + '\r\n\r\n'
    )
    return resp


# definir funcao para tratar cada conexao ao servidor
def on_new_client(clientsocket, addr):
    #
    #
    print("funcao de tratameto")
    while True:
        msgBruta = clientsocket.recv(1024)
        msgBase = msgBruta.decode()
        print('From -> '+ str(addr) + '\r\nMensagem recebida : \r\n'+ msgBase)        
        if msgBase:
            break
    
    if msgBase.__contains__(' / '):
        msg = sendHTTP(
            '<html><head><title>Alo turma</title></head>'
            '<body><h1>Deu certo pessoal</h1><p>'
            'criamos um monstro....</body></html>'
        )    
        clientsocket.send(msg.encode())
    else:
        resp = (
        'HTTP/1.1 400 OK\r\n'
        'Content-type: text/html\r\n'
        'Connection: close\r\n'
        '\r\n'
        '\r\n' 
        '<html><head></head><body>Nao tem arquivo...</body></html>')
        clientsocket.send(resp.encode())
    clientsocket.close()





https = get_ip()
port  = 8080
print("Iniciando Servidor no ip "+ https + " na porta : " + str(port))

def socketServer(a,b):
    global https
    global port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    try:
        sock.bind((https, port))
    except socket.error:
        sock.bind(('',port))

    sock.listen(1)

    while True:
        c, addr = sock.accept()
        _thread.start_new_thread(on_new_client,(c,addr))

    sock.close()


print("principal....executando")
_thread.start_new_thread(socketServer,(1,1))
while True:
    f = 10

