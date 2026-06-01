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

df_semanas = get_ultimas_5_semanas()

# ── Layout ────────────────────────────────────────────────────────────────────
layout = html.Div(
    [
# ====================================
        html.Header(
            [
                html.Img(
                    src='/assets/nmas_logo.png',
                    style={'height': '44px', 'objectFit': 'contain'}
                ),
                html.Div([
                    html.H1("Dashboard OKR", className="header-title"),
                    html.P("Monitor de indicadores OKR", className="header-subtitle"),
                ], style={'paddingTop': '15px'}),
            ],
            className="dashboard-header",
            style={'margin': '-25px -25px 0 -25px'}
        ),
# ====================================
        dbc.Row(
            dbc.Col(
                html.Div([
                    html.P(
                        "OKR — 2026",
                        style={
                            'fontSize': '12px', 'fontWeight': '600', 'letterSpacing': '0.18em',
                            'textTransform': 'uppercase', 'color': 'var(--fuchsia)',
                            'margin': '0 0 6px 0'
                        }
                    ),
                    html.H1(
                        'Información general',
                        style={
                            'fontSize': '52px', 'fontWeight': '800', 'margin': '0',
                            'lineHeight': '1.1', 'color': 'var(--text-primary)',
                            'letterSpacing': '-0.02em'
                        }
                    ),
                    html.Div(style={
                        'height': '4px', 'width': '160px', 'marginTop': '12px',
                        'background': 'var(--gradient-brand)', 'borderRadius': '2px'
                    })
                ])
            , style = {'display': 'flex', 'flex': '1'})
        , style = {'display': 'flex', 'height': '120px', 'paddingBottom': '90px'}),
# ====================================
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        'Transmitidas y No transmitidas'
                    , style = {'padding': '0', 'flex': '1', 'display': 'flex', 'textAlign': 'center', 'alignItems': 'center', 'justifyContent': 'center', 'fontSize': '15px', 'fontWeight': '800'})
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
                            dbc.Card(
                                html.Div(id='desc_transmitidas', style={'padding': '18px'}),
                                style={'flex': '0 0 calc(80% - 8px)'},
                                className='card-invisible'
                            )
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
                    , style = {'padding': '0', 'flex': '1', 'display': 'flex', 'textAlign': 'center', 'alignItems': 'center', 'justifyContent': 'center', 'fontSize': '15px', 'fontWeight': '800'})
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
                            dbc.Card(
                                html.Div(id='desc_politicas', style={'padding': '18px'}),
                                style={'flex': '0 0 calc(80% - 8px)'},
                                className='card-invisible'
                            )
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
        , style = {'display': 'flex', 'flex': '1'}),
# ====================================
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        'Formatos y programas'
                    , style = {'padding': '0', 'flex': '1', 'display': 'flex', 'textAlign': 'center', 'alignItems': 'center', 'justifyContent': 'center', 'fontSize': '15px', 'fontWeight': '800'})
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
                            dbc.CardHeader(html.Div('Peticiones por programa'), style = {'textAlign': 'center'}),
                            dcc.Graph(
                                id = 'peticiones_por_programa_plot',
                                figure = get_empty_fig(),
                                config = {'responsive': True, 'displayModeBar': False},
                                style = {'height': '100%', 'weight': '100%'},
                            )
                        ]
                    , style = {'flex': '1'}
                    , className = 'card-clean card-coral fade-in')
                , style = {'display': 'flex', 'flex': '1', 'height': '600px'}),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.Div('Formato de peticiones'), style = {'textAlign': 'center'}),
                            dcc.Graph(
                                id = 'formato_de_peticiones_plot',
                                figure = get_empty_fig(),
                                config = {'responsive': True, 'displayModeBar': False},
                                style = {'height': '100%', 'weight': '100%'},
                            )
                        ]
                    , style = {'flex': '1'}
                    , className = 'card-clean card-coral fade-in')
                , style = {'display': 'flex', 'flex': '1', 'height': '600px'}),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Label(html.Div('Seleccione semana'), style = {'textAlign': 'center'}),
                                dbc.Card(
                                    dcc.Dropdown(
                                        id = 'formatos_y_programas_dd',
                                        options = [
                                            {'label': f'Semana {s}', 'value': s}
                                        for s in df_semanas['semana']],
                                        value = None,
                                        clearable = False,
                                        placeholder = 'Seleccione valor'
                                    , style = {'flex': '1'}
                                    , className = 'dropdown-brand')
                                , style = {'flex': '1', 'padding': '3px'}
                                , className = 'card-filled-fuchsia'),
                            ]
                        , style = {'flex': '0 0 calc(10% - 8px)', 'display': 'flex', 'flexDirection': 'column', 'gap': '5px'}),
                        dbc.Card(
                            html.Div(id='desc_formatos_programas', style={'padding': '18px'}),
                            style={'flex': '0 0 calc(90% - 8px)'},
                            className='card-invisible'
                        )
                    ]
                , style = {'display': 'flex', 'flex': '1', 'flexDirection': 'column','height': '600px', 'gap': '16px'})
            ]
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

