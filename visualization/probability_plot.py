# visualization/influence_plot.py

import plotly.graph_objects as go

def plot_influence(influence_scores):

    nodes = list(influence_scores.keys())
    values = list(influence_scores.values())

    fig = go.Figure()

    fig.add_bar(x=nodes, y=values)

    fig.update_layout(
        title="Node Influence on Axis Victory",
        xaxis_title="Node",
        yaxis_title="Influence Score"
    )

    return fig