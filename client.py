from server import receive
import socket, threading, tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '192.168.0.110'
PORT = 12000

class Client:
    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))

        msg = tkinter.Tk()
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=msg)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=gui_loop)
        receive_thread = threading.Thread(target=receive)

        gui_thread.start()
        receive_thread.start()