import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/slide_1", name="slide_1")

def kpi_text(pct, count):
    return html.Div([
        html.H2(f"{pct}%", style={'fontWeight': '800', 'margin': '0', 'lineHeight': '1'}),
        html.P(f"{count:,}", style={'margin': '0', 'fontSize': '13px', 'color': 'inherit', 'opacity': '0.75'}),
    ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'justifyContent': 'center', 'height': '100%'})

# ── Layout ────────────────────────────────────────────────────────────────────
layout = html.Div(
    [
# ====================================
        dbc.Row(
            dbc.Col(
                html.H1(
                    'Información general', 
                style = {'fontSize': '60px', 'fontWeight': '700'})
            , style = {'display': 'flex', 'flex': '1'})
        , style = {'display': 'flex', 'flex': '0 0 calc(10% - 8px)'}),
# ====================================
        dbc.Row(
            [
            dbc.Col(
                dbc.Card(
                    [
                    dbc.CardHeader('Transmitidas y rechazadas', style = {'textAlign': 'center'}),
                    dbc.CardBody(
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dbc.Card(style = {'flex': '0 0 calc(50% - 8px)'}, className = 'card-clean card-filled-coral'),
                                        dbc.Card(style = {'flex': '0 0 calc(50% - 8px)'}, className = 'card-clean card-filled-coral')
                                    ]
                                , style = {'display': 'flex', 'flex': '0 0 calc(40% - 8px)', 'flexDirection': 'column', 'gap': '16px'}),
                                dbc.Card(
                                    style = {'display': 'flex', 'flex': '0 0 calc(60% - 8px)'}, className = 'card-clean card-coral'
                                )
                            ]
                        , style = {'display': 'flex', 'flex': '1', 'gap': '16px'})
                    , style = {'display': 'flex', 'flex': '1'})
                    ]
                , style = {'display': 'flex', 'flex': '1'}
                , className = 'card-clean')
            , style = {'display': 'flex', 'flex': '1'}),
            dbc.Col(
                dbc.Card(
                    [
                    dbc.CardHeader('Políticas y No políticas', style = {'textAlign': 'center'}),
                    dbc.CardBody(
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dbc.Card(
                                            kpi_text(78, 583)
                                        , style = {'flex': '0 0 calc(50% - 8px)'}
                                        , className = 'card-clean card-filled-coral'),
                                        dbc.Card(
                                            kpi_text(78, 583)
                                        , style = {'flex': '0 0 calc(50% - 8px)'}
                                        , className = 'card-clean card-filled-coral')
                                    ]
                                , style = {'display': 'flex', 'flex': '0 0 calc(40% - 8px)', 'flexDirection': 'column', 'gap': '16px'}),
                                dbc.Card(
                                    style = {'display': 'flex', 'flex': '0 0 calc(60% - 8px)'}, className = 'card-clean card-coral'
                                )
                            ]
                        , style = {'display': 'flex', 'flex': '1', 'gap': '16px'})
                    , style = {'display': 'flex', 'flex': '1'})
                    ]
                , style = {'display': 'flex', 'flex': '1'}
                , className = 'card-clean')
            , style = {'display': 'flex', 'flex': '1'})
            ]
        , style = {'display': 'flex', 'flex': '0 0 calc(45% - 8px)'}),
# ====================================
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader('Transmitidas y rechazadas por mes', style = {'textAlign': 'center'}),
                        dbc.CardBody(style = {'flex': '1'})
                    ]
                , style = {'flex': '1', 'display': 'flex'}, className = 'card-clean')
            , style = {'display': 'flex', 'flex': '1'})
        , style = {'display': 'flex', 'flex': '0 0 calc(45% - 8px)'})
# ====================================
    ]
, style = {
    'height': '100vh',
    'width': '100%',
    'display': 'flex',
    'flexDirection': 'column',
    'gap': '16px',
    'padding': '25px',
    'boxSizing': 'border-box'
}    
, className = 'slide')
