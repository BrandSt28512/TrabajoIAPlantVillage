import os
import pandas as pd
from pathlib import Path

DATASET_DIR = Path("PlantVillage-Dataset/raw/color")

registros = []

for carpeta_clase in DATASET_DIR.iterdir():
  if carpeta_clase.is_dir():
    nombre_clase = carpeta_clase.name
    for ruta_img in carpeta_clase.glob("*.JPG"):
      registros.append({
        "ruta": str(ruta_img),
        "clase": nombre_clase
      })

df = pd.DataFrame(registros)
print(df.shape)

df[["cultivo", "estado"]] = df["clase"].str.split("___", expand=True)

# Normalizar texto: minúsculas y sin guiones bajos sobrantes
df["cultivo"] = df["cultivo"].str.replace("_", " ").str.strip().str.title()
df["estado"]  = df["estado"].str.replace("_", " ").str.strip().str.title()

df["sana"] = df["estado"].str.lower().apply(
    lambda x: 1 if "healthy" in x else 0
)

df.to_csv("plantvillage_index.csv", index=False)
print("Índice generado correctamente ✅")