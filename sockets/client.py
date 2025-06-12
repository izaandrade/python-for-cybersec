import socket

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criação do objeto socket, padrão sempre
# IP e host qual queremos nos conectar
host = '127.0.0.1'
port = 9005

# connect
s.connect((host, port))
# conectado ao servidor

# client receiving data
while True:
    msg = s.recv(1024).decode()
    if not msg:
        break
    print(msg)
    data = input("please enter a message>> ")
    s.sendall(str.encode(data))

s.close()


#data = s.recv(1024).decode() # pois estamos recebendo o dado via rede, ele vem encoded
#print(data)
#s.close()
#print("connection closed")