import socket

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criação do objeto socket, padrão sempre

# host and port
host = '127.0.0.1'
port = 9005

# bind
# set up to take connections
s.bind((host, port)) # IP da máquina + porta um pc aleatório, sempre um número maior que 1024
print(f"server started on {host}:{port}")

# listen
s.listen()
print("waiting for a connection...")

# aguardando conexão

# accept

client, addr = s.accept() # não será executado até alguém tentar conectar - alguém = client
# temos alguém conectado

print(f"connection received from {addr}")
while True:
    data = input("please enter a message>> ")
    client.sendall(str.encode(data))
    msg = client.recv(1024).decode()
    if not msg:
        break
    print(msg)

client.close()

# if the server is sending
#data = "this is a test. thanks for connecting"
#client.sendall(str.encode(data))
#client.close()
#print(f"connection with {addr} has been closed")