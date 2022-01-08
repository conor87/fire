from time import sleep
import socket
from monit import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
import sys

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = "192.168.1.6"
ADDR = (SERVER, PORT)

'''
def send2(msg):
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
'''


def send():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    server_msg = client.recv(2048).decode(FORMAT)
    print(server_msg)
    if server_msg == 'alarm':
        print('Wszczynam')
        #-----pojawienie się okan
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec_())
        #------
    else:
        print('Nie wszczynam')
    client.close()


while True:
    send()
    sleep(2)
