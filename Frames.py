import tkinter as ttk
from tkinter.ttk import *


class Frames:
    items = []
    frame = None

    def __init__(self, window):
        self.switch = {}

    def add_items(self):
        for i in self.items:
            i["object"].grid(column=i["clmn"], row=i["rw"], columnspan=i['cs'], rowspan=i['rs'], padx=5, pady=5)

    def get_element(self, name: str):
        for i in self.items:
            if i['name'] == name:
                return i['object']
        raise Exception('вызвана не сущ entry')

    def switcher(self, frame_name: str):
        self.frame.pack_forget()
        self.switch[frame_name].pack()

    def add_switch(self, switch_name: str, switch):
        self.switch[switch_name] = switch

        