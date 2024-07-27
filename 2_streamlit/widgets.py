import streamlit as st
import pandas as pd

st.title("Stremlit Text Input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is {age}")

if name:
    st.write(f"Hello, {name}")
    
options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}")


st.title("Separation")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 35, 46, 23],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
