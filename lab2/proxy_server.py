#!/usr/bin/env python3
import socket
from multiprocessing import Process
import sys

# define address & buffer size
GOOGLE_HOST = "www.google.com"
GOOGLE_PORT = 80
CLIENT_HOST = "localhost"
CLIENT_PORT = 5050
BUFFER_SIZE = 4096


def create_tcp_socket():
    """
        create a tcp socket
    """
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(
            f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    return s


def get_remote_ip(host):
    """
        get host information
    """
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip


def send_data_google(serversocket, payload):
    """
        send data to www.google.com; payload in byte string
    """
    print("Sending payload")
    try:
        serversocket.sendall(payload)
    except socket.error:
        print('Send failed')
        sys.exit()
    print("Payload sent successfully")


def forward(serversocket: socket, clientsocket: socket):
    # accept data from connected client
    full_data = clientsocket.recv(BUFFER_SIZE)
    print(f"received data: {full_data}")

    send_data_google(serversocket, full_data)
    full_data = b""
    while True:
        data = serversocket.recv(BUFFER_SIZE)
        if not data:
            break
        full_data += data
        print(f"recv'd {data}")

    clientsocket.sendall(full_data)
    print("sent back data")
    clientsocket.close()
    sys.exit(0)  # kill the child process


def main():
    """
    1. connect to google
    2. fork on new incoming connection
    3. forward received request to www.google.com
    4. send response from www.google.com to client
    """
    try:
        # make the socket, get the ip, and connect to google
        google = create_tcp_socket()
        google_ip = get_remote_ip(GOOGLE_HOST)
        google.connect((google_ip, GOOGLE_PORT))
        print(f'Socket Connected to {GOOGLE_HOST} on ip {google_ip}')

        # make the listening socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((CLIENT_HOST, CLIENT_PORT))
        s.listen(2)

        # continuously listen for connections
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")

            p = Process(target=forward, args=(google, conn))
            p.start()
    except Exception as e:
        print("EXCEPTION: ", e)
    finally:
        # close connection
        s.close()


if __name__ == "__main__":
    main()
