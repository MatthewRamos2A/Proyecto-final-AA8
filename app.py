from flask import Flask, render_template, request
from preprocessing import load_and_preprocess
from model import train_model
from visualization import plot_results, plot_sort_comparison
from sorting import compare_sorts
from statistics import descriptive_table, boxplot_temperature

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    fig = None
    sort_fig = None
    stats_table = None
    boxplot_fig = None

    try:
        if request.method == "POST":
            file = request.files["file"]

            # 🔹 Ahora recibimos 3 valores
            df, data, sample_df = load_and_preprocess(file)

            # 🔹 Modelo climático
            model, X_test, y_test = train_model(df)
            y_pred = model.predict(X_test)

            fig = plot_results(y_test, y_pred).to_html(
                include_plotlyjs="cdn"
            )

            # 🔹 Comparación Merge Sort vs Radix Sort
            merge_time, radix_time = compare_sorts(data)

            sort_fig = plot_sort_comparison(
                merge_time, radix_time
            ).to_html(include_plotlyjs="cdn")

            # 🔹 Tabla estadística descriptiva (muestra reducida)
            stats_table = descriptive_table(sample_df).to_html(
                classes="table table-striped"
            )

            # 🔹 Boxplot
            boxplot_fig = boxplot_temperature(sample_df).to_html(
                include_plotlyjs="cdn"
            )

    except Exception as e:
        return str(e)

    return render_template(
        "index.html",
        fig=fig,
        sort_fig=sort_fig,
        stats_table=stats_table,
        boxplot_fig=boxplot_fig
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)