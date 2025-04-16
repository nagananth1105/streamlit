import streamlit as st
import pandas as pd
import time as tt
from datetime import time as time
table=pd.DataFrame({"columns":["1","2","3"],"values":[1,2,3]})
st.title("Hello World")
st.markdown("---")
x="""
print("Hello World")
def function():
if(True):
    print("Hello World")
else:
    print("Goodbye World")
"""
st.code(x, language='python')
y={"a":1,"b":2,"c":3}
st.json(y)
st.latex(r"\begin{pmatrix}a & b \\ c & d\end{pmatrix}")
st.metric(label="wind speed",value="120ms⁻¹",delta="1.4ms⁻¹")
st.table(table)
label=st.checkbox("answer",value=True)
if label:
    st.write("hi")
else:
    pass
st.image("images.jpg",caption="nagananth" ,width=100)
st.file_uploader("pls upload your images to analyze",type=['jpg','png'])
x=st.multiselect("select your faviourt cars",options=["audi","bmw","mercedes"])
print(x)
y=st.slider("select your character" ,min_value=0,max_value=100)
input=st.text_input("enter the text",max_chars=y)
input2=st.text_area("enter the text",max_chars=y)
date=st.date_input("enter the date",min_value=pd.to_datetime("2023-01-01"),max_value=pd.to_datetime("2023-12-31"))
time=st.time_input("enter the time",value=time(0,0,0))
if str(time)=="00:00:00":
    st.write("please set the timer ")
else:
   bar=st.progress(0)
   p_status=st.empty()
   for i in range(10):
       bar.progress((i+1)*10)
       p_status.write(str(i+1)+"%" +"completed")
       tt.sleep(1)
       st.spinner("loading...")