import streamlit as st

st.title("AI Financial Advisor - Week 1 Prototype")

income = st.number_input("Enter Monthly Income")

if st.button("Calculate"):
    st.write("Needs:", income * 0.5)
    st.write("Wants:", income * 0.3)
    st.write("Savings:", income * 0.2)