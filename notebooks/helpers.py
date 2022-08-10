import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def get_entries_fig(entries=pd.DataFrame):

    entries_fig = px.scatter(entries)
    entries_fig.update_traces(
        marker=dict(
            symbol='triangle-up',
            color='green',
            size=15,
            line=dict(
                    width=1,
                    color='black'
                ),
            ),
        selector=dict(mode='markers')
    )

    return entries_fig