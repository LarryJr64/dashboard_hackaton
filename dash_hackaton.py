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
# df = pd.read_csv("D:\Cours_2021-2022\Semestre_3\dashboard_moritz\CLAUDE_DILETTA_ROUSSEAU.csv")
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
    dcc.RadioItems(
        id = 'dropdown-to-show_or_hide-element',
        options=[
            {'label': 'Show ReadMe', 'value': 'on'},
            {'label': 'Hide ReadMe', 'value': 'off'}
        ],
        value = 'on',
        inputStyle={"margin-right": "5px", "margin-left": "10px"},
        labelStyle={'display': 'inline-block'}
    ),
    
        dcc.Textarea(
        id = 'element-to-hide',
        value = "Le cadre de notre projet se fait sur la demande de Mme CULLMANN Sabine qui souhaitait avoir une vision d???ensemble sur l?????v??nement, comprendre quels sont les acteurs des hackathons.L???id??e originale ??tait donc de pouvoir trouver le profil des participants en fonction des donn??es r??colt??es lors d?????ditions pr??c??dentes (Cat??gorie d?????ge, sexe, provenance etc.) ainsi que de comprendre leurs incitations ?? participer ?? ce processus d???innovation et de partage. (Diff??rentes questions bas??es sur la satisfaction, les incitations, leur projet, leur ??quipe etc.). Le travail demand?? ?? notre groupe ??tait d???ordre technique, il fallait rendre les donn??es utilisables et permettre ?? Mme CULLMANN d???avoir un nouvel outil pour ses recherches. La part th??orique derri??re le projet est un article fourni par madame CULLMANN expliqu?? ci-dessous. L'article 'La coconstruction de l???innovation durant un hackathon, une approche par la valeur' de In??s Guguen-Gicquel, Sabine Cullmann et Herbert Cast??ran explore l'analyse de la perception de la valeur par les participants lors des hackathons. Les donn??es viennent d'un sondage rempli par les participants des hackathons pr??c??dents et correspondent ?? un ensemble de question/reponses sur la satisfaction, les caract??ristiques et le ressenti des acteurs du hackathon. Notre analyse est d??compos??e en deux parties. (Graphique ?? barres et diagrammes circulaires). La premi??re partie permet de mesurer et de remarquer les features du hackathon/questions marqu??es comme importantes par les participants. La mesure se fait en fonction de leur satisfaction globale vis-??-vis de l'??v??nement. La seconde partie permet de comprendre les profils des participants en fonction de leurs caract??ristiques personnelles",
        style={'width': '100%', 'height': 300},
        ),
    ],
    ),
    
        html.Br(),
        html.Div([
            html.Div(id='container_variables'), #1
            
            dcc.Dropdown(
                id = 'lst_qst',
                options =[
                    {'label' : 'la participation ?? un hackathon permet de simplifier le procesus d???innovation', 'value' : 'UTILITE_INNOVATION'},
                    {'label' : 'participer ?? un hackathon me permet de me tenir ?? jour des derni??res innovations', 'value' : 'INFORMATION_INNOVATION'},
                    {'label' : 'je m???informe souvent ?? propos des hackathons', 'value' : 'INTERET_PARTICIPANT1'},
                    {'label' : 'je m???informe souvent ?? propos du devenir des projets apr??s le hackathon', 'value' : 'INTERET_PARTICIPANT2'},
                    {'label' : 'Quand je participe ?? un hackathon, j?????prouve souvent une sensation de bien-??tre', 'value' : 'SATISFACTION1'},
                    {'label' : 'Quand je participe ?? un hackathon, ??a m???absorbe compl??tement', 'value' : 'SATISFACTION2'},
                    {'label' : 'participer ?? un hackathon, ??a me donne l???occasion d???en parler ensuite avec mes proches', 'value' : 'NETWORKING1'},
                    {'label' : 'j???aime participer ?? un hackathon et garder contact ensuite avec les personnes que j???y ai rencontr??es', 'value' : 'NETWORKING2'},
                    {'label' : 'je cherche ?? nouer des contacts durables durant un hackathon', 'value' : 'NETWORKING3'},
                    {'label' : 'participer ?? un hackathon, ??a me donne l???occasion d???en parler ensuite avec mon ??quipe', 'value' : 'NETWORKING4'},
                    {'label' : 'j???aime bien participer ?? un hackathon et en parler ensuite avec d???autres participants de hackathons', 'value' : 'NETWORKING5'},
                    {'label' : 'Apr??s avoir particip?? ?? un hackathon, j???aime bien me poser des questions importantes sur moi-m??me', 'value' : 'SELF_IMPROVEMENT1'},
                    {'label' : 'Globalement, je consid??re que participer ?? un projet du hackathon, ??a vaut bien l?????nergie que j???y consacre', 'value' : 'SATISFACTION3'},
                    {'label' : 'Globalement, je consid??re qu???un hackathon permet vraiment de d??velopper de la valeur pour l???individu', 'value' : 'SELF_IMPROVEMENT2'},
                    {'label' : 'Par rapport ?? ce que j???en attends, je suis un peu d????u par les projets auxquels je participe', 'value' : 'SATISFACTION4'},
                    {'label' : 'Globalement, je suis vraiment satisfait des projets auxquels j???ai particip??s', 'value' : 'SATISFACTION5'},
                    {'label' : 'Globalement, je suis vraiment satisfait des hackathons auxquels j???ai particip??', 'value' : 'SATISFACTION6'},
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
                {'label' : 'p??riph??rie de Strasbourg', 'value' : 'aux alentours de Strasbourg'},
                {'label' : 'Alsace', 'value' : 'en Alsace'},
                {'label' : 'France', 'value' : 'en France'},
                {'label' : 'Strasbourg', 'value' : '?? Strasbourg'},
                {'label' : 'pays ??trangers', 'value' : "?? l'??tranger"}],
            value=['aux alentours de Strasbourg', 'en Alsace', 'en France', "?? Strasbourg","?? l'??tranger",'41-45 ans', '46-50 ans','51-55 ans'],
            style={'color': '#7FDBFF' , 'font-size': 20},
            inputStyle={"margin-right": "5px", "margin-left": "10px"},
            ),
        
        html.Br(),
        html.Div(id='cont_role2'), 
        dcc.Dropdown(
            id = 'lst_role',
            options =[
                {'label' : 'autre', 'value' : 'autre'},
                {'label' : 'b??n??vole', 'value' : 'b??n??vole'},
                {'label' : 'coach', 'value' : 'coach'},
                {'label' : 'consommateur', 'value' : 'consommateur'},
                {'label' : 'designer', 'value' : 'designer'},
                {'label' : 'hacker', 'value' : 'hacker'},
                {'label' : 'organisateur', 'value' : 'organisateur'},
                {'label' : 'partenaire', 'value' : 'partenaire'},
                {'label' : "professionnel de l'industrie", 'value' : "professionnel de l'industrie"},
                {'label' : 'professionnel de sant?? ', 'value' : 'professionnel de sant??'},
                ],
            value=['organisateur', 'partenaire', "professionnel de l'industrie", 'professionnel de sant??', 'autre', 'b??n??vole', 'coach', 'consommateur', 'designer', 'hacker'],
            multi=True
            ),
        
        html.Br(),
                   
        html.Div(className= 'row', children=[
             html.Div(children=[
                 dcc.Graph(id="graphi", style={'display': 'inline-block'}),
                 dcc.Graph(id="grapho", style={'display': 'inline-block'}),
]),
             html.Div(children=[
                 
                 dcc.Graph(id="grapha", style={'display': 'inline-block'}),
                 dcc.Graph(id="graphe", style={'display': 'inline-block'})
                 ])
             ,])])


