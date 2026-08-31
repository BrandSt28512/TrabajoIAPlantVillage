import pandas as pd
df = pd.read_csv("plantvillage_index.csv")

# ¿Cuál es el cultivo con mayor número de imágenes?
cultivo_top = df["cultivo"].value_counts().idxmax()
total_top = df["cultivo"].value_counts().max()
print(f"1. El cultivo con mayor número de imágenes es '{cultivo_top}' con {total_top} imágenes.")

# ¿Qué porcentaje del dataset corresponde a hojas sanas?
porcentaje_sanas = df["sana"].mean() * 100
print(f"2. El porcentaje de hojas sanas en el dataset es del {porcentaje_sanas:.2f}%.")

# ¿Existe algún cultivo sin categoría "healthy"?
# Agrupamos por cultivo y verificamos si la suma de la columna 'sana' es igual a 0
cultivos_sin_healthy = df.groupby("cultivo")["sana"].sum()
cultivos_faltantes = cultivos_sin_healthy[cultivos_sin_healthy == 0].index.tolist()

if cultivos_faltantes:
    print(f"3. Sí, existen cultivos sin categoría 'healthy': {', '.join(cultivos_faltantes)}.")
else:
    print("3. No, todos los cultivos cuentan con al menos una categoría de hojas sanas ('healthy').")