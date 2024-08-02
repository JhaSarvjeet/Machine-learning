import streamlit as st
import pandas as pd
st.title("Steamlit text input")
name=st.text_input("enter your name")
if name:
    st.write(f"Hello {name}")

#slider
age=st.slider("enter age",0,100,10)
st.write(f"your age is {age}")

#dropdown
option=['python','java','C++','c']
choice=st.selectbox("choose your option",option)
st.write(f"you selected {choice}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df=pd.DataFrame(data)
df.to_csv("test.csv")
st.write(df)


uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)