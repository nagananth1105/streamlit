import streamlit as st
input=st.text_input("Enter your name", max_chars=20, placeholder="Enter your name")
button=st.button("Submit")
if button:
    option= st.checkbox("Do you want to proceed?", value=True)
    if option:
       print(input)