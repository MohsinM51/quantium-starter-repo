from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


data= pd.read_csv('pink_morsel_data.csv')

data['date']=pd.to_datetime(data['date'])

app = Dash(__name__)

fig = px.line(data,
              x='date', y='sales',
              title='Sales Over Time',
              labels={'date': 'Date', 'sales': 'Sales'},
              template='plotly_dark',
              color_discrete_sequence=['lightgreen'])
fig.update_layout(
    title={'x': 0.5},  # Center the title
    xaxis_title='Date',
    yaxis_title='Sales',
    font=dict(family='Arial, sans-serif', size=20, color='white'),  # Change the font
    plot_bgcolor='#2a2a2a',  # Change the plot background color
    paper_bgcolor='#1a1a1a',  # Change the paper background color
    xaxis=dict(showgrid=True, gridcolor='#444444'),  # Customize grid lines
    yaxis=dict(showgrid=True, gridcolor='#444444')
)

app.layout = html.Div(className='container',children=[
    html.H1(children='Pink Morsel Data', style={'text-align': 'center'}),
    dcc.Graph(id='pink-morsel-graph', figure=fig)
])


if __name__ == '__main__':
    app.run(debug=True)