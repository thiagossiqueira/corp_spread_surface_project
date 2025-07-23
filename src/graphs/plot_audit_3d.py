from pandas import DataFrame
import plotly.graph_objects as go


def plot_audit_3d(surface_df: DataFrame) -> go.Figure:
    """
    3-D scatter for DI futures:
        x = tenor (years, numeric),
        y = obs_date,
        z = yield (%).
    """
    pts = surface_df.sort_values("obs_date")

    fig = go.Figure(data=[
        go.Scatter3d(
            x=pts["tenor"],               # numeric tenor
            y=pts["obs_date"],
            z=pts["yield"],
            mode="markers",
            marker=dict(size=4, color="royalblue", opacity=0.8),
            text=(pts["id"] + "<br>" +
                  "Tenor: " + pts["tenor"].round(2).astype(str) + " yrs"),
            hovertemplate="<b>%{text}</b><br>Date: %{y|%Y-%m-%d}"
                          "<br>Yield: %{z:.2f}%<extra></extra>"
        )
    ])

    fig.update_layout(
        title="DI Futures – Yield vs. Tenor & Date",
        height=700,
        scene=dict(
            xaxis_title="Tenor (years)",
            yaxis_title="Obs date",
            zaxis_title="Yield (%)"
        ),
        margin=dict(l=20, r=20, t=40, b=40)
    )
    return fig


__all__ = [
    "plot_audit_3d",
]
