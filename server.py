import socket
import threading


class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 12345

        # Create TCP socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind and listen
        self.server.bind((self.host, self.port))
        self.server.listen(5)

        print("Server started. Waiting for client...")

        # Accept client
        self.clientsocket, self.addr = self.server.accept()
        print("Connected from:", self.addr)

    def receive_messages(self):
        while True:
            try:
                msg = self.clientsocket.recv(1024).decode()
                if not msg:
                    print("Client disconnected")
                    break
                print(msg)
            except Exception as e:
                print("Receive error:", e)
                break

    def chat(self):
        receiver = threading.Thread(target=self.receive_messages)
        receiver.daemon = True
        receiver.start()

        while True:
            msg = input()
            msg = f"\nserver: {msg}\n"
            self.clientsocket.send(msg.encode())


if __name__ == "__main__":
    server = Server()
    server.chat()
