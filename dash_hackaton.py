### PROJET DASH MORITZ ###

import dash
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import numpy as np  # pip install dash (version 2.0.0 or higher)
import plotly.io as pio
pio.renderers.default='browser'
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.CYBORG])
#app = dash.Dash(__name__, external_stylesheets = [dbc.themes.FLATLY])
server = app.server
colors = {
    'background': '#000000', 
    'text': '#7FDBFF'
}

# on clear un peu et on fait des moyennes
url = 'https://raw.githubusercontent.com/LarryJr64/dashboard_hackaton/main/CLAUDE_DILETTA_ROUSSEAU.csv'
df = pd.read_csv(url, sep = ',')
df['INNOVATION']= (df['UTILITE_INNOVATION'] + df['INFORMATION_INNOVATION'])/2
df['INTERET_PARTICIPANT'] = (df['INTERET_PARTICIPANT1'] + df['INTERET_PARTICIPANT2'])/2
df['NETWORKING']= (df['NETWORKING1'] + df['NETWORKING2'] + df['NETWORKING3'] + df['NETWORKING4'] + df['NETWORKING5'])/5
df['SELF_IMPROVEMENT'] = (df['SELF_IMPROVEMENT1']+df['SELF_IMPROVEMENT2'])/2
#df.drop(df.iloc[:, 0:19], inplace=True, axis=1)
df = df.drop('Network ID', axis=1)
df['SATISFACTION_GLOBAl']= round(df['SATISFACTION_GLOBAl']/2)


