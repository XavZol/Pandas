import pandas as pd
import json as json

df1 = pd.DataFrame({'Salario': [30000, 45000, 38000],
                    'Antigüedad': [9, 13, 15]},
                    index=[1, 2, 3])
df2 = pd.DataFrame({'Ciudad': ['Madrid', 'Barcelona', 'Valencia'],
                    'Jerarquía' : ['Baja', 'Alta', 'Media']},
                    index=[1, 2, 4])

print(df1)
print(df2)

df_unido = df1.join(df2)
print(df_unido)


df_unido = df1.join(df2, how='inner')
print(df_unido)

# Creación del DataFrame df_a
df_a = pd.DataFrame({
    'id': [1, 2, 3],
    'Nombre': ['Ana', 'Beto', 'Carla']
})
df_a.set_index('id', inplace=True)

# Creación del DataFrame df_b
df_b = pd.DataFrame({
    'id': [1, 2, 3],
    'Edad': [25, 30, 35]
})
df_b.set_index('id', inplace=True)

df_join = df_a.join(df_b)
print(df_join)

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
}).set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2],
    'NombreCategoria': ['Categoría 1', 'Categoría 2']
}).set_index('CategoriaID')

nombreMerc = productos_df.join(categorias_df)
print(nombreMerc)

nombreMerc = productos_df.join(categorias_df, how='left')
print(nombreMerc)

nombreMerc = productos_df.join(categorias_df, how='right')
print(nombreMerc)

productos_df1 = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
})

productos_df1 = productos_df1.set_index('ProductoID')

categorias_df1 = pd.DataFrame({
    'CategoriaID': [1, 2, 3],
    'NombreCategoria': ['Categoría 1', 'Categoría 2', 'Categoría 3']
}).set_index('CategoriaID')


nombreMercancía = productos_df1.join(categorias_df1, how='inner')
print(nombreMercancía)

nombreMercancía = productos_df1.join(categorias_df1, how='right')
print(nombreMercancía)

nombreMercancía = productos_df1.join(categorias_df1, how='left')
print(nombreMercancía)