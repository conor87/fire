import socket
import pickle
import time

HEADERSIZE = 10
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))

    while True:
        full_msg = b''
        new_msg = True
        while True:
            msg = s.recv(16)
            if new_msg:
                #print("new msg len:",msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            #print(f"full message length: {msglen}")

            full_msg += msg

            #print(len(full_msg))

            if len(full_msg)-HEADERSIZE == msglen:
                #print("full msg recvd")
                #print(full_msg[HEADERSIZE:])
                print(pickle.loads(full_msg[HEADERSIZE:]))
                new_msg = True
                full_msg = b""
    s.close()
if __name__ == "__main__":
    while True:
        main()
        time.sleep(5)