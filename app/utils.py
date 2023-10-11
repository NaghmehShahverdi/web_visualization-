import pandas as pd
import plotly.graph_objects as go
from app.models import CLUSTER as cluster_labels

# def generate_graph(filtered_genes):
#     if len(filtered_genes) <= 0:
#         return None

#     cluster_colors, super_cluster, legend_handles, added_colors = [], [], [], set()

#     df = pd.DataFrame.from_records(filtered_genes)
#     df['spe_val'] = df['spe_val'].fillna(0)

#     for i, j in enumerate(cluster_labels):
#         cluster_colors.append('#'+str(cluster_labels[i][1].split('#')[1]))
#         super_cluster.append(cluster_labels[i][1].split('#')[0])

#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

#     ax1.bar(df['cluster'], df['spe_val'], color=cluster_colors, width=1)

#     ax1.set_xlabel('Cluster ID')
#     ax1.set_ylabel('Specificity Value')
#     ax1.spines['right'].set_visible(False)
#     ax1.spines['top'].set_visible(False)
#     ax1.spines['left'].set_visible(False)
#     ax1.spines['bottom'].set_visible(False)

#     for i, (color, name) in enumerate(zip(cluster_colors, super_cluster)):
#         if color not in added_colors:
#             legend_handles.append(mpatches.Patch(color=color, label=name))
#             added_colors.add(color)

#     ax2.legend(handles=legend_handles, title='Color Legend',
#                loc='center left', fontsize=8.4, borderaxespad=0.1).set_frame_on(False)
#     ax2.axis('off')
#     fig.tight_layout()
#     fig.subplots_adjust(left=0.07, right=1.5, top=0.97, bottom=0.1)

#     x_ticks = np.arange(0, 461, 20)
#     ax1.set_xticks(x_ticks)


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


    plot_html = fig.to_html(full_html=True,default_width='100%')

    return plot_html