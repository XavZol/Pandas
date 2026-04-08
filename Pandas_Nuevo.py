import pandas as pd
import json as json


ruta = (r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Datos_Ventas_Tienda.csv')
df_ventas = pd.read_csv(ruta)
print(df_ventas)

ruta2 = (r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Datos_Ventas_Tienda2.csv')
df_ventas2 = pd.read_csv(ruta2)
print(df_ventas2)

df = pd.concat([df_ventas, df_ventas2], ignore_index=True)

print(df.tail()) #Para ver hasta donde determina el nuevo Data Frame 

df['Fecha'] = pd.to_datetime(df['Fecha'])
print(df)
print(df.info())

producto_mas_vendido = df.groupby('Producto')['Cantidad'].sum() 
producto_mas_vendido = producto_mas_vendido.sort_values(ascending=False)
print(producto_mas_vendido.head(1))

meses = [] # Lista vacía para almacenar los meses extraídos de la columna 'Fecha'
for f in df['Fecha']: # Iteramos sobre cada fecha en la columna 'Fecha' del DataFrame
    meses.append(f.month) # Agregamos el mes extraído a la lista 'meses'
df['Meses'] = meses  # Agregamos la lista de meses como una nueva columna en el DataFrame
print(df) # Imprimimos el DataFrame para verificar que la nueva columna 'Meses' se ha agregado correctamente


ventas_por_mes = df.groupby('Meses')['Total Venta'].sum().sort_values(ascending=False) # Agrupamos el DataFrame por la columna 'Meses', sumamos los valores de 'Total Venta' para cada mes y ordenamos los resultados de mayor a menor
print(ventas_por_mes.head(1)) # Imprimimos el resultado para ver el mes con las ventas totales más altas. El método head(1) se utiliza para mostrar solo la primera fila del resultado, que corresponde al mes con las ventas más altas.


ventas_por_categoria = df.groupby('Producto')['Total Venta'].sum() # Agrupamos el DataFrame por la columna 'Producto' y sumamos los valores de 'Total Venta' para cada producto
print(ventas_por_categoria) # Imprimimos el resultado para ver las ventas totales por categoría de producto

df.to_csv(r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Datos_Ventas_Tienda_Completo.csv', index=False) # Guardamos el DataFrame completo en un nuevo archivo CSV sin incluir el índice
