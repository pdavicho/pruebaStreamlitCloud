import streamlit as st

st.text('Hello world')
x = st.slider('x') 
st.write(x, 'squared is', x * x)
