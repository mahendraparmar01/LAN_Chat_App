# 💬 LAN Chat App (Python)

A simple **Local Network Chat App** built using Python's `socket`, `threading`, and `Tkinter`. It allows multiple users to chat in real-time over a LAN.


## 📌 Features

- 🧠 Multi-client support via threading
- 💬 Real-time chat with GUI (Tkinter)
- 🧾 Chat logs saved daily
- ⚙️ Commands: `/exit`, `/mute`
- 📡 Server-client model over LAN


## 📁 Project Structure
```bash
LAN_Chat_App/
├── server.py # Server script
├── client.py # Client GUI app
└── chat_logs/ # Chat logs auto-generated daily
```


## 🛠️ Tools Used

- Python 3
- `socket` — networking
- `threading` — multi-client handling
- `tkinter` — GUI for client
- `datetime`, `os` — file management


## 🚀 How to Run

### 1. Clone the Repository

### 2. Start the Server
```bash
python server.py
```
> You'll see: Server listening on `127.0.0.1:12345`

### 3. Run Clients (in two terminals)

```bash
python client.py
```
> A chat window will appear. Enter a nickname and start chatting!

## ✨ Chat Commands
| Command | Description            |
| ------- | ---------------------- |
| `/exit` | Leave the chat         |
| `/mute` | Local mute placeholder |
