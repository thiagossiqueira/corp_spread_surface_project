from pandas import DataFrame
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def plot_historical_yield_curve(df: DataFrame, source_text: str ="", id_vars: str ="DATE") -> go.Figure:
    df_rev = df.iloc[:, ::-1]
    melt = pd.melt(df_rev.reset_index(), id_vars=id_vars,
                   var_name="Maturity", value_name="Yield")
    melt[id_vars] = pd.to_datetime(melt[id_vars]).dt.strftime("%b-%Y")

    fig = px.line(
        melt, x="Maturity", y="Yield",
        animation_frame=id_vars, animation_group="Maturity",
        range_y=[df.values.min(), df.values.max()],
        color_discrete_sequence=["cornflowerblue"],
        labels={"Yield": "Yield (%)"}
    )
    latest = df_rev.iloc[-1]
    fig.add_trace(go.Scatter(x=latest.index, y=latest.values,
                             name="Latest", line=dict(color="black", width=3)))
    for s in fig.layout.sliders[0].steps:
        s["args"][1]["frame"]["redraw"] = True
    for b in fig.layout.updatemenus[0].buttons:
        b["args"][1]["frame"]["redraw"] = True
        b["args"][1]["frame"]["duration"] = 200
    fig.update_layout(
        title="Animated Yield-Curve History", height=600,
        margin=dict(t=70, b=90, l=20, r=20),
        annotations=[dict(text=source_text, x=0, y=-0.15,
                          xref="paper", yref="paper", showarrow=False)]
    )
    return fig

__all__ = [
    "plot_historical_yield_curve",
]
