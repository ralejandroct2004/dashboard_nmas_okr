import dash
from dash import html, dcc

dash.register_page(__name__, path="/", name="home")

layout = html.Div(
    [
        # Logo como fondo — grande, centrado, muy sutil
        html.Img(
            src='/assets/nmas_logo.png',
            style={
                'position': 'absolute',
                'top': '50%', 'left': '50%',
                'transform': 'translate(-50%, -50%)',
                'width': '75%', 'maxWidth': '900px',
                'filter': 'brightness(0) invert(1)',
                'opacity': '0.06',
                'pointerEvents': 'none',
                'zIndex': '0',
                'objectFit': 'contain'
            }
        ),

        # Capa gradiente sobre el fondo
        html.Div(style={
            'position': 'absolute', 'inset': '0',
            'background': (
                'radial-gradient(ellipse at 70% 20%, rgba(144,26,114,0.35) 0%, transparent 55%),'
                'radial-gradient(ellipse at 20% 80%, rgba(200,134,26,0.20) 0%, transparent 50%),'
                'radial-gradient(ellipse at 50% 50%, rgba(106,21,138,0.15) 0%, transparent 70%)'
            ),
            'pointerEvents': 'none',
            'zIndex': '0'
        }),

        # Contenido central
        html.Div(
            [
                # Logo pequeño arriba (visible)
                html.Img(
                    src='/assets/nmas_logo.png',
                    style={
                        'height': '56px', 'objectFit': 'contain',
                        'filter': 'brightness(0) invert(1)',
                        'opacity': '0.90', 'marginBottom': '32px'
                    }
                ),

                # Línea degradada
                html.Div(style={
                    'height': '3px', 'width': '56px',
                    'background': 'var(--gradient-brand)',
                    'borderRadius': '2px', 'marginBottom': '32px'
                }),

                # Título
                html.H1(
                    "Dashboard OKR",
                    style={
                        'fontSize': '72px', 'fontWeight': '800',
                        'color': '#ffffff', 'margin': '0 0 14px 0',
                        'letterSpacing': '-0.03em', 'lineHeight': '1'
                    }
                ),

                # Subtítulo
                html.P(
                    "Monitor de indicadores de desempeño · 2026",
                    style={
                        'fontSize': '12px', 'fontWeight': '600',
                        'color': 'rgba(255,255,255,0.45)',
                        'margin': '0 0 52px 0',
                        'letterSpacing': '0.16em',
                        'textTransform': 'uppercase'
                    }
                ),

                # CTA
                dcc.Link(
                    html.Div(
                        [
                            html.Span("Ingresar al dashboard"),
                            html.Span("→", className="arrow")
                        ],
                        style={'display': 'flex', 'alignItems': 'center', 'gap': '10px'}
                    ),
                    href="/informacion_general",
                    className="home-cta"
                ),

                # Hint
                html.P(
                    "Información general · Formatos · Programas",
                    style={
                        'fontSize': '11px', 'fontWeight': '500',
                        'color': 'rgba(255,255,255,0.18)',
                        'marginTop': '48px', 'letterSpacing': '0.10em',
                        'textTransform': 'uppercase'
                    }
                ),
            ],
            style={
                'display': 'flex', 'flexDirection': 'column',
                'alignItems': 'center', 'textAlign': 'center',
                'position': 'relative', 'zIndex': '1',
                'padding': '0 24px'
            }
        )
    ],
    style={
        'minHeight': '100vh',
        'backgroundColor': 'var(--header-bg)',
        'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center',
        'position': 'relative', 'overflow': 'hidden',
        'fontFamily': "'Montserrat', sans-serif"
    }
)