#______________________________________________________________________________________
# App layout
app.layout = html.Div([

    html.H1("Dashboard Hackaton", style={'text-align': 'center', 'color': '#7FDBFF', 'font-size': 35}),
    html.Br(),
    


        html.Div([
            html.Div(id='container_variables'), #1
            
            dcc.Dropdown(
                id = 'lst_qst',
                options =[
                    {'label' : 'la participation à un hackathon permet de simplifier le procesus d’innovation', 'value' : 'UTILITE_INNOVATION'},
                    {'label' : 'participer à un hackathon me permet de me tenir à jour des dernières innovations', 'value' : 'INFORMATION_INNOVATION'},
                    {'label' : 'je m’informe souvent à propos des hackathons', 'value' : 'INTERET_PARTICIPANT1'},
                    {'label' : 'je m’informe souvent à propos du devenir des projets après le hackathon', 'value' : 'INTERET_PARTICIPANT2'},
                    {'label' : 'Quand je participe à un hackathon, j’éprouve souvent une sensation de bien-être', 'value' : 'SATISFACTION1'},
                    {'label' : 'Quand je participe à un hackathon, ça m’absorbe complètement', 'value' : 'SATISFACTION2'},
                    {'label' : 'participer à un hackathon, ça me donne l’occasion d’en parler ensuite avec mes proches', 'value' : 'NETWORKING1'},
                    {'label' : 'j’aime participer à un hackathon et garder contact ensuite avec les personnes que j’y ai rencontrées', 'value' : 'NETWORKING2'},
                    {'label' : 'je cherche à nouer des contacts durables durant un hackathon', 'value' : 'NETWORKING3'},
                    {'label' : 'participer à un hackathon, ça me donne l’occasion d’en parler ensuite avec mon équipe', 'value' : 'NETWORKING4'},
                    {'label' : 'j’aime bien participer à un hackathon et en parler ensuite avec d’autres participants de hackathons', 'value' : 'NETWORKING5'},
                    {'label' : 'Après avoir participé à un hackathon, j’aime bien me poser des questions importantes sur moi-même', 'value' : 'SELF_IMPROVEMENT1'},
                    {'label' : 'Globalement, je considère que participer à un projet du hackathon, ça vaut bien l’énergie que j’y consacre', 'value' : 'SATISFACTION3'},
                    {'label' : 'Globalement, je considère qu’un hackathon permet vraiment de développer de la valeur pour l’individu', 'value' : 'SELF_IMPROVEMENT2'},
                    {'label' : 'Par rapport à ce que j’en attends, je suis un peu déçu par les projets auxquels je participe', 'value' : 'SATISFACTION4'},
                    {'label' : 'Globalement, je suis vraiment satisfait des projets auxquels j’ai participés', 'value' : 'SATISFACTION5'},
                    {'label' : 'Globalement, je suis vraiment satisfait des hackathons auxquels j’ai participé', 'value' : 'SATISFACTION6'},
                    ],
                value=['SATISFACTION6'],
                multi=True
                ),
            

        ]),
        html.Br(),
        
        html.Div(id='container_sex'),       #3
        
        dcc.Checklist(                      #4
            id = 'lst_sex',
            options=[
                {'label' : "Homme", 'value' : 1},
                {'label' : 'Femme', 'value' : 0}],
            style={'color': '#7FDBFF' , 'font-size': 20},
            inputStyle={"margin-right": "5px", "margin-left": "10px"},
            value=[0,1]),
        html.Br(),
        
        html.Div(id='container_cat'),       #5

        
        dcc.Checklist(                      #6
            id = 'lst_cat',
            options=[
                {'label' : '15-20', 'value' : '15-20 ans'},
                {'label' : '21-25', 'value' : '21-25 ans'},
                {'label' : '26-30', 'value' : '26-30 ans'},
                {'label' : '31-35', 'value' : '31-35 ans'},
                {'label' : '36-40', 'value' : '36-40 ans'},
                {'label' : '41-45', 'value' : '41-45 ans'},
                {'label' : '46-50', 'value' : '46-50 ans'},
                {'label' : '51-55', 'value' : '51-55 ans'}],
            value=['15-20 ans', '21-25 ans', '26-30 ans', '31-35 ans','36-40 ans','41-45 ans', '46-50 ans','51-55 ans'],
            style={'color': '#7FDBFF' , 'font-size': 20},
            inputStyle={"margin-right": "5px", "margin-left": "10px"},
            ),
        html.Br(),

        html.Div([
            dcc.Graph(id='graph'),      #7
        html.Br(),
        
        html.Div(id='container_note'),      #8
        html.Br(),
        
        dcc.RangeSlider(0, 10,              #9
                        id = 'slider_note',
                        value=[0, 10],
                        step =1,
                tooltip={"placement": "bottom", "always_visible": True})
    ]),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row([
    html.Div(html.Hr(style={'borderWidth': "0.3vh", "width": "100%", "color": "##7FDBFF"}))
]),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(id='none',children=[],style={'display': 'none'}),
        html.Div(id='cont_sex2'), 
        dcc.Checklist(                      
            id = 'lst_sex2',
            options=[
                {'label' : "Homme", 'value' : 1},
                {'label' : 'Femme', 'value' : 0}],
            style={'color': '#7FDBFF' , 'font-size': 20},
            inputStyle={"margin-right": "5px", "margin-left": "10px"},
            value=[0,1]),
        
        html.Br(),
        html.Div(id='cont_cat2'), 
        dcc.Checklist(                      
            id = 'lst_cat2',
            options=[
                {'label' : '15-20', 'value' : '15-20 ans'},
                {'label' : '21-25', 'value' : '21-25 ans'},
                {'label' : '26-30', 'value' : '26-30 ans'},
                {'label' : '31-35', 'value' : '31-35 ans'},
                {'label' : '36-40', 'value' : '36-40 ans'},
                {'label' : '41-45', 'value' : '41-45 ans'},
                {'label' : '46-50', 'value' : '46-50 ans'},
                {'label' : '51-55', 'value' : '51-55 ans'}],
            value=['15-20 ans', '21-25 ans', '26-30 ans', '31-35 ans','36-40 ans','41-45 ans', '46-50 ans','51-55 ans'],
            style={'color': '#7FDBFF' , 'font-size': 20},
            inputStyle={"margin-right": "5px", "margin-left": "10px"},
            ),
        
        html.Br(),
        html.Div(id='cont_lieu2'), 
        dcc.Checklist(                      
            id = 'lst_lieu2',
            options=[
                {'label' : 'périphérie de Strasbourg', 'value' : 'aux alentours de Strasbourg'},
                {'label' : 'Alsace', 'value' : 'en Alsace'},
                {'label' : 'France', 'value' : 'en France'},
                {'label' : 'Strasbourg', 'value' : 'à Strasbourg'},
                {'label' : 'pays étrangers', 'value' : "à l'étranger"}],
            value=['aux alentours de Strasbourg', 'en Alsace', 'en France', "à Strasbourg","à l'étranger",'41-45 ans', '46-50 ans','51-55 ans'],
            style={'color': '#7FDBFF' , 'font-size': 20},
            inputStyle={"margin-right": "5px", "margin-left": "10px"},
            ),
        
        html.Br(),
        html.Div(id='cont_role2'), 
        dcc.Dropdown(
            id = 'lst_role',
            options =[
                {'label' : 'autre', 'value' : 'autre'},
                {'label' : 'bénévole', 'value' : 'bénévole'},
                {'label' : 'coach', 'value' : 'coach'},
                {'label' : 'consommateur', 'value' : 'consommateur'},
                {'label' : 'designer', 'value' : 'designer'},
                {'label' : 'hacker', 'value' : 'hacker'},
                {'label' : 'organisateur', 'value' : 'organisateur'},
                {'label' : 'partenaire', 'value' : 'partenaire'},
                {'label' : "professionnel de l'industrie", 'value' : "professionnel de l'industrie"},
                {'label' : 'professionnel de santé ', 'value' : 'professionnel de santé '},
                ],
            value=['organisateur', 'partenaire', "professionnel de l'industrie", 'professionnel de santé', 'autre', 'bénévole', 'coach', 'consommateur', 'designer', 'hacker'],
            multi=True
            ),
        
        
        html.Br(),
            # dcc.Graph(id='graphi')
        # html.Div(className= 'row', children=[
        #     html.H4("Moyennes"),
        #     html.Br(),
        #     px.pie(df, labels=['Femme','Homme'], values = pd.Series(df.index, index=df['GENRE']).groupby(level=0).size().tolist() 
                   
        html.Div(className= 'row', children=[
             html.Div(children=[
        #         dcc.Graph(px.pie(df, labels=['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen'], values = [4500,2500,1053,500])),
                 dcc.Graph(id="graphi", style={'display': 'inline-block'}),
                 dcc.Graph(id="grapho", style={'display': 'inline-block'}),
]),
             html.Div(children=[
                 
                 dcc.Graph(id="grapha", style={'display': 'inline-block'}),
                 dcc.Graph(id="graphe", style={'display': 'inline-block'})
                 ])
             ,])])


