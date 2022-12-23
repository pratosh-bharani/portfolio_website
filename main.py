import streamlit as st

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