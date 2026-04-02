import pandas as pd

# Usar raw string o barras normales para evitar errores de escape en Windows
df = pd.read_csv(r"C:\Users\javie\OneDrive\Desktop\Precipitaciones.csv")

# Verifica que la carga fue correcta
serie = df["region"]
print(serie.head())

# print(df.head())

datos = [10,55,60,80]
serie2 = pd.Series(datos)
serie2 = serie2 + 100
print(serie2)

indices = ["a", "b", "c", "d"]
serie2 = pd.Series(datos, indices)
print(serie2)

print(serie2["b"])

paises = ["México", "Argentina", "España", "Estados Unidos" ]
capitales = ["Distrito Federal", "Buenos Aires", "Madrid", "Washington D.C"]
Mezlca = ["México Distrito Federal"]
serie3 = pd.Series(capitales,paises)
print(f"{serie3} ")

data = {"Id_producto": [1001, 1002, 1003, 1003],
        "Cantidad_vendida": [30, None, 25, 25],
        "Precio": [20.5, 15, None, 22.6]}

df = pd.DataFrame(data)
print(df)
print(df.info())
print(df.isnull()) # true o false
print(df.isnull().sum())

df_eliminados = df.dropna() # traer los valores diferenciados
print(df_eliminados)

valores = {"Cantidad_vendida" : 0, "Precio": df["Precio"].mean()} #Método mean para el promedio
df_eliminados2 = df.fillna(valores) #rellenar los valores no válidos


# df_eliminados2["Cantidad_vendida"] = df_eliminados2["Cantidad_vendida"].astype("int64")  Otra forma de convertir a enteros
df_eliminados2["Cantidad_vendida"] = df_eliminados2["Cantidad_vendida"].astype(int) 
print(df_eliminados2)

# ELIMINAR DIPLICADOS
df_unicos  = df_eliminados2.drop_duplicates(subset="Id_producto") # Con subset especificamos la columna a checar
print(df_unicos)