# import requirements
import streamlit as st
import telethon
from telegram import Bot
import time
from random import randint
import requests
import os

import asyncio
from telethon.sync import TelegramClient

# asyncio.set_event_loop(loop)
import asyncio


# def get_or_create_eventloop():
#     try:
#         return asyncio.get_event_loop()
#     except RuntimeError as ex:
#       if "There is no current event loop in thread" in str(ex):
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             return asyncio.get_event_loop()
# get_or_create_eventloop()
# if "loop" not in st.session_state:
#     st.session_state.loop = asyncio.new_event_loop()
# asyncio.set_event_loop(st.session_state.loop)



title = st.text_input('Movie title2222', '')
st.write('The current movie title is', title)

bot=Bot(requirements.TOKEN)
bulkchan=-1001861555690
#***************************Telethon signin part
# @st.experimental_singleton
# def sendcode():
#       loop = asyncio.new_event_loop()
#       asyncio.set_event_loop(loop)
#       client=TelegramClient(requirements.SESSION_NAME ,requirements.api_id ,requirements.api_hash, loop=loop)#, loop=loop
#       st.write(client.is_connected())
#       client.connect()
#       st.write("connectiong")
#       rpl=client.send_code_request(requirements.phone)
#       print(rpl)
#       st.write(f"rpl: {rpl.phone_code_hash}")
#       st.session_state['phash']=rpl.phone_code_hash
#       st.write(f"rpl: {st.session_state['phash']}")
#       st.write("sent")
#       client.disconnect()
#       return rpl.phone_code_hash

# if st.button('Say hello'):
#       st.write('Why wwwww there')
#       rp=sendcode()
#       print(f"rp:{rp}")
#       print(f"session_state:{st.session_state['phash']}")
#       ee=f"session_state:{st.session_state['phash']}"
#       st.write(st.session_state['phash'])
      
# else:
#       st.write('Goodbye')

# if st.button('come in'):
#       if title!='':
#             st.write('sdf')
#             loop = asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#             client=TelegramClient(requirements.SESSION_NAME ,requirements.api_id ,requirements.api_hash, loop=loop)#, loop=loop
#             st.write(client.is_connected())
#             client.connect()
#             st.write("connectiong")
#             st.write(title)
#             st.write(st.session_state['phash'])
#             client.sign_in(phone=requirements.phone, code=title,phone_code_hash=st.session_state['phash'])
# else:
#       st.write('Goodbye')
#EOF***************************Telethon signin part
@st.cache(ttl = 30)
def sendmes():
      res=bot.send_message(bulkchan,"STREAMLIT")
header=st.container()
with header:
      st.title('Hello Guys*******')


# sendmes()


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
