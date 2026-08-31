import pandas as pd
df = pd.read_csv("plantvillage_index.csv")
from PIL import Image

def obtener_dimensiones(ruta):
    with Image.open(ruta) as img:
        return img.size  # (ancho, alto)

# Aplicar sobre una muestra para no saturar memoria
muestra = df.sample(200, random_state=42).copy()
muestra[["ancho", "alto"]] = muestra["ruta"].apply(
    lambda r: pd.Series(obtener_dimensiones(r))
)

muestra[["ancho", "alto"]].describe()