import pandas as pd
import json as json

df1 = pd.DataFrame({'Nombre': ["Juan", "Gabriel", "María"], 'Edad': [23, 25, 30]})
print(df1)

df2 = pd.DataFrame({'Nombre': ["Carlos", "Ana", "Luis"], 'Edad': [25, 24, 26]})
print(df2)

df_concatenando = pd.concat([df1, df2])
print(df_concatenando)

df_concatenando1 = pd.concat([df1, df2], axis=1) # Modifica el axis a las tablas para unirlas horizontalmente
print(df_concatenando1)

df_concatenando = pd.concat([df1, df2], ignore_index=True) # Modifica el index para que no se repitan los indices de las tablas
print(df_concatenando)


df_concatenando = pd.concat([df1, df2], keys=['df1', 'df2']) # Agrega una columna con el nombre de la tabla de origen 
print(df_concatenando)



ventas_enero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"],
                            'Cantidad': [300, 200, 150]})

ventas_febrero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"],
                                'Cantidad': [350, 210, 170]})

ventas_concatenadas = pd.concat([ventas_enero, ventas_febrero], keys=['Enero', 'Febrero'])
print(ventas_concatenadas)



datos_cliente = pd.DataFrame({'Nombre': ["Ana", "Luis", "Marta"], 
                            'Edad': [34, 45, 28]})

compras_cliente = pd.DataFrame({'Producto': ["Libro", "Lápiz", "Cuaderno"],
                                'Precio': [15.50, 0.50, 2.00]})

datos_compras = pd.concat([datos_cliente, compras_cliente], axis=1)
print(datos_compras)



tienda_a = pd.DataFrame({'Producto': ["Manzanas", "Bananas"],
                        'Cantidad': [500, 300]})

tienda_b = pd.DataFrame({'Producto': ["Naranjas", "Peras"], 
                        'Cantidad': [400, 250]})

tiendas_concatenadas = pd.concat([tienda_a, tienda_b], ignore_index=True)
print(tiendas_concatenadas)