from tkinter import *
import requests
import json


class Register:

    def __init__(self, window):
        self.switch = None
        self.frame = Frame(window, padx=1, pady=1)
        self.items = [
            {'column': 1, 'row': 2, "name": "error",    'object': Label(self.frame, text="")},
            {'column': 0, 'row': 0, "name": "",         'object': Label(self.frame, text='логин')},
            {'column': 1, 'row': 0, "name": "login",    'object': Entry(self.frame)},
            {'column': 0, 'row': 1, "name": "",         'object': Label(self.frame, text='пароль')},
            {'column': 1, 'row': 1, "name": "password", 'object': Entry(self.frame)},
            {'column': 0, 'row': 2, "name": "",         'object': Label(self.frame, text="повторите пароль")},
            {'column': 1, 'row': 2, "name": "con_pass", 'object': Entry(self.frame)},
            {'column': 1, 'row': 3, "name": "",         'object':
                Button(self.frame, text='Создать аккаунт', command=self.register)},
            {'column': 0, 'row': 3, "name": "",         'object':
                Button(self.frame, text='Вернуться к входу', command=self.switcher)},
        ]
        self.add_items()

    def add_items(self):
        for i in self.items:
            i["object"].grid(column=i["column"], row=i["row"], padx=5, pady=5)

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

    def register(self):
        user = {
            "username": self.get_element("login").get(),
            "password": self.get_element("password").get(),
            "confirm_password": self.get_element("con_pass").get()
        }
        res = requests.post(f"http://194.146.240.26:2001/register", json=user)
        response = json.loads(res.text)
        print(response)
        if response['error']:
            self.get_element('error').config(text=response["message"])
            print(response["message"])
        else:
            self.get_element('error').config(text="Вы вошли!!!")
