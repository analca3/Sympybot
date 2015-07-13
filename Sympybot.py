#!/usr/bin/env python3
import telebot
import time
from LaTeX2IMG import LaTeX2IMG
from time import sleep
from threading import current_thread
from sympy import *

TOKEN = ''


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            if text[0:7] == "/ ":
                pass
            elif text[0] == "@":
                pass
            else:
                break

            tb.send_chat_action(chatid,'upload_document')

            filename = 'resultado' + current_thread().name

            ###########
            # Add calculus
            ###########

            LaTeX2IMG.main(['LaTeX2IMG',text,filename,'webp'])
            result = open(filename + '.webp','rb')
            tb.send_sticker(chatid, result)

with open("token.txt","r") as file:
    TOKEN = file.readline().strip()
init_session()  # Init sympy session
tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()

while True: # Don't let the main Thread end.
    sleep(5)
