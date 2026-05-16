import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from pages.get_figures import *
from pages.get_data import *

dash.register_page(__name__, path="/informacion_general", name="info_general")

def kpi_text(pct, count):
    return html.Div([
        html.H2(f"{pct}%", style={'fontWeight': '800', 'margin': '0', 'lineHeight': '1'}),
        html.P(f"{count:,}", style={'margin': '0', 'fontSize': '13px', 'color': 'inherit', 'opacity': '0.75'}),
    ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'justifyContent': 'center', 'height': '100%'})

df_m, df_t = get_months_and_quarters_with_data()
df_t_nt_mes = get_transmitidas_y_rechazadas_por_mes()
fig_t_nt_mes = fig_transmitidas_y_rechazadas_por_mes(df_t_nt_mes)

# ── Layout ────────────────────────────────────────────────────────────────────
layout = html.Div(
    [
# ====================================
        dbc.Row(
            dbc.Col(
                html.H1(
                    'Información general', 
                style = {'fontSize': '65px', 'fontWeight': '700'})
            , style = {'display': 'flex', 'flex': '1'})
        , style = {'display': 'flex', 'height': '100px', 'paddingBottom': '110px'}),
# ====================================
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        'Transmitidas y No transmitidas'
                    , style = {'padding': '0', 'flex': '1', 'display': 'flex', 'textAlign': 'center', 'alignItems': 'center', 'justifyContent': 'center', 'fontSize': '20px', 'fontWeight': '800'})
                , style = {'flex': '1', 'display': 'flex'}
                , className = 'card-filled-coral')
            , style = {'display': 'flex', 'flex': '1'})
        , style = {'height': '75px', 'display': 'flex', 'flexDirection': 'column'}),
# ====================================
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.Div(id = 'transmitidas_y_no_transmitidas_plot_title'), style = {'textAlign': 'center'}),
                            dcc.Graph(
                                id = 'transmitidas_y_no_transmitidas_plot',
                                figure = get_empty_fig(),
                                config = {'responsive': True, 'displayModeBar': False},
                                style = {'height': '100%', 'weight': '100%'}
                            )
                        ]
                    , style = {'flex': '1'}, className = 'card-clean card-coral fade-in')
                , style = {'display': 'flex', 'flex': '1', 'height': '400px'}),
                dbc.Col(
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Label(html.Div('Seleccione tipo de filtro'), style = {'textAlign': 'center'}),
                                            dbc.Card(
                                                dcc.Dropdown(
                                                    id = 'transmitidas_y_no_transmitidas_dd_type',
                                                    options = [
                                                        {'label': 'Histórico', 'value': 'historico'},
                                                        {'label': 'Mensual', 'value': 'mes'},
                                                        {'label': 'Trimestral', 'value': 'trimestre'}
                                                    ],
                                                    value = 'historico',
                                                    clearable = False,
                                                    placeholder = 'Seleccione tipo'
                                                , style = {'flex': '1'}
                                                , className = 'dropdown-brand')
                                            , style = {'flex': '1', 'padding': '3px'}
                                            , className = 'card-filled-fuchsia'),
                                        ]
                                    , style = {'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'gap': '5px'}),
                                    html.Div(
                                        [
                                            html.Label(html.Div('Seleccione valor'), style = {'textAlign': 'center'}),
                                            dbc.Card(
                                                dcc.Dropdown(
                                                    id = 'transmitidas_y_no_transmitidas_dd_value',
                                                    options = [],
                                                    value = None,
                                                    clearable = False,
                                                    placeholder = 'Seleccione valor'
                                                , style = {'flex': '1'}
                                                , className = 'dropdown-brand')
                                            , style = {'flex': '1', 'padding': '3px'}
                                            , className = 'card-filled-fuchsia'),
                                        ]
                                    , style = {'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'gap': '5px'}),
                                ]
                            , style = {'flex': '0 0 calc(20% - 8px)', 'display': 'flex', 'gap': '16px'}),
                            dbc.Card(style = {'flex': '0 0 calc(80% - 8px)'}, className = 'card-invisible')
                        ]
                    , style = {'display': 'flex', 'flex': '1', 'flexDirection': 'column', 'gap': '16px'})
                , style = {'display': 'flex', 'flex': '1', 'height': '400px'})
            ]
        , style = {'display': 'flex', 'flex': '1'}),
# ====================================
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        'Políticas y no políticas'
                    , style = {'padding': '0', 'flex': '1', 'display': 'flex', 'textAlign': 'center', 'alignItems': 'center', 'justifyContent': 'center', 'fontSize': '20px', 'fontWeight': '800'})
                , style = {'flex': '1', 'display': 'flex'}
                , className = 'card-filled-coral')
            , style = {'display': 'flex', 'flex': '1'})
        , style = {'height': '75px', 'display': 'flex', 'flexDirection': 'column'}),
