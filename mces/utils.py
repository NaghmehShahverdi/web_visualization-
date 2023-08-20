import base64
import plotly.express as px
import base64
import pandas as pd
from io import BytesIO
from plotly.offline import plot


def generate_graph1(filtered_genes):

    df = pd.DataFrame.from_records(filtered_genes)
    fig = px.scatter(df, x='cluster', y='name', color='spe_rank',
                     color_continuous_scale='viridis', title='Specificity Heatmap by -log(p-value) Across Clusters')

    fig.update_layout(
        width=1200,
        height=3000,
        paper_bgcolor="#fff"

    )

    plot_div = plot(fig, output_type='div', include_plotlyjs=True)

    return plot_div


# ---------------------------------------------------------------------------------------------------


def generate_graph2(filtered_genes):
    df = pd.DataFrame.from_records(filtered_genes)
    df['spe_rank'] = df['spe_rank'].fillna(0)

    dynamic_height = df.shape[0]*10
    if dynamic_height < 700:
        dynamic_height = 700

    if dynamic_height > 10000:
        dynamic_height = 10000

    fig = px.bar(df, y='name', x='spe_rank', orientation='h',
                 title='Genes Filtered by P-Value Threshold: Gene & Specificity  in Chosen Cluster')

    fig.update_layout(
        yaxis_title='gene',
        xaxis_title='spe_rank',
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(df))),
            ticktext=df['name'],
            tickfont=dict(size=9)
        ),
        width=1200,
        height=dynamic_height,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#212124'),
        yaxis_showgrid=False,
        yaxis_gridcolor='#212124',
        xaxis_showgrid=True,
        xaxis_gridcolor='#eeeeee',
    )

    buffer = BytesIO()
    fig.write_image(buffer, format='png')
    buffer.seek(0)
    graph_data = base64.b64encode(buffer.read()).decode()

    return graph_data


# ---------------------------------------------------------------------------------------------------

def generate_graph3(filtered_genes):

    df = pd.DataFrame.from_records(filtered_genes)
    df['spe_rank'] = df['spe_rank'].fillna(0)
    df = df.sort_values('cluster')


    print('============================\n', df, '\n============================\n', flush=True)

    fig = px.bar(df, y='cluster', x='spe_rank', orientation='h', color='spe_rank',
                 title='Specificity Landscape of Selected Gene Across Clusters')

    fig.update_layout(
        yaxis_title='gene',
        xaxis_title='spe_rank',
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(df))),
            ticktext=df['cluster'],
            tickfont=dict(size=10)
        ),

        width=1200,
        height=5000,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#212124'),
        yaxis_showgrid=False,
        yaxis_gridcolor='#212124',
        xaxis_showgrid=True,
        xaxis_gridcolor='#eeeeee',
        xaxis={'categoryorder': 'total descending'}
    )

    buffer = BytesIO()
    fig.write_image(buffer, format='png')
    buffer.seek(0)
    graph_data = base64.b64encode(buffer.read()).decode()

    return graph_data



# ---------------------------------------------------------------------------------------------------


def generate_graph4(filtered_genes):
    df = pd.DataFrame.from_records(filtered_genes)
    df['spe_rank'] = df['spe_rank'].fillna(0)

    dynamic_height = df.shape[0]*10
    if dynamic_height < 700:
        dynamic_height = 700

    if dynamic_height > 50000:
        dynamic_height = 50000

    fig = px.bar(df, y='name', x='scz_2022_p_log', orientation='h',
                 title='Genes Filtered by Specificity  Threshold: Gene & P-Value in Chosen Cluster')

    fig.update_layout(
        yaxis_title='Gene',
        xaxis_title='-log(P-Value)',
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(df))),
            ticktext=df['name'],
            tickfont=dict(size=9)
        ),
        width=1200,
        height=dynamic_height,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#212124'),
        yaxis_showgrid=False,
        yaxis_gridcolor='#212124',
        xaxis_showgrid=True,
        xaxis_gridcolor='#eeeeee',
    )

    buffer = BytesIO()
    fig.write_image(buffer, format='png')
    buffer.seek(0)
    graph_data = base64.b64encode(buffer.read()).decode()

    return graph_data
