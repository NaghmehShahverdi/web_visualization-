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
    custom_legend = [
        dict(
            label=super_cluster[i],
            method='update',
            args=[{'visible': [True if x == i else False for x in range(len(super_cluster))]}, {'title': super_cluster[i]}],
        )
        for i in range(len(super_cluster))
    ]

    traces = []

    for i in range(len(super_cluster)):
        mask = [True if x == i else False for x in range(len(super_cluster))]
        trace = go.Bar(
            x=df['cluster'][mask],
            y=df['spe_val'][mask],
            name=super_cluster[i],
            text=df['hovertext'][mask],  # Set text to hovertext
            hoverinfo='text+y',  # Show hovertext and y value when hovering
            marker=dict(color=cluster_colors[i]),
            textposition='inside',
            textfont=dict(color=cluster_colors[i]) 
        )
        traces.append(trace)

    layout = go.Layout(
        barmode='group',
        xaxis=dict(type='category'),
        updatemenus=[
            {
                'buttons': custom_legend,
                'direction': 'down',
                'showactive': True,
                'x': 0.15,
                'xanchor': 'left',
                'y': 1.15,
                'yanchor': 'top',
            }
        ],

    )

    fig = go.Figure(data=traces, layout=layout)

    plot_html = fig.to_html(full_html=True,default_width='100%')

    return plot_html