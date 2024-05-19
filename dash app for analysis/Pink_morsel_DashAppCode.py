from dash import Dash, html, dcc #import statements
import plotly.express as px
import pandas as pd


data= pd.read_csv('pink_morsel_data.csv') #reading csv file data

data['date']=pd.to_datetime(data['date']) #converting date column in date format

app = Dash(__name__) #initializing dash app

#creating line graph using plotly express
fig = px.line(data,
              x='date', y='sales', #x and y axis initialization
              title='Sales Over Time', #title
              labels={'date': 'Date', 'sales': 'Sales'}, #axis labelling
              template='plotly_dark', #theme
              color_discrete_sequence=['lightgreen'] #graph line color
              )

#updating plot layout
fig.update_layout(
    title={'x': 0.5},  # Center the title
    font=dict(family='Arial, sans-serif', size=20, color='white'),  # Change the font
    plot_bgcolor='#2a2a2a',  # Change the plot background color
    paper_bgcolor='#1a1a1a',  # Change the paper background color
    xaxis=dict(showgrid=True, gridcolor='#444444'),  # Customize x axis grid lines
    yaxis=dict(showgrid=True, gridcolor='#444444')  # Customize y axis grid lines
)

#defining layout of dashapp
app.layout = html.Div(className='container', # Apply a CSS class named 'container' to the main Div
                      children=[
                          html.H1(children='Pink Morsel Data',style={'text-align': 'center'}),  # Text content of the H1 element
                          dcc.Graph(id='pink-morsel-graph', figure=fig) #fig as graph
                      ]
                      )

#running app in debug mode
if __name__ == '__main__':
    app.run(debug=True)