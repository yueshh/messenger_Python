import tkinter as ttk
from tkinter.ttk import *
from actions_password import hash_password, password_verification
import requests
import json
from Frames import *


class Register(Frames):

    def __init__(self, window):
        super().__init__(window)
        self.frame = ttk.Frame(window, padx=1, pady=170)
        self.items = [
            {'clmn': 0, 'rw': 4, 'cs': 2, 'rs': 1, "name": "error",    'object': Label(self.frame, text="")},
            {'clmn': 0, 'rw': 0, 'cs': 1, 'rs': 1, "name": "",         'object': Label(self.frame, text='логин')},
            {'clmn': 1, 'rw': 0, 'cs': 1, 'rs': 1, "name": "login",    'object': Entry(self.frame)},
            {'clmn': 0, 'rw': 1, 'cs': 1, 'rs': 1, "name": "",         'object': Label(self.frame, text='пароль')},
            {'clmn': 1, 'rw': 1, 'cs': 1, 'rs': 1, "name": "password", 'object': Entry(self.frame)},
            {'clmn': 0, 'rw': 2, 'cs': 1, 'rs': 1, "name": "",         'object': Label(self.frame, text="повторите пароль")},
            {'clmn': 1, 'rw': 2, 'cs': 1, 'rs': 1, "name": "con_pass", 'object': Entry(self.frame)},
            {'clmn': 1, 'rw': 3, 'cs': 1, 'rs': 1, "name": "",         'object':
                Button(self.frame, text='Создать аккаунт', command=self.register)},
            {'clmn': 0, 'rw': 3, 'cs': 1, 'rs': 1, "name": "",         'object':
                Button(self.frame, text='Вернуться к входу', command=lambda: self.switcher('login'))},
        ]
        super().add_items()

    def register(self):
        login_entry = self.get_element("login")
        password_entry = self.get_element("password")
        conf_psswrd_entry = self.get_element("con_pass")

        if (not isinstance(login_entry, Entry)
                or not isinstance(password_entry, Entry)
                or not isinstance(conf_psswrd_entry, Entry)):
            raise Exception('ошибка')
        conf_password = conf_psswrd_entry.get()
        password = password_entry.get()
        result = password_verification(password, conf_password)
        if not result[0]:
            self.get_element('error').config(text=result[1])
            return
        user = {
            "username": login_entry.get(),
            "password": hash_password(password),
        }
        res = requests.post(f"http://194.146.240.26:2001/register", json=user)
        response = json.loads(res.text)
        if response['error']:
            self.get_element('error').config(text=response["message"])
            print(response["message"])
        else:
            self.switcher("chat")
