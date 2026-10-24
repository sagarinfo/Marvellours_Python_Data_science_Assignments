import streamlit as st

st.title("Even or Odd Number")

number = st.number_input("Enter an integer", value=0, step=1)

if st.button("Check"):
    if number % 2 == 0:
        st.success(f"{number} is an Even number")
    else:
        st.info(f"{number} is an Odd number")