import base64
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
from io import BytesIO
from app.models import CLUSTER as cluster_labels


def generate_graph(filtered_genes):
    if len(filtered_genes) <= 0:
        return None

    cluster_colors, super_cluster, legend_handles, added_colors = [], [], [], set()

    df = pd.DataFrame.from_records(filtered_genes)
    df['spe_rank'] = df['spe_rank'].fillna(0)

    for i, j in enumerate(cluster_labels):
        cluster_colors.append('#'+str(cluster_labels[i][1].split('#')[1]))
        super_cluster.append(cluster_labels[i][1].split('#')[0])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

    ax1.bar(df['cluster'], df['spe_rank'], color=cluster_colors, width=1)

    ax1.set_xlabel('Cluster ID')
    ax1.set_ylabel('Specificity Rank')
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)

    for i, (color, name) in enumerate(zip(cluster_colors, super_cluster)):
        if color not in added_colors:
            legend_handles.append(mpatches.Patch(color=color, label=name))
            added_colors.add(color)

    ax2.legend(handles=legend_handles, title='Color Legend',
               loc='center left', fontsize=8.4, borderaxespad=0.1).set_frame_on(False)
    ax2.axis('off')
    fig.tight_layout()
    fig.subplots_adjust(left=0.07, right=1.5, top=0.97, bottom=0.1)

    x_ticks = np.arange(0, 461, 20)
    ax1.set_xticks(x_ticks)

    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    graph_data = base64.b64encode(buffer.read()).decode()
    buffer.close()

    return graph_data
