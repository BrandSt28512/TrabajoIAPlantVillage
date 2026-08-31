import pandas as pd
df = pd.read_csv("plantvillage_index.csv")

# Dimensiones del dataset
print(df.shape)

# Primeras filas
df.head()

# Tipos de datos y valores no nulos
df.info()

# Estadísticas descriptivas (columnas numéricas)
df.describe()


