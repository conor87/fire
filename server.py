import socket
import threading
from main import alarm

HEADER = 64
PORT = 5050
SERVER = "192.168.1.6"
# SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client2(conn, addr):
    print(f"[NEW CONNCETION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode('utf8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf8')
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Alarm2".encode('utf-8'))

    conn.close()


def handle_client(conn, addr):
    print(f"[NEW CONNCETION] {addr} connected")
    # pobierz aktualny stan alarmu
    czy_alarm = alarm()

    connected = True
    if connected:
        conn.send(czy_alarm.encode('utf-8'))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")
    

print("[STARTING] server is starting...")
start()

