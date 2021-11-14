import streamlit as st
import pandas as pd

st.text('Hello world')
x = st.slider('x') 
st.write(x, 'squared is', x * x)

option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

hoja = pd.read_csv('prueba.csv')
hoja.head()