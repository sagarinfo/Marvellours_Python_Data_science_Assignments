import streamlit as st

st.title("Student Result Calculator")

name = st.text_input("Student Name")
m1 = st.number_input("Marks in Subject 1 (out of 100)", min_value=0, max_value=100, value=0)
m2 = st.number_input("Marks in Subject 2 (out of 100)", min_value=0, max_value=100, value=0)
m3 = st.number_input("Marks in Subject 3 (out of 100)", min_value=0, max_value=100, value=0)

if st.button("Calculate Result"):
    if not name.strip():
        st.warning("Please enter the student's name.")
    else:
        total = m1 + m2 + m3
        percentage = total / 300 * 100

        st.write(f"**Name:** {name}")
        st.write(f"**Total Marks:** {total} / 300")
        st.write(f"**Percentage:** {percentage:.2f}%")

        # Must score at least 40 in every subject to pass
        if m1 >= 40 and m2 >= 40 and m3 >= 40:
            st.success(f"{name} has PASSED")
        else:
            st.error(f"{name} has FAILED")