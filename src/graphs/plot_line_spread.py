from pandas import DataFrame
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def plot_line_spread(df: DataFrame, low: str="2-year", high: str="10-year",
                     idx_name: str="DATE", source_text: str="") -> go.Figure:
    data = df.copy()
    data["Spread"] = data[high] - data[low]
    mask = data["Spread"] <= 0
    data["Spread_above"] = np.where(mask, data["Spread"], 0)
    data["Spread_below"] = np.where(mask, 0, data["Spread"])
    fig = px.area(data.reset_index(), x=idx_name, y="Spread",
                  hover_data={"Spread": True},
                  labels={"Spread": f"{high} − {low} (%)"})
    fig.add_trace(go.Scatter(x=data.index, y=data["Spread_above"],
                             fill="tozeroy", mode="none"))
    fig.add_trace(go.Scatter(x=data.index, y=data["Spread_below"],
                             fill="tozeroy", mode="none"))
    fig.update_layout(
        title=f"Yield-Spread: {high} minus {low}", height=550,
        margin=dict(t=60, b=90, l=20, r=20),
        annotations=[dict(text=source_text, x=0, y=-0.15,
                          xref="paper", yref="paper", showarrow=False)],
        showlegend=False
    )
    return fig

__all__ = [
    "plot_line_spread",
]
