import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# ====================================

def get_empty_fig():
    fig = go.Figure()

    fig.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin = dict(t = 5, b = 5, r = 5, l = 5)
    )

    return fig

# ====================================

def fig_transmitidas_y_no_transmitidas(df):
    fig = go.Figure()

    df = df[['transmitidas', 'no_transmitidas']]
    total = df.iloc[0].sum()

    fig.add_trace(
        go.Pie(
            labels=list(df.columns),
            values=list(df.iloc[0].values),
            hole=0.45,
            hovertemplate='<b>%{label}</b><br>Cantidad: %{value}<br>Porcentaje: %{percent}<extra></extra>',
            texttemplate='<b>%{label}</b><br>%{value} (%{percent})',
            textposition='outside',
            marker=dict(
                colors=['#e24b4a', '#185fa5'],
                line=dict(color='white', width=2)
            ),
            pull=[0.03] * 2
        )
    )
    fig.update_layout(
        annotations=[dict(
            text=f'<b>Total</b><br>{total:,}',
            x=0.5, y=0.5,
            font=dict(size=16),
            showarrow=False
        )],
        showlegend=True,
        legend=dict(orientation='v', x=1.05, y=0.5),
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin = dict(t = 5, b = 5, r = 5, l = 5)
    )

    return fig

# ====================================

def fig_politicas_y_no_politicas(df):
    fig = go.Figure()

    df = df[['politicas', 'no_politicas']]
    total = df.iloc[0].sum()

    fig.add_trace(
        go.Pie(
            labels=list(df.columns),
            values=list(df.iloc[0].values),
            hole=0.45,
            hovertemplate='<b>%{label}</b><br>Cantidad: %{value}<br>Porcentaje: %{percent}<extra></extra>',
            texttemplate='<b>%{label}</b><br>%{value} (%{percent})',
            textposition='outside',
            marker=dict(
                colors=['#e24b4a', '#185fa5'],
                line=dict(color='white', width=2)
            ),
            pull=[0.03] * 2
        )
    )
    fig.update_layout(
        annotations=[dict(
            text=f'<b>Total</b><br>{total:,}',
            x=0.5, y=0.5,
            font=dict(size=16),
            showarrow=False
        )],
        showlegend=True,
        legend=dict(orientation='v', x=1.05, y=0.5),
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin = dict(t = 5, b = 5, r = 5, l = 5)
    )

    return fig

def fig_transmitidas_y_rechazadas_por_mes(df):
    df_add = pd.DataFrame([{'mes': m, 'transmitidas': 0, 'rechazadas': 0} for m in range(df['mes'].max() + 1, 13)])
    df = pd.concat([df, df_add]).reset_index(drop=True)

    meses_encode = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }

    fig = make_subplots(rows=2, cols=6, subplot_titles = [meses_encode[i] for i in range(1, 13)], vertical_spacing=0.15)
    for i, row in df.iterrows():
        row_i = i // 6 + 1
        col_i = i % 6 + 1
        total = row['transmitidas'] + row['rechazadas']

        fig.update_yaxes(range=[0, df['transmitidas'].max() * 1.2], row=row_i, col=col_i)
        fig.add_trace(
            go.Bar(
                x = ['Transmitidas', 'Rechazadas'],
                y = list(row[['transmitidas', 'rechazadas']]),
                name = meses_encode[i + 1],
                text=[
                    f"{int(row['transmitidas'])} ({row['transmitidas']/total:.1%})" if total > 0 else '0',
                    f"{int(row['rechazadas'])} ({row['rechazadas']/total:.1%})" if total > 0 else '0',
                ],
                textposition='outside',
                textfont=dict(color='black')
            ),
            row = row_i, col = col_i
        )

    fig.update_layout(
        showlegend=True,
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin = dict(t = 35, b = 5, r = 5, l = 5)
    )
    
    return fig