import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.2.6"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    server_msg = client.recv(2048).decode(FORMAT)
    print(server_msg)
    if server_msg == 'Alarm':
        print('Wszczynam')
    else:
        print('Nie wszczynam')

send("Hello world 1!")
send("Hello world 2!")
send("Hello world 3!")

send(DISCONNECT_MESSAGE)