@dash.callback(
    Output('formato_de_peticiones_plot', 'figure'),
    Output('peticiones_por_programa_plot', 'figure'),
    Input('formatos_y_programas_dd', 'value')
)
def update_formatos_y_programa_plot(semana):
    df1 = get_peticiones_por_programa(semana)
    fig1 = fig_peticiones_por_programa(df1)

    df2 = get_formato_de_peticiones(semana)
    fig2 = fig_formato_de_peticiones(df2)

    return fig1, fig2

# ====================================

def _span(text, color='var(--fuchsia)', bold=True):
    return html.Span(text, style={'fontWeight': '700' if bold else '400', 'color': color})

@dash.callback(
    Output('desc_transmitidas', 'children'),
    Input('transmitidas_y_no_transmitidas_dd_type', 'value'),
    Input('transmitidas_y_no_transmitidas_dd_value', 'value'),
    Input('transmitidas_y_no_transmitidas_dd_value', 'options'),
)
def update_desc_transmitidas(type_, value, options):
    label = next((op['label'] for op in options if op['value'] == value), 'Histórico')
    periodo = _span(label)

    df = get_transmitidas_y_rechazadas(type_, value)
    transmitidas = int(df['transmitidas'].sum())
    no_transmitidas = int(df['no_transmitidas'].sum())
    total = transmitidas + no_transmitidas

    if type_ == 'historico':
        texto = [
            "En esta gráfica se muestra la distribución ", _span("histórica"), " de todas las peticiones registradas. "
            "Se observa la proporción entre notas ", _span("transmitidas", 'var(--purple)'), " al aire "
            "y notas ", _span("no transmitidas", 'var(--coral)'), " acumuladas en todo el período."
        ]
    else:
        texto = [
            "En esta gráfica se muestran las peticiones de ", periodo, ". "
            "Se observa la proporción entre notas ", _span("transmitidas", 'var(--purple)'), " al aire "
            "y notas ", _span("no transmitidas", 'var(--coral)'), " durante ese período."
        ]

    bullets = html.Ul([
        html.Li([_span("Transmitidas: ", 'var(--purple)'), f"{transmitidas:,}"], style={'marginBottom': '4px'}),
        html.Li([_span("No transmitidas: ", 'var(--coral)'), f"{no_transmitidas:,}"], style={'marginBottom': '4px'}),
        html.Li([_span("Total: ", 'var(--fuchsia)'), f"{total:,}"]),
    ], style={'fontSize': '15px', 'lineHeight': '1.9', 'color': 'var(--text-secondary)', 'marginTop': '12px', 'paddingLeft': '18px'})

    return html.Div([
        html.P(texto, style={'fontSize': '15px', 'lineHeight': '1.9', 'color': 'var(--text-secondary)', 'marginBottom': '0'}),
        bullets
    ])

# ====================================

