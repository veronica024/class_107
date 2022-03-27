import pandas as pd
import csv
import plotly.scattor_plot as sp

df = pd.read_csv("data.csv")

student_df = df.loc[df['student_id'] == "TRL_zny"]

print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
            x=student_df.groupby("level")["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            orientation='h'))

fig.show()
