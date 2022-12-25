import streamlit as st
import telethon
from telegram import Bot
import time
from random import randint

import os

TOKEN="5835458437:AAEQLztS3xnaPX2BtY183nV2aTXgssZa-5o"#oosfeebot
bot=Bot(TOKEN)
bulkchan=-1001861555690

@st.cache(persist=True,ttl = 100)
def sendmes():
      res=bot.send_message(bulkchan,"STREAMLIT")
header=st.container()
with header:
      st.title('Hello Guys888')


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
