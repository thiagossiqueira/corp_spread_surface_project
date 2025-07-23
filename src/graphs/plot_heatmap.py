from pandas import DataFrame
import plotly.graph_objects as go


def plot_heatmap(df: DataFrame, source_text="") -> go.Figure:
    zmin, zmax = df.values.min(), df.values.max()
    data = df.T.iloc[::-1]   # flip so shortest at bottom
    fig = go.Figure(data=[go.Heatmap(
        z=data.values, x=data.columns, y=data.index,
        colorscale="ice", reversescale=True,
        zmin=zmin, zmax=zmax,
        hovertemplate="<br>Date: %{x}"
                      "<br>Maturity: %{y}"
                      "<br>Yield: %{z:.2f}%<extra></extra>"
    )])
    fig.update_layout(
        title="Yield-Curve Heat-map", height=600,
        margin=dict(t=70, b=90, l=20, r=20),
        annotations=[dict(text=source_text, x=0, y=-0.15,
                          xref="paper", yref="paper", showarrow=False)]
    )
    return fig

__all__ = [
    "plot_heatmap",
]
