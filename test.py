import streamlit as st
from datetime import datetime as dt

@st.experimental_singleton
def sendcode():
    return "My Code"


if st.button('Say hello'):
      mm=sendcode()
      st.session_state['mm']=mm
      now=dt.now()
      st.session_state['now']=now
      st.write(now.day)


if st.button('How are you'):
      st.write("How are you")



if st.button('goodbye'):
      st.write(st.session_state['mm'])
      st.write(st.session_state['now'].day)

    