import pandas as pd
df = pd.read_csv("plantvillage_index.csv")

# Aquí se realiza el ejercicio #1
# Es fundamental verificar si el dataset está balanceado antes de entrenar el modelo.

# Número de imágenes por clase específica (cultivo + estado)
df["clase"].value_counts()

# Número de imágenes por tipo de cultivo
df["cultivo"].value_counts()

# Porcentaje de hojas sanas vs enfermas
df["sana"].value_counts(normalize=True) * 100

# Combinación cultivo + estado (tabla cruzada)
df.groupby(["cultivo", "estado"]).size().sort_values(ascending=False)