import plotly.express as px

def plot_results(y_true, y_pred):
    fig = px.scatter(
        x=y_true,
        y=y_pred,
        labels={
            "x": "Temperatura Real",
            "y": "Temperatura Predicha"
        },
        title="Control CMC - Temperatura Real vs Predicha"
    )
    return fig


def plot_sort_comparison(merge_time, radix_time):
    fig = px.bar(
        x=["Merge Sort", "Radix Sort"],
        y=[merge_time, radix_time],
        labels={
            "x": "Algoritmo",
            "y": "Tiempo de ejecución (segundos)"
        },
        title="Comparación de tiempos: Merge Sort vs Radix Sort"
    )
    return fig
