import streamlit as st

 # Title of the app
st.title("Student Information")




import streamlit as st
import pandas as pd
with st.form("my_form"):
   name=st.text_input("Enter the student's name", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible", icon=None, width="stretch", bind=None)
   age=st.slider("Select the student's age", min_value=1, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch", bind=None)

   st.form_submit_button('Display Information')



st.write(f"Student's name : {name}")
st.write(f"Student's age : {age}")