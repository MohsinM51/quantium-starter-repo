from dash import Dash, html, dcc, callback, Input, Output  # import statements
import plotly.express as px
import pandas as pd

# Reading CSV file data
data = pd.read_csv('pink_morsel_data.csv')

# Converting date column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Initializing Dash app
app = Dash(__name__)

# Defining layout of Dash app
app.layout = html.Div(className='container',  # Apply a CSS class named 'container' to the main Div
                      children=[
                          html.H1(children='Pink Morsel Sales', style={'text-align': 'center'}),  # Text content of the H1 element
                          dcc.RadioItems(
                              id='radio-items',
                              options=[
                                  {'label': 'North', 'value': 'north'},
                                  {'label': 'South', 'value': 'south'},
                                  {'label': 'East', 'value': 'east'},
                                  {'label': 'West', 'value': 'west'},
                                  {'label': 'All', 'value': 'all'}
                              ],
                              value='north',
                              labelStyle={'display': 'inline-block', 'margin': '0 15px 0 0'},  # Increased margin-right
                              className='radio-items'
                          ),
                          dcc.Graph(id='pink-morsel-graph', style={'height': '50em'})  # Graph element
                      ]
                      )

@callback(
    Output('pink-morsel-graph', 'figure'),
    Input('radio-items', 'value')
)
def update_graph(chosen_region):
    if chosen_region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'] == chosen_region]

    # Creating line graph using Plotly Express
    fig = px.line(filtered_data,
                  x='date', y='sales',  # x and y axis initialization
                  title='Sales Over Time',  # title
                  labels={'date': 'DATE', 'sales': 'SALES $'},  # axis labelling
                  template='plotly_dark',  # theme
                  color_discrete_sequence=['#B1DDF1']  # graph line color
                  )

    # Updating plot layout
    fig.update_layout(
        title={'x': 0.5},  # Center the title
        font=dict(family='Arial, sans-serif', size=20, color='white'),  # Change the font
        plot_bgcolor='#2a2a2a',  # Change the plot background color
        paper_bgcolor='#1a1a1a',  # Change the paper background color
        xaxis=dict(showgrid=True, gridcolor='#444444'),  # Customize x axis grid lines
        yaxis=dict(showgrid=True, gridcolor='#444444', dtick=100)  # Customize y axis grid lines
    )
    return fig

# Running app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
