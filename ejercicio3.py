import pandas as pd
df = pd.read_csv("plantvillage_index.csv")

# Todas las imágenes enfermas de tomate
tomate_enfermo = df[(df["cultivo"] == "Tomato") & (df["sana"] == 0)]

# Cantidad de cultivos únicos disponibles
df["cultivo"].nunique()

# Lista de todas las enfermedades registradas
df["estado"].unique()

# Cultivo con mayor cantidad de enfermedades distintas
df.groupby("cultivo")["estado"].nunique().sort_values(ascending=False)