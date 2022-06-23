import plotly.express as px
import pandas as pd

#prints the cumulative data from the first script
df = pd.read_csv(f'results.csv')
fig = px.scatter_geo(df, lat = 'Latitude', lon = 'Longitude', hover_name = 'Timestamp')
fig.update_layout(title = 'ISS Trajectory', title_x = 1)
fig.show()