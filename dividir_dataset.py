import pandas as pd
from sklearn.model_selection import train_test_split

# Cargar el índice previamente generado
df = pd.read_csv("plantvillage_index.csv")

# Dividir el dataset
train_df, temp_df = train_test_split(
    df, test_size=0.3, stratify=df["clase"], random_state=42
)
val_df, test_df = train_test_split(
    temp_df, test_size=0.5, stratify=temp_df["clase"], random_state=42
)

print("Train:", train_df.shape[0])
print("Val:  ", val_df.shape[0])
print("Test: ", test_df.shape[0])