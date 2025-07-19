import socket
import threading
import os
from datetime import datetime

HOST = '127.0.0.1'
PORT = 12345
clients = []
nicknames = []

# Create logs folder
if not os.path.exists("chat_logs"):
    os.mkdir("chat_logs")
log_file = f"chat_logs/chat_{datetime.now().strftime('%Y-%m-%d')}.txt"

def broadcast(message, _client=None):
    with open(log_file, 'a') as f:
        f.write(message + "\n")
    for client in clients:
        if client != _client:
            client.send(message.encode())

def handle(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg.strip() == "/exit":
                index = clients.index(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"[INFO] {nickname} has left the chat.")
                clients.remove(client)
                nicknames.remove(nickname)
                break
            else:
                index = clients.index(client)
                broadcast(f"{nicknames[index]}: {msg}", client)
        except:
            break

def receive():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"Connected with {addr}")
        client.send("NICK".encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)
        broadcast(f"[INFO] {nickname} joined the chat.")
        client.send("Connected to the server.\nType '/exit' to leave.".encode())
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
