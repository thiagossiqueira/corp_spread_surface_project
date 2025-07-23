from pandas import DataFrame
import plotly.graph_objects as go


def plot_yield_curve_surface(df: DataFrame, source_text: str ="") -> go.Figure:
    short_col = df.columns[0]             # line on shortest tenor
    zmin, zmax = df.values.min(), df.values.max()
    fig = go.Figure()
    fig.add_trace(go.Surface(
        x=df.columns, y=df.index, z=df.values,
        colorscale="ice", reversescale=True,
        cmin=zmin, cmax=zmax,
        hovertemplate="<br>Date: %{y}"
                      "<br>Maturity: %{x}"
                      "<br>Yield: %{z:.2f}%<extra></extra>"
    ))
    fig.add_trace(go.Scatter3d(
        x=[short_col]*len(df), y=df.index, z=df[short_col],
        mode="lines", line=dict(color="black", width=1.5),
        name=f"{short_col} yield"
    ))
    fig.update_layout(
        title="3-D Yield-Curve Surface", height=900,
        scene=dict(
            aspectratio=dict(x=1, y=1.75, z=0.75),
            camera=dict(eye=dict(x=1.65, y=1.57, z=0.25))
        ),
        margin=dict(l=0, r=0, t=40, b=10),
        annotations=[dict(text=source_text, x=0, y=0.02,
                          xref="paper", yref="paper", showarrow=False)]
    )
    return fig

__all__ = [
    "plot_yield_curve_surface",
]
