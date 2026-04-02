import pandas as pd
import json as json

df = pd.read_csv(r"C:\Users\javie\OneDrive\Desktop\medallas.csv")

print(df)

print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

df_relleno = df.fillna(0, inplace=True) # Rellena directo el dataFrame y no genera una copia

print(df.describe())

print(df.isnull().sum())

print(df_relleno)

top_3_oro = df.sort_values('Oro', ascending=False).head(3) # obtener los tres primeros de ORO en orden ASCENDENTE
print(top_3_oro)

filtro = df['Total'] > 10
mas_10_medallas = df[filtro]
mas_10_medallas.sort_values('Total', ascending=False) 
print(mas_10_medallas)