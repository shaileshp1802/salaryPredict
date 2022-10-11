import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("./data/data.csv")

x = np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data["Salary"]))

st.title("Salary Predictor")

st.image("./images/salary.png")

if st.checkbox("Show Data Used"):
    st.dataframe(data)

val = st.slider("Filter Data Years", 0 , 15)
data = data.loc[data["YearsExperience"] >= val]

exp = st.number_input("Enter your exp", 0.00, 20.00, step = 0.25)
exp = np.array(exp).reshape(1,-1)
pred = lr.predict(exp)[0]

if st.button("Predict"):
    st.success(f"Predicte Salary is {round(pred)}")

# graph = st.selectbox("What kind of garph?", ['Interactive', 'Non-interactive'])

# if graph == 'Interactive':
#     layout = go.Layout(
#         xaxis = dict(range=[0,16]),
#         yaxis = dict(range=[0,2100000])
#     )
#     fig = go.Figure(data=go.scatter(x=data['YearsExperience'], y=data['Salary'], mode='marker'))
#     st.plotly_chart(fig)
# if graph == 'Non-interactive':
plt.figure(figsize=(10,5))
plt.scatter(data['YearsExperience'], data['Salary'])
plt.ylim(0)
plt.xlabel("Years of Exp")
plt.ylabel("Salary")
plt.tight_layout()
st.pyplot()

