import pandas as pd
import plotly.express as px

def descriptive_table(df):
    stats = df.describe().round(2)
    return stats

def boxplot_temperature(df):
    fig = px.box(
        df,
        y="MaxTemp",
        title="Boxplot de Temperatura Máxima (Muestra Reducida)"
    )
    return fig
