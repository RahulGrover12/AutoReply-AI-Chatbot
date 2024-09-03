# Copyright @ Rahul Grover
# https://www.github.com/RahulGrover12
# Auto Reply AI ChatBot

import pyautogui as pyg
import time
import pyperclip
from client_openAi import aiProcess
import os

def check_last_message(chat_log,sender_name="Rahul Grover"):
    message = chat_log.strip().split("/2024]")[-1]
    if(not sender_name in message):
        return True
    return False


def append_to_file(file_path, text):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")

file_path = "chat.txt"

pyg.click(465, 1056)
time.sleep(1.5)

last_reply = ""

while True:

    if os.path.exists(file_path):
        os.remove(file_path)

    pyg.moveTo(676, 199)
    pyg.dragTo(1875, 932, duration=1.5, button="left")

    pyg.hotkey('ctrl','c')
    pyg.click(1232, 513)
    time.sleep(1.5)

    chat_history = pyperclip.paste()
    # print(chat_history)
    append_to_file(file_path, chat_history)

    if(check_last_message(chat_history)):
        reply = aiProcess(chat_history)
        print(reply)
        if(reply!=last_reply):
            pyperclip.copy(reply)

            pyg.click(1065, 984)
            time.sleep(1.5)

            pyg.hotkey('ctrl', 'v')
            time.sleep(1.5)

            pyg.press('enter')
            last_reply = reply
    
    time.sleep(2)