import tkinter as ttk
from tkinter.ttk import *
import requests
import json
from actions_password import hash_password
from Frames import *



class Login(Frames):

    def __init__(self, window):
        super().__init__(window)
        self.frame = ttk.Frame(window, padx=1, pady=180)
        self.items = [
            {'clmn': 0, 'rw': 3, 'cs': 2, 'rs': 1, "name": "error",    'object': Label(self.frame, text="")},
            {'clmn': 0, 'rw': 0, 'cs': 1, 'rs': 1, "name": "",         'object': Label(self.frame, text='логин')},
            {'clmn': 1, 'rw': 0, 'cs': 1, 'rs': 1, "name": "login",    'object': Entry(self.frame)},
            {'clmn': 0, 'rw': 1, 'cs': 1, 'rs': 1, "name": "",         'object': Label(self.frame, text='пароль')},
            {'clmn': 1, 'rw': 1, 'cs': 1, 'rs': 1, "name": "password", 'object': Entry(self.frame)},
            {'clmn': 0, 'rw': 2, 'cs': 1, 'rs': 1, "name": "",         'object':
                Button(self.frame, text='войти', command=self.login)},
            {'clmn': 1, 'rw': 2, 'cs': 1, 'rs': 1, "name": "",         'object':
                Button(self.frame, text='регистрация', command=lambda: self.switcher('register'))},
        ]
        super().add_items()

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
        if response['error']:
            self.get_element('error').config(text=response["message"])
            print(response["message"])
        else:
            file = open('session_key', 'a')
            file.write(response['data']['session_key'])
            file.close()
            self.switcher("chat")