# dfff = df.copy()
# lst_cat2 = ['26-30 ans', '36-40 ans']
# dfff = dfff.sort_values(by='Je suis.1')
# dfff
# dfff = dfff[dfff["Je vis"].isin(lst_cat2)]
# dfff['Je suis.1'].unique().tolist()
# pd.Series(dfff.index, index=dfff['Je suis.1']).groupby(level=0).size()

print('hello')
#______________________________________________________________________________________
# variables dans les graph
@app.callback(
    [Output(component_id='container_variables', component_property='children'), #1
     Output(component_id='container_sex', component_property='children'),       #3
     Output(component_id='container_cat', component_property='children'),       #5
     Output(component_id='container_note', component_property='children'),      #8
     Output(component_id='graph', component_property='figure'),                 #7
     ],
    [Input(component_id='lst_qst', component_property='value'),                #2
     Input(component_id='lst_sex', component_property='value'),                 #4
     Input(component_id='lst_cat', component_property='value'),                 #6
     Input(component_id='slider_note', component_property='value'),             #9
     ]            
)

#def update_graph(lst_vrbl, lst_sex, lst_cat, slider_note):
def update_graph(lst_qst, lst_sex, lst_cat, slider_note):

    container = "Selectionnez les questions données aux participants" #: {}".format(lst_vrbl)
    container2 = "Selectionnez le sexe des participants" #+ str(lst_sex)
    container3 = "Selectionnez les tranches d'âge des participants"  #:{}".format(lst_cat)
    container4 = "Selectionnez l'intervalle de la note moyenne donnée par le participant" # : {}".format(lst_vrbl)

    dff = df.copy()
    dff = dff[dff["GENRE"].isin(lst_sex)]
    dff = dff[dff["AGE"].isin(lst_cat)]
    dff = dff[dff["SATISFACTION_GLOBAl"].isin(range(slider_note[0],slider_note[1]+1))]
    dff = dff.groupby(dff['SATISFACTION_GLOBAl'], as_index=False)[lst_qst].mean()
    

    fig = px.bar(dff, x ='SATISFACTION_GLOBAl', y = lst_qst,
                 barmode="group")
    fig.update_layout(
            plot_bgcolor=colors['background'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
            )


    return container, container2, container3, container4, fig

#______________________________________________________________________________________

@app.callback(
    [
    Output(component_id='cont_sex2', component_property='children'),
    Output(component_id='cont_cat2', component_property='children'),
    Output(component_id='cont_lieu2', component_property='children'),
    Output(component_id='cont_role2', component_property='children'),
    Output(component_id='graphi', component_property='figure'),
    Output(component_id='grapho', component_property='figure'),
    Output(component_id='grapha', component_property='figure'),
    Output(component_id='graphe', component_property='figure'),
    ],
    [
     Input(component_id='lst_sex2', component_property='value'),
     Input(component_id='lst_cat2', component_property='value'),
     Input(component_id='lst_lieu2', component_property='value'),
     Input(component_id='lst_role', component_property='value')
     ])




def jsplus(lst_sex2, lst_cat2, lst_lieu2, lst_role):


    dfff = df.copy()
    dfff = dfff[dfff["GENRE"].isin(lst_sex2)]
    dfff = dfff[dfff["AGE"].isin(lst_cat2)]
    dfff = dfff[dfff["Je vis"].isin(lst_lieu2)]
    dfff = dfff[dfff["Je suis.1"].isin(lst_role)]
    
    dfff = dfff.sort_values(by='GENRE')
    truci = pd.Series(dfff.index, index=dfff['GENRE']).groupby(level=0).size().tolist()
    label_truci = dfff['GENRE'].unique().tolist()
    
    cont_sex2 = "Selectionnez le sexe des participants"
    cont_cat2 = "Selectionnez les tranches d'âge des participants"
    cont_lieu2 = "Selectionnez le lieu de résidence des participants"
    cont_role2 = "Selectionnez le rôle des participants"
    
    
    
    
    figi = go.Figure(data=[go.Pie(labels=label_truci, 
                                  values = truci,
                                  hole=.4)])
    figi.update_layout(
            title_text="Répartition des genres", title_x =0.5,
            plot_bgcolor=colors['text'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
            )
    
    dfff = dfff.sort_values(by='AGE')
    truco = pd.Series(dfff.index, index=dfff['AGE']).groupby(level=0).size().tolist()
    label_truco = dfff['AGE'].unique().tolist()     
    figo = go.Figure(data=[go.Pie(labels=label_truco, 
                                  values = truco,
                                  hole=.4)])
    figo.update_layout(
            title_text="Répartition des tranches d'âge", title_x =0.5,
            plot_bgcolor=colors['text'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
            )

    dfff = dfff.sort_values(by='Je vis')
    truca = pd.Series(dfff.index, index=dfff['Je vis']).groupby(level=0).size().tolist() 
    label_truco = dfff['Je vis'].unique().tolist() 
    figa = go.Figure(data=[go.Pie(labels=label_truco, 
                                  values = truca,
                                  hole=.4)])
    figa.update_layout(
            title_text="Répartition des lieux de résidence", title_x =0.45,
            plot_bgcolor=colors['text'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
            )

    dfff = dfff.sort_values(by='Je suis.1')    
    truce = pd.Series(dfff.index, index=dfff['Je suis.1']).groupby(level=0).size().tolist()  
    label_truce = dfff['Je suis.1'].unique().tolist()
    fige = go.Figure(data=[go.Pie(labels=label_truce, 
                                  values = truce, 
                                  hole=.4)])
    fige.update_layout(
            title_text="Répartition des rôles", title_x =0.4,
            plot_bgcolor=colors['text'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
            )
     
    return  cont_sex2, cont_cat2, cont_lieu2, cont_role2, figi, figo, figa, fige


# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
