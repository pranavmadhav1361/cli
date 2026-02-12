import socket
import threading


class Client:
    def __init__(self):
        self.server_ip = input("Enter server IP: ")
        self.server_port = 12345

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.server_ip, self.server_port))
        print("Connected to server")

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                if not msg:
                    print("Server disconnected")
                    break
                print(msg)
            except:
                break

    def chat(self):
        self.connect()

        receiver = threading.Thread(target=self.receive_messages)
        receiver.daemon = True
        receiver.start()

        while True:
            msg = input()
            msg = f"\nclient: {msg}\n"
            self.client_socket.send(msg.encode())


if __name__ == "__main__":
    client = Client()
    client.chat()
