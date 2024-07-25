import tkinter as ttk
from tkinter.ttk import *
import requests
import json
from actions_password import hash_password


class Login:

    def __init__(self, window):
        self.switch = None
        self.frame = ttk.Frame(window, padx=1, pady=1)
        self.items = [
            {'clmn': 0, 'rw': 3, 'cs': 2, 'rs': 1, "name": "error",    'object': Label(self.frame, text="")},
            {'clmn': 0, 'rw': 0, 'cs': 1, 'rs': 1, "name": "",         'object': Label(self.frame, text='логин')},
            {'clmn': 1, 'rw': 0, 'cs': 1, 'rs': 1, "name": "login",    'object': Entry(self.frame)},
            {'clmn': 0, 'rw': 1, 'cs': 1, 'rs': 1, "name": "",         'object': Label(self.frame, text='пароль')},
            {'clmn': 1, 'rw': 1, 'cs': 1, 'rs': 1, "name": "password", 'object': Entry(self.frame)},
            {'clmn': 0, 'rw': 2, 'cs': 1, 'rs': 1, "name": "",         'object':
                Button(self.frame, text='войти', command=self.login)},
            {'clmn': 1, 'rw': 2, 'cs': 1, 'rs': 1, "name": "",         'object':
                Button(self.frame, text='регистрация', command=self.switcher)},
        ]
        self.add_items()

    def add_items(self):
        for i in self.items:
            i["object"].grid(column=i["clmn"], row=i["rw"], columnspan=i['cs'], rowspan=i['rs'], padx=5, pady=5)
            
    def get_element(self, name: str):
        for i in self.items:
            if i['name'] == name:
                return i['object']
        raise Exception('вызвана не сущ entry')

    def switcher(self):
        self.frame.pack_forget()
        self.switch()

    def add_switch(self, switch):
        self.switch = switch

    def login(self):
        login_entry = self.get_element("login")
        password_entry = self.get_element("password")
        if not isinstance(login_entry, Entry) or not isinstance(password_entry, Entry):
            raise Exception('ошибка')
        user = {
            "username": login_entry.get(),
            "password": hash_password(password_entry.get()),
        }
        res = requests.post(f"http://194.146.240.26:2001/login", json=user)
        response = json.loads(res.text)
        print(response)
        if response['error']:
            self.get_element('error').config(text=response["message"])
            print(response["message"])
        else:
            self.get_element('error').config(text="Вы вошли!!!")
