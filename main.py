import tkinter as ttk
from tkinter.ttk import *
from Register import *
from Login import *

window = ttk.Tk()

window.title("Messenger")
window.geometry("270x170")
window.resizable(False, False)

login = Login(window)
register = Register(window)

login.add_switch(lambda: register.frame.pack())
register.add_switch(lambda: login.frame.pack())

login.frame.pack()
style = Style()
style.theme_use('clam')
style.configure('TLabel', background='#F0F0F0')

window.mainloop()
