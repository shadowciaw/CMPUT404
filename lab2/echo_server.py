#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process
import sys

# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def recv_data(clientsocket):
    # recieve data, wait a bit, then send it back
    full_data = clientsocket.recv(BUFFER_SIZE)
    print("received data: {full_data}".format(full_data=full_data))
    time.sleep(0.5)
    clientsocket.sendall(full_data)
    clientsocket.close()
    sys.exit(0)  # kill the child process


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind socket to address
        s.bind((HOST, PORT))
        # set to listening mode
        s.listen(2)

        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            p = Process(target=recv_data, args=conn)
            p.start()


if __name__ == "__main__":
    main()