@dash.callback(
    Output('desc_politicas', 'children'),
    Input('politicas_y_no_politicas_dd_type', 'value'),
    Input('politicas_y_no_politicas_dd_value', 'value'),
    Input('politicas_y_no_politicas_dd_value', 'options'),
)
def update_desc_politicas(type_, value, options):
    label = next((op['label'] for op in options if op['value'] == value), 'Histórico')
    periodo = _span(label)

    df = get_politicas_y_no_politicas(type_, value)
    politicas = int(df['politicas'].sum())
    no_politicas = int(df['no_politicas'].sum())
    total = politicas + no_politicas

    if type_ == 'historico':
        texto = [
            "En esta gráfica se muestra la clasificación editorial ", _span("histórica"), " de todas las peticiones. "
            "Se observa la proporción entre notas de ", _span("contenido político", 'var(--purple)'),
            " y notas ", _span("no políticas", 'var(--coral)'), " acumuladas en todo el período."
        ]
    else:
        texto = [
            "En esta gráfica se muestra la clasificación editorial de ", periodo, ". "
            "Se observa la proporción entre notas de ", _span("contenido político", 'var(--purple)'),
            " y notas ", _span("no políticas", 'var(--coral)'), " durante ese período."
        ]

    bullets = html.Ul([
        html.Li([_span("Políticas: ", 'var(--purple)'), f"{politicas:,}"], style={'marginBottom': '4px'}),
        html.Li([_span("No políticas: ", 'var(--coral)'), f"{no_politicas:,}"], style={'marginBottom': '4px'}),
        html.Li([_span("Total: ", 'var(--fuchsia)'), f"{total:,}"]),
    ], style={'fontSize': '15px', 'lineHeight': '1.9', 'color': 'var(--text-secondary)', 'marginTop': '12px', 'paddingLeft': '18px'})

    return html.Div([
        html.P(texto, style={'fontSize': '15px', 'lineHeight': '1.9', 'color': 'var(--text-secondary)', 'marginBottom': '0'}),
        bullets
    ])

# ====================================

@dash.callback(
    Output('desc_formatos_programas', 'children'),
    Input('formatos_y_programas_dd', 'value'),
)
def update_desc_formatos_programas(semana):
    if semana is None:
        return html.P("Selecciona una semana para ver el análisis.", style={'fontSize': '15px', 'color': 'var(--text-muted)'})

    semana_span = _span(f"semana {semana}")

    df_prog = get_peticiones_por_programa(semana).sort_values('peticiones', ascending=False)
    df_fmt  = get_formato_de_peticiones(semana).sort_values('peticiones', ascending=False)

    def top_items(df, col, n=3):
        items = []
        for _, row in df.head(n).iterrows():
            items.append(html.Li([
                _span(str(row[col]), 'var(--purple)'),
                f": {int(row['peticiones']):,} peticiones ({int(row['transmitidas']):,} transmitidas)"
            ], style={'marginBottom': '4px'}))
        return items

    estilo_p  = {'fontSize': '15px', 'lineHeight': '1.9', 'color': 'var(--text-secondary)', 'marginBottom': '4px'}
    estilo_ul = {'fontSize': '15px', 'lineHeight': '1.9', 'color': 'var(--text-secondary)', 'marginBottom': '18px', 'paddingLeft': '18px'}

    return html.Div([
        html.P(_span("Peticiones por programa"), style={'fontSize': '14px', 'marginBottom': '6px'}),
        html.P(
            ["Conteos de la ", semana_span, " ordenados de mayor a menor con transmitidas por programa:"],
            style=estilo_p
        ),
        html.Ul(top_items(df_prog, 'programa'), style=estilo_ul),

        html.P(_span("Formato de peticiones"), style={'fontSize': '14px', 'marginBottom': '6px'}),
        html.P(
            ["Conteos de la ", semana_span, " ordenados de mayor a menor con transmitidas por formato:"],
            style=estilo_p
        ),
        html.Ul(top_items(df_fmt, 'formato'), style={**estilo_ul, 'marginBottom': '0'}),
    ])