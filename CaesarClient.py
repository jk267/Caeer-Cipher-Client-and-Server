'''
David Kim(jk267)
CS232 Operating Systems
Professor Norman
Assignment: Caesar Client and Server Assignment
Date: April 24, 2024

'''
import socket
import sys

class CaesarClient:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            # Connect to server
            self.client_socket.connect((self.HOST, self.PORT))

            print("Welcome to the Caesar Cipher client!")
            while True:
                rotation = input("Please enter the rotation amount from 1 - 25 (or 'quit' to exit): ").strip()

                if rotation == 'quit':
                    sys.exit(0)
                elif not rotation.isdigit() or not (1 <= int(rotation) <= 25):
                    print("Exiting...Please reconnect and enter an integer between 1 and 25.")
                    sys.exit(0)

                # Send message to server
                self.client_socket.send(rotation.encode())
                # Receive and display server's response
                response = self.client_socket.recv(1024).decode()
                print("Server response:", response)  

                while True:
                    message = input("Enter a message to send (or 'quit' to exit): ").strip()

                    if message == 'quit':
                        sys.exit(0)

                    # Send message to server
                    self.client_socket.send(message.encode())

                    # Receive and display server's response
                    response = self.client_socket.recv(1024).decode()
                    
                    if not response:
                        print("Connection closed by the server.")
                        break
                    print("Server response:", response)   

        except Exception as e:
            print("Error:", e)

        finally:
            # Close socket
            self.client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 <CaesarClient.py> <hostname> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    client = CaesarClient(host, port)
    client.start()
