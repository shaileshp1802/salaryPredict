import streamlit as st
import pandas as pd

st.header("Contribute to our dataset")
exp = st.number_input("Enter Your Exp",0,20)
sal = st.number_input("Enter Your Salary",0,2100000)

exp
sal

if st.button("Submit"):
    to_add = {
        'YearsExperience': [exp],
        'Salary': [sal]
    }
    to_add = pd.DataFrame(to_add)
    to_add.to_csv("./data/data.csv",mode="a",header=False,index=False)
    st.success("Submitted")

