import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nickname = ""

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "NICK":
                client.send(nickname.encode())
            else:
                chat_box.config(state='normal')
                chat_box.insert('end', message + '\n')
                chat_box.yview('end')
                chat_box.config(state='disabled')
        except:
            break

def write():
    message = msg_entry.get()
    if message.strip() == "":
        return
    if message.strip() == "/exit":
        client.send("/exit".encode())
        window.quit()
        return
    elif message.strip() == "/mute":
        messagebox.showinfo("Mute", "Mute is a local command. Muting not implemented.")
        msg_entry.delete(0, 'end')
        return
    client.send(message.encode())
    msg_entry.delete(0, 'end')

# GUI Setup
window = tk.Tk()
window.title("LAN Chat Client")

chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled')
chat_box.pack(padx=10, pady=10, fill='both', expand=True)

msg_entry = tk.Entry(window)
msg_entry.pack(padx=10, pady=(0, 10), fill='x')
msg_entry.bind('<Return>', lambda event: write())

send_button = tk.Button(window, text="Send", command=write)
send_button.pack(padx=10, pady=(0, 10))

nickname = simpledialog.askstring("Nickname", "Choose your nickname:", parent=window)
if not nickname:
    window.quit()

recv_thread = threading.Thread(target=receive)
recv_thread.start()

window.protocol("WM_DELETE_WINDOW", lambda: client.send("/exit".encode()) or window.destroy())
window.mainloop()
