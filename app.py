import streamlit as streamlit
import joblib
model=joblib.load('spam-ham')
st.title('SPAM-HAM CLASSIFER')
ip=st.text_input('Enter message')
op=model.predict([ip])
if st.button('Predict'):
st.title(op[0])




