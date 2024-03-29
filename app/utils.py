import pandas as pd
import plotly.graph_objects as go
from app.models import CLUSTER as cluster_labels
from plotly.graph_objs import Layout


def generate_graph(filtered_genes, phenotype=None, option=3):

    if len(filtered_genes) <= 0:
        return None

    cluster_colors, super_cluster = [], []

    df = pd.DataFrame.from_records(filtered_genes)
    df2 = pd.DataFrame.from_records(phenotype)
    if option == 3:
        df['spe_val'] = df['spe_val'].fillna(0)
    else:
        df['enrichment_score'] = df['enrichment_score'].fillna(0)

    print(df2, flush=True)

    for i, j in enumerate(cluster_labels):
        cluster_colors.append('#'+str(cluster_labels[i][1].split('#')[1]))
        super_cluster.append(cluster_labels[i][1].split('#')[0])
    df['cluster'] = df['cluster'].astype(str)
    df2['top_three_regions'] = df2['top_three_regions'].astype(str)
    df2['top_three_dissections'] = df2['top_three_dissections'].astype(str)
    df['hovertext'] = 'Cluster: ' + df['cluster'] + '<br>Super Cluster: ' + \
        super_cluster + ' <br>Top Three Regions: ' + \
        df2['top_three_regions'] + '<br> Top Three Dissections: ' + df2['top_three_dissections']

    traces = []

    for i in range(len(super_cluster)):
        mask = [True if x == i else False for x in range(len(super_cluster))]

        show_legend = i == super_cluster.index(super_cluster[i])

        trace = go.Bar(
            x=df['cluster'][mask],
            y=df['spe_val'][mask] if option == 3 else df['enrichment_score'][mask],
            name=super_cluster[i] if show_legend else '',
            text=df['hovertext'][mask],
            hoverinfo='y+text',
            marker=dict(color=cluster_colors[i]),
            textposition='inside',
            textfont=dict(color=cluster_colors[i]),
            showlegend=show_legend,
            hoverlabel=dict(font_size=18),
        )

        traces.append(trace)

    layout = Layout(
        paper_bgcolor='rgb(255,255,255)',
        plot_bgcolor='rgb(255,255,255)',
        bargap=0,
        bargroupgap=0,
        xaxis_title='Cluster number (Siletti et al. 2023)',
        yaxis_title='Specificity value (Duncan et al. in review)' if option == 3 else 'Enrichment value (Siletti et al. 2023)',
    )

    fig = go.Figure(data=traces, layout=layout).update_traces(width=1)

    fig.update_layout(legend=dict(font=dict(size=12, color="black")))

    plot_html = fig.to_html(full_html=True, default_width='100%', default_height='800px')

    return plot_html
