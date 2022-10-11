import imp
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

st.image("data:image/png;base64,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")

if st.checkbox("Show Table"):
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
