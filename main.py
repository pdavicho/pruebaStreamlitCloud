import streamlit as st

st.text('Hello world')
x = st.slider('x') 
st.write(x, 'squared is', x * x)

option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)
