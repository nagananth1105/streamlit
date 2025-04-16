import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.markdown("<h1 style='text-align:center;'>User Registration</h1>", unsafe_allow_html=True)
label=pd.DataFrame({"columns":["1","2","3"],"columns3":["100","200","300"]})
x=np.linspace(0,10,100)
with st.form("form 1"):
    col1, col2 = st.columns(2)
    first= col1.text_input("First Name", placeholder="Enter your first name", max_chars=20)
    last=col2.text_input("Last Name", placeholder="Enter your last name", max_chars=20)
    st.text_input("Password", placeholder="Enter your password", max_chars=20, type="password")
    st.text_input("Confirm Password", placeholder="Confirm your password", max_chars=20, type="password")
    st.text_input("Email", placeholder="Enter your email", max_chars=30)
    st.text_input("Phone Number", placeholder="Enter your phone number", max_chars=15)
    day,month,year=st.columns(3)
    day.text_input("Day", placeholder="DD", max_chars=2)
    month.text_input("Month", placeholder="MM", max_chars=2)
    year.text_input("Year", placeholder="YYYY", max_chars=4)
    submitted = st.form_submit_button("Submit")
    if submitted:
        if first=="" and last=="" :
            st.warning("Please enter your first and last name.")
        else:
            st.success("your registration is successful!")

opt=st.sidebar.radio("select the preffered chart for your data",options=["bar","line","pie"])
if opt=="line":
  fig=plt.figure(figsize=(10,5))
  plt.style.use('ggplot')
  plt.plot(x,np.sin(x))
  plt.plot(x,np.cos(x))
  st.write(fig)
elif opt=="bar":
  fig=plt.figure(figsize=(10,5))
  plt.bar(label.columns,label.columns)
  st.write(fig)
elif opt=="pie":
  fig=plt.figure(figsize=(10,5))
  plt.pie(label.columns,labels=label.columns)
  st.write(fig)
else:
  st.write("please select the chart type")



