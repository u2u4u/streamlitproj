import requirements
import streamlit as st
import telethon
from telegram import Bot
import time
from random import randint

import os

import asyncio
from telethon.sync import TelegramClient
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
client=TelegramClient(requirements.SESSION_NAME ,requirements.api_id ,requirements.api_hash, loop=loop)

title = st.text_input('Movie title', '')
st.write('The current movie title is', title)

bot=Bot(requirements.TOKEN)
bulkchan=-1001861555690


if st.button('Say hello'):
    st.write('Why hello there')
    client.connect()
    client.send_code_request(requirements.phone)

else:
    st.write('Goodbye')

if st.button('come in'):
      if title!='':
            st.write('sdf')
            client.sign_in(requirements.phone, title)
else:
      st.write('Goodbye')

@st.cache(ttl = 30)
def sendmes():
      res=bot.send_message(bulkchan,"STREAMLIT")
header=st.container()
with header:
      st.title('Hello Guys*******')


sendmes()


# f = open("demofile2.txt", "w")
# f.write("Now the file has more content!")
# f.close()
# from pathlib import Path
# print(Path.cwd())
# print('1---------------------------------')
# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read()) 
# print('2---------------------------------')
# import os
# print('Get current working directory : ', os.getcwd())
# print('3---------------------------------')
# print('File name :    ', os.path.basename(__file__))
# print('Directory Name:     ', os.path.dirname(__file__))
# print('4---------------------------------')
# print('Absolute path of file:     ',
#       os.path.abspath(__file__))
# print('Absolute directoryname: ',
#       os.path.dirname(os.path.abspath(__file__)))
# print('5---------------------------------')
# nfile = 'demofile2.txt'
# print("Path of the file..", os.path.abspath(nfile))
