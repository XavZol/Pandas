import pandas as pd
import json as json

df = pd.DataFrame({
    'Col1': [100, 200, 300], 
    'Col2': [400, 500, 600],
    'Col3': [300, 800, 900]
}, index=['fila1', 'fila2', 'fila3'])
# Fila específica y columna específica
df.loc['fila1', 'Col1']  # Retorna 100
print(df)

# Múltiples filas y columnas
df.loc[df.index.isin(['fila1', 'fila3']), ['Col1', 'Col2']]
print(df)

# Filas con condición y columnas específicas
subf = df.loc[df['Col1'] > 150, df.columns.isin(['Col1', 'Col3'])]
print(subf)

subtabla = df.loc[df['Col1'] > 200]  # Dividir tu tabla en subtablas
print(subtabla)

booldf = df.loc[[False, True, False]] #Traer solo la fila2 por booleanos
print(booldf)

df3 = df.loc[df['Col1'] > 150]
print(df3)

col = df.loc[ : , ['Col1', 'Col2']]
print(col)

# LOC nos permite elegir filas y coolumnas por etiquetas, mientras que ILOC nos permite elegir filas y columnas por posición.


elegir = df.iloc[0]
print(elegir)

elegir = df.iloc[:, [0, 1]]
print(elegir)   

elegir = df.iloc[1 : 3]
print(elegir)   

df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Carmen'],
    'Edad': [25, 30, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
}, index=['fila1', 'fila2', 'fila3'])

# Seleccionar la fila de Luis
luis = df.loc['fila2']
print(luis)

# Seleccionar la columna de Edad
edad = df['Edad']
print(edad)

# Seleccionar la edad de Carmen
edad_carmen = df.loc['fila3', 'Edad']
print(edad_carmen)