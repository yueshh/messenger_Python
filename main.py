from tkinter import *
from Register import *
from Login import *
from Chat import *
import tkinter.ttk as ttk

window = Tk()
window.title("Messenger")
window.geometry("270x130")
window.resizable(False, False)

ttk.Style().theme_use("clam")


login = Login(window)
register = Register(window)

login.add_switch(lambda: register.frame.pack())
register.add_switch(lambda: login.frame.pack())

login.frame.pack()
window.mainloop()