#______________________________________________________________________________________


@app.callback(
   Output(component_id='element-to-hide', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])


def show_hide_element(visibility_state):
    if visibility_state == 'on':
        return {'width': '100%', 'height': 300}
    if visibility_state == 'off':
        return {'display': 'none'}


#______________________________________________________________________________________


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


def update_graph(lst_qst, lst_sex, lst_cat, slider_note):

    container = "Selectionnez les questions donn??es aux participants" 
    container2 = "Selectionnez le sexe des participants"
    container3 = "Selectionnez les tranches d'??ge des participants"  
    container4 = "Selectionnez l'intervalle de la note moyenne donn??e par le participant" 

    dff = df.copy()
    dff = dff[dff["GENRE"].isin(lst_sex)]
    dff = dff[dff["AGE"].isin(lst_cat)]
    dff = dff[dff["SATISFACTION_GLOBAl"].isin(range(slider_note[0],slider_note[1]+1))]
    dff = dff.groupby(dff['SATISFACTION_GLOBAl'], as_index=False)[lst_qst].mean()
    

    fig = px.bar(dff, x ='SATISFACTION_GLOBAl', y = lst_qst,
                 labels={
                     'SATISFACTION_GLOBAl': 'Note moyenne du hackaton donn??e par le participant',
                     'value':'Moyenne des questions',
                     'variable' : 'Questions choisies'},
                 barmode="group")
    fig.update_layout(
            title_text="Notes moyennes des questions en fonction de la satifaction globale des participants", title_x =0.45,
            title_font=dict(size=18),
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
    cont_cat2 = "Selectionnez les tranches d'??ge des participants"
    cont_lieu2 = "Selectionnez le lieu de r??sidence des participants"
    cont_role2 = "Selectionnez le r??le des participants"
    
    
    
    
    figi = go.Figure(data=[go.Pie(labels=label_truci, 
                                  values = truci,
                                  hole=.4)])
    figi.update_layout(
            title_text="R??partition des genres", title_x =0.5,
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
            title_text="R??partition des tranches d'??ge", title_x =0.5,
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
            title_text="R??partition des lieux de r??sidence", title_x =0.45,
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
            title_text="R??partition des r??les", title_x =0.4,
            plot_bgcolor=colors['text'],
            paper_bgcolor=colors['background'],
            font_color=colors['text']
            )
     
    return  cont_sex2, cont_cat2, cont_lieu2, cont_role2, figi, figo, figa, fige


# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
