import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Pratosh Bharani")
    content = """
    Hi, I am Pratosh! I'm a data analyst, a Python programmer, and an amateur photographer.
    """
    st.info(content)
st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, col4 = st.columns(2)

# Import the dataset
df = pd.read_csv("data.csv", sep=";")

with col3:
    for ind in df[:10].index:
        st.header(df['title'][ind])

with col4:
    for ind in df[10:].index:
        st.header(df['title'][ind])