# ====================================
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.Div(id = 'politicas_y_no_politicas_plot_title'), style = {'textAlign': 'center'}),
                            dcc.Graph(
                                id = 'politicas_y_no_politicas_plot',
                                figure = get_empty_fig(),
                                config = {'responsive': True, 'displayModeBar': False},
                                style = {'height': '100%', 'weight': '100%'},
                            )
                        ]
                    , style = {'flex': '1'}, className = 'card-clean card-coral fade-in')
                , style = {'display': 'flex', 'flex': '1', 'height': '400px'}),
                dbc.Col(
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Label(html.Div('Seleccione tipo de filtro'), style = {'textAlign': 'center'}),
                                            dbc.Card(
                                                dcc.Dropdown(
                                                    id = 'politicas_y_no_politicas_dd_type',
                                                    options = [
                                                        {'label': 'Histórico', 'value': 'historico'},
                                                        {'label': 'Mensual', 'value': 'mes'},
                                                        {'label': 'Trimestral', 'value': 'trimestre'}
                                                    ],
                                                    value = 'historico',
                                                    clearable = False,
                                                    placeholder = 'Seleccione tipo'
                                                , style = {'flex': '1'}
                                                , className = 'dropdown-brand')
                                            , style = {'flex': '1', 'padding': '3px'}
                                            , className = 'card-filled-fuchsia'),
                                        ]
                                    , style = {'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'gap': '5px'}),
                                    html.Div(
                                        [
                                            html.Label(html.Div('Seleccione valor'), style = {'textAlign': 'center'}),
                                            dbc.Card(
                                                dcc.Dropdown(
                                                    id = 'politicas_y_no_politicas_dd_value',
                                                    options = [],
                                                    value = None,
                                                    clearable = False,
                                                    placeholder = 'Seleccione valor'
                                                , style = {'flex': '1'}
                                                , className = 'dropdown-brand')
                                            , style = {'flex': '1', 'padding': '3px'}
                                            , className = 'card-filled-fuchsia'),
                                        ]
                                    , style = {'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'gap': '5px'}),
                                ]
                            , style = {'flex': '0 0 calc(20% - 8px)', 'display': 'flex', 'gap': '16px'}),
                            dbc.Card(style = {'flex': '0 0 calc(80% - 8px)'}, className = 'card-invisible')
                        ]
                    , style = {'display': 'flex', 'flex': '1', 'flexDirection': 'column', 'gap': '16px'})
                , style = {'display': 'flex', 'flex': '1', 'height': '400px'})
            ]
        , style = {'display': 'flex', 'flex': '1'}),
# ====================================
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(html.Div('Transmitidas y rechazadas por mes'), style = {'textAlign': 'center'}),
                        dcc.Graph(
                            id = 'transmitidas_y_no_transmitidas_meses_plot',
                            figure = fig_t_nt_mes,
                            config = {'displayModeBar': False, 'responsive': True},
                            style = {'height': '100%', 'weight': '100%'}
                        )
                    ]
                , style = {'flex': '1'}
                , className = 'card-clean card-coral fade-in')
            , style = {'display': 'flex', 'flex': '1', 'height': '600px'})
        , style = {'display': 'flex', 'flex': '1'})
# ====================================
    ]
    , style = {
        'width': '100vw',
        'display': 'flex',
        'flexDirection': 'column',
        'gap': '16px',
        'padding': '25px',
        'boxSizing': 'border-box'
    }    
)

# ====================================

@dash.callback(
    Output('transmitidas_y_no_transmitidas_dd_value', 'options'),
    Output('transmitidas_y_no_transmitidas_dd_value', 'value'),
    Input('transmitidas_y_no_transmitidas_dd_type', 'value')
)
def update_transmitidas_y_no_transmitidas_dd(type_):
    global df_m, df_t
    if type_ == 'historico':
        return [], None
    
    elif type_ == 'mes':
        return [{'label': mes, 'value': i+1} for i, mes in enumerate([
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]) if i + 1 in df_m['mes'].tolist()], 1
    
    elif type_ == 'trimestre':
        return [
            {'label': f'Trimestre {i}', 'value': i} for i in range(1, 5)
        if i in df_t['trimestre'].tolist()], 1
    
# ====================================

@dash.callback(
    Output('politicas_y_no_politicas_dd_value', 'options'),
    Output('politicas_y_no_politicas_dd_value', 'value'),
    Input('politicas_y_no_politicas_dd_type', 'value')
)
def update_politicas_y_no_politicas_dd(type_):
    global df_t, df_m

    if type_ == 'historico':
        return [], None
    
    elif type_ == 'mes':
        return [{'label': mes, 'value': i+1} for i, mes in enumerate([
            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
        ]) if i + 1 in df_m['mes'].tolist()], 1
    
    elif type_ == 'trimestre':
        return [
            {'label': f'Trimestre {i}', 'value': i} for i in range(1, 5)
        if i in df_t['trimestre'].tolist()], 1
    
# ====================================

@dash.callback(
    Output('transmitidas_y_no_transmitidas_plot', 'figure'),
    Output('transmitidas_y_no_transmitidas_plot_title', 'children'),
    Input('transmitidas_y_no_transmitidas_dd_type', 'value'),
    Input('transmitidas_y_no_transmitidas_dd_value', 'value'),
    Input('transmitidas_y_no_transmitidas_dd_value', 'options'),
)
def update_transmitidas_y_no_transmitidas_plot(type_, value, value_options):
    df = get_transmitidas_y_rechazadas(type_, value)
    fig = fig_transmitidas_y_no_transmitidas(df)

    return (
        fig, 
        f"Transmitidas y no transmitidas ({next((op['label'] for op in value_options if op['value'] == value), 'Histórico')})"
    )

# ====================================

@dash.callback(
    Output('politicas_y_no_politicas_plot', 'figure'),
    Output('politicas_y_no_politicas_plot_title', 'children'),
    Input('politicas_y_no_politicas_dd_type', 'value'),
    Input('politicas_y_no_politicas_dd_value', 'value'),
    Input('politicas_y_no_politicas_dd_value', 'options'),
)
def update_politicas_y_no_politicas_plot(type_, value, value_options):
    df = get_politicas_y_no_politicas(type_, value)
    fig = fig_politicas_y_no_politicas(df)

    return (
        fig,
        f"Políticas y no políticas ({next((op['label'] for op in value_options if op['value'] == value), 'Histórico')})"
    )

# ====================================