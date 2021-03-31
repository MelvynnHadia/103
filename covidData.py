import pandas as pd

import plotly.express as px

df = pd.read_csv("csv files/data.csv")

fig = px.bar(df, x="Date", y="Infected",color = "Country",title = 'Covid Infection Statistics')

fig.show()