
import dash
import dash_html_components as html
import dash_core_components as dcc



app = dash.Dash(__name__)

# Define app layout with a navigation bar and empty page content
app.layout = html.Div([
    
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Monitoring', href='/monitoring', className='nav-link'),
        

        
        dcc.Link('Prediction', href='/prediction', className='nav-link')
    ], className='nav'),
    html.Div([
        html.Div(id='page-content', className='content')
    ], className='hello')
], style={ 'margin': 'auto', 'textAlign': 'center'})


    

# Define the callbacks to update the page content based on the URL
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/monitoring':
        return html.Div(
            children=[html.H1('Analysis of Relationship between Macroeconomic Indicators & ETFs'),
            html.H2('Monitoring page 📈')]
            
        )
    
    elif pathname == '/prediction':
        return html.Div(
            children=[html.H1('Analysis of Relationship between Macroeconomic Indicators & ETFs'),
            html.H2('Prediction page 🤖')]
            
        )
    else:
        return html.H1('Analysis of Relationship between Macroeconomic Indicators & ETFs')


# , style={'textAlign': 'center'}
if __name__ == '__main__':
    app.run_server()
