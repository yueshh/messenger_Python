import tkinter as ttk
from tkinter.ttk import *
import requests
import json
from actions_password import hash_password
from Frames import *


class Chat(Frames):
    def __init__(self, window):
        super().__init__(window)
        self.frame = ttk.Frame(window, padx=1, pady=1)
        self.items = [
            {'clmn': 0, 'rw': 0, 'cs': 2, 'rs': 1, "name": "messanger", 'object': Label(self.frame, text='')},
            {'clmn': 0, 'rw': 0, 'cs': 2, 'rs': 1, "name": "error", 'object': Label(self.frame, text="")},
            {'clmn': 1, 'rw': 2, 'cs': 1, 'rs': 1, "name": "", 'object':
                Button(self.frame, text='обновить чат', command=self.update_chat)},
        ]
        self.add_items()

    def update_chat(self):
        messages = self.get_messages()
        result = ''
        for i in messages:
            result += str(i["user_id"]) + '\n' + i["body"] + ' ' + i["send_time"] + '\n'
        self.get_element('messanger').config(text=result)
    def get_messages(self):
        file = open('session_key', 'r')
        self.session_key = file.read(40)
        file.close()
        req = {
            "session_key": self.session_key
        }
        res = requests.post(f"http://194.146.240.26:2001/get", json=req)
        response = json.loads(res.text)
        if response['error']:
            self.get_element('error').config(text=response["message"])
            print(response["message"])
            return []
        else:
            return response["data"]