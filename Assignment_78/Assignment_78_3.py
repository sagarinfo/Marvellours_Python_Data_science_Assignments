import streamlit as st

st.title("Simple Interest Calculator")

principal = st.number_input("Principal Amount", min_value=0.0, value=1000.0)
rate = st.number_input("Rate of Interest (% per year)", min_value=0.0, value=5.0)
time = st.number_input("Time Period (years)", min_value=0.0, value=1.0)

if st.button("Calculate"):
    si = (principal * rate * time) / 100
    st.success(f"Simple Interest = {si:.2f}")
    st.write(f"Total Amount = {principal + si:.2f}")