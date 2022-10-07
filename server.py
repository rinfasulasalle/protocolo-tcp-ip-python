import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
# El método bind() de la clase de socket de Python asigna una dirección IP y un número de puerto a una instancia de socket.
# El método bind() se usa cuando un socket necesita convertirse en un socket de servidor.
# Como los programas del servidor escuchan en los puertos publicados, se requiere que un puerto y la dirección IP se asignen explícitamente a un socket del servidor.
# Para los programas de cliente, no es necesario vincular el socket explícitamente a un puerto. El kernel del sistema operativo se encarga de asignar la IP de origen y un número de puerto temporal.
# El socket del cliente puede usar el método connect(), después de que se complete la creación del socket para contactar al socket del servidor.

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()