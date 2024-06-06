'''
David Kim(jk267)
CS232 Operating Systems
Professor Norman
Assignment: Caesar Client and Server Assignment
Date: April 24, 2024

'''

import sys
import threading
from datetime import datetime
import socket

#client and server logic mostly borrowed from https://realpython.com/python-sockets/
class CaesarServer:
    def __init__(self, port):
        self.PORT = port
        self.HOST = ""
        self.client_count = 0

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            print(f"Server is listening on port {self.PORT}")
            while True:
                conn, addr = s.accept()
                thread = threading.Thread(target=self.handle_connections, args=(conn, addr))
                thread.start()

    def handle_connections(self, conn, addr):
        with threading.Lock():
            self.client_count += 1
            print(f"[{datetime.now()}] Connection from {addr[0]} at {addr[1]}. | Total client(s): {self.client_count}")

        received_rotation_n = False
        
        while True:
            data = conn.recv(1024)
            if not data:
                self.client_count -= 1
                print(f"[{datetime.now()}] Client {addr[0]} at {addr[1]} has left. | Total client(s): {self.client_count}")
                break
            
            if not received_rotation_n:
                rotation = int(data.decode().strip())
                if 1 <= rotation <= 25:
                    data = f"rotation amount is {rotation}"
                    conn.sendall(data.encode())  # Echo back the received data to the client
                    received_rotation_n = True
                else:
                    conn.sendall(b"please enter an integer between 1-25. Connection closed. Please retry.")
                    conn.close()
                    break
            else:
                rotated_data = self.rotate_text(data.decode(), rotation)
                conn.sendall(rotated_data.encode())  # Send rotated data back to the client

    def rotate_text(self, text, rotation_n):
        # refered from https://stackoverflow.com/questions/45950617/function-that-receives-and-rotates-a-text
        rotated_text = ""
        for char in text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                rotated_text += chr((ord(char) - shift + rotation_n) % 26 + shift)
            else:
                rotated_text += char
        return rotated_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <CaesarServer.py> <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    server = CaesarServer(port)
    server.start()