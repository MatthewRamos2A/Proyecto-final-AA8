import pandas as pd
from exceptions import ClimateDataError

def load_and_preprocess(file):
    try:
        df = pd.read_csv(file)

        if "MaxTemp" not in df.columns:
            raise ClimateDataError(
                "El dataset no contiene la columna MaxTemp"
            )

        df = df[["MaxTemp"]].dropna().sample(n=50, random_state=42)

        # Lista numérica para los algoritmos de ordenamiento
        data = df["MaxTemp"].astype(int).tolist()

        # 🔹 MUESTRA REDUCIDA PARA ANÁLISIS ESTADÍSTICO
        sample_df = df.sample(n=min(50, len(df)), random_state=42)

        return df, data, sample_df

    except Exception as e:
        raise ClimateDataError(str(e))
