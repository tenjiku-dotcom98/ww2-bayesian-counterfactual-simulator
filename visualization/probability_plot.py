# visualization/probability_plot.py

import plotly.graph_objects as go

def plot_probability_shift(baseline, counterfactual):
    fig = go.Figure()

    fig.add_bar(
        name="Baseline",
        x=["Axis Victory"],
        y=[baseline]
    )

    fig.add_bar(
        name="Counterfactual",
        x=["Axis Victory"],
        y=[counterfactual]
    )

    fig.update_layout(
        title="Axis Victory Probability Shift",
        yaxis_title="Probability",
        barmode="group"
    )

    return fig