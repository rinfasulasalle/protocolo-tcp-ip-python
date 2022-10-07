import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECTED FROM CHAT SERVER"
SERVER = "192.168.40.73" 
# Ip si es local se pone el 192 si es hamachi escribe la del hamavhi
ADDR = (SERVER, PORT)
MESSAGE = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

#send("Hello World!")
#input()
#send("Hello Everyone!")
#input()
#send("Hello Tim!")
while (MESSAGE != "exit"):
    MESSAGE = input("MESSAGE: ")
    send(MESSAGE)
# Si sale del while significa que puso exit y posteriormente 
send(DISCONNECT_MESSAGE)