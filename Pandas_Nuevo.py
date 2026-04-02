import pandas as pd

datos = {"nombre" : ["Pedro", "Juan", "Lorena"], "edad": [25, 39, 34]}

# {'nombre': ['Pedro', 'Juan', 'Lorena'], 'edad': [25, 39, 34]}

df = pd.DataFrame(datos)
print(df)

df["nombre"]