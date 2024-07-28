import tkinter as ttk
from tkinter.ttk import *
from Register import *
from Login import *
from Chat import *

window = ttk.Tk()
h, w = 500, 500


window.title("Messenger")
window.geometry(f"{h}x{w}")
window.resizable(False, False)

login = Login(window)
register = Register(window)
chat = Chat(window)

login.add_switch('register', register.frame)
register.add_switch('login', login.frame)
login.add_switch('chat', chat.frame)
register.add_switch('chat', chat.frame)

login.frame.pack()
style = Style()
style.theme_use('clam')
style.configure('TLabel', background='#F0F0F0')

window.mainloop()
