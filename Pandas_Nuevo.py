import pandas as pd
import json as json


ruta = r'C:\Users\javie\OneDrive\Desktop\Top-Películas.csv'
df = pd.read_csv(ruta)

print(df)

df_ordenado = df.sort_values(by='rating', ascending=False)
df_ordenado.head(10)
print(df)


df_ordenado = df.sort_values(by=['rating', 'recaudación(M)'], ascending=False)
df_ordenado.head(10)
print(df)

df_agrupado = df.groupby('género')['rating'].mean()
print(df_agrupado)


df_agrupado = df.groupby('año')['recaudación(M)'].sum()
df_agrupado.sort_values(ascending=False).head()
print(df_agrupado)