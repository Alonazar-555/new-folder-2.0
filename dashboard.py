import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample DataFrame for demonstration
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [23, 17, 35, 29]
})

# Create a bar chart using Plotly Express
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children="Sample Dashboard"),
    html.Div(children='A simple example dashboard with Dash and Plotly.'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)