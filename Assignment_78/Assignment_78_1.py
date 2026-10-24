import streamlit as st

st.title("Addition of Two Numbers")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

if st.button("Add"):
    st.success(f"Sum = {num1 + num2}")