import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='IPL', value='tab-1'),
        dcc.Tab(label='ODI', value='tab-2'),
    ]),
    html.Div(id='tabs-example-content')
])

@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Background on IPL'),
            html.P('Indian Premier League (IPL), Indian professional Twenty20 (T20) cricket league established in 2008. The league, which is based on a round-robin group and knockout format, has teams in major Indian cities. Matches generally begin in late afternoon or evening so that at least a portion of them are played under floodlights at night to maximize the television audience for worldwide broadcasts. The top four teams contest three play-off matches, with one losing team being given a second chance to reach the final, a wrinkle aimed at maximizing potential television revenue. The play-off portion of the tournament involves the four teams that finished at the top of the tables in a series of knockout games that allows one team that lost its first-round game a second chance to advance to the final match'),

            html.P('With the advent of the IPL, almost overnight the world’s best cricketers—who had seldom made the kind of money earned by their counterparts in other professional sports—became millionaires. The owners of the IPL franchises, who included major companies, Bollywood film stars, and media moguls, bid for the best players in auctions organized by the league. The eight founding franchises were the Mumbai Indians, the Chennai Super Kings, the Royal Challengers Bangalore, the Deccan Chargers (based in Hyderabad), the Delhi Daredevils, the Punjab XI Kings (Mohali), the Kolkata Knight Riders, and the Rajasthan Royals (Jaipur). In late 2010 two franchises, Rajasthan and Punjab, were expelled from the league by the BCCI for breeches of ownership policy, but they were later reinstated in time for the 2011 tournament. Two new franchises, the Pune Warriors India and the Kochi Tuskers Kerala, joined the IPL for the 2011 tournament. The Kochi club played just one year before the BCCI terminated its contract. In 2013 the Deccan Chargers were replaced in the IPL by the Sunrisers Hyderabad.'),
  
            
        ],style={'display': 'inline-block', 'width': '100%', 'background-color':'DeepSkyBlue', 'color': 'White', 'text-indent': '5%'})

    elif tab == 'tab-2':
        return html.Div([
            html.H3('Background on ODI'),
            html.P('A One Day International (ODI) is a form of limited overs cricket, played between two teams with international status, in which each team faces a fixed number of overs, currently 50 (used to be 60 overs until 1983), with the game lasting up to 8 hours. The Cricket World Cup, generally held every four years, is played in this format. One Day International matches are also called Limited Overs Internationals (LOI), although this generic term may also refer to Twenty20 International matches. They are major matches and considered the highest standard of List A, limited-overs competition.'),
        ],style={'display': 'inline-block', 'width': '100%', 'background-color':'DeepSkyBlue', 'color': 'White', 'text-indent': '5%'})



if __name__ == '__main__':
    app.run_server(debug=True)

    
