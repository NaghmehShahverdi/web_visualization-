import pandas as pd
import plotly.graph_objects as go
from app.models import CLUSTER as cluster_labels




def generate_graph(filtered_genes):
    if len(filtered_genes) <= 0:
        return None

    cluster_colors, super_cluster, legend_handles, added_colors = [], [], [], set()

    df = pd.DataFrame.from_records(filtered_genes)
    df['spe_val'] = df['spe_val'].fillna(0)

    for i, j in enumerate(cluster_labels):
        cluster_colors.append('#'+str(cluster_labels[i][1].split('#')[1]))
        super_cluster.append(cluster_labels[i][1].split('#')[0])
    df['cluster'] = df['cluster'].astype(str)
    df['hovertext'] = 'Cluster: ' + df['cluster'] + '<br>Super Cluster: ' + super_cluster
    # Create a custom legend for superclusters


    traces = []

    for i in range(len(super_cluster)):
        mask = [True if x == i else False for x in range(len(super_cluster))]

        # Only show the legend entry for the first trace in each supercluster
        show_legend = i == super_cluster.index(super_cluster[i])

        trace = go.Bar(
            x=df['cluster'][mask],
            y=df['spe_val'][mask],
            name=super_cluster[i] if show_legend else '',  # Set the name for the first trace only
            text=df['hovertext'][mask],  # Set text to an empty string
            hoverinfo='y+text',  # Show y value and text when hovering
            marker=dict(color=cluster_colors[i]),
            textposition='inside',
            textfont=dict(color=cluster_colors[i]),
            showlegend=show_legend,  # Control legend visibility
        )

        traces.append(trace)


    fig = go.Figure(data=traces)


    plot_html = fig.to_html(full_html=True,default_width='100%',default_height='800px')

    return plot_html