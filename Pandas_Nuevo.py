import pandas as pd
import json as json


ruta_excel = r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Compras_desde_ads.xlsx'
ruta_xml = r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Valores+de+acciones.xml'

df1 = pd.read_excel(ruta_excel)
df2 = pd.read_xml(ruta_xml)

print(df1)
print(df2)

df2 = pd.read_xml(ruta_xml)
print(df2)

numeros = {
    'romanos': ['I', 'II', 'III', 'IV'],
    'arabigos': [1, 2, 3, 4], 
    'texto': ['uno', 'dos', 'tres', 'cuatro']
}

df = pd.DataFrame(numeros)
print(df)

df['Fechas'] = pd.Series(pd.date_range('20240202', periods=4))
print(df)

# df.to_csv(r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Numeros3.csv', index=False)

data = {
    'Fecha': ['2024-03-19', '2024-03-20', '2024-03-21', '2024-03-22', '2024-03-23', '2024-03-24'],
    'Producto': ['Manzanas', 'Peras', 'Naranjas', 'Plátanos', 'Uvas', 'Melocotones'],
    'Cantidad': [23, 15, 18, 30, 8, 20],
    'Precio': [1.2, 1.5, 1.0, 0.8, 2.0, 1.7]
}
df_ventas = pd.DataFrame(data)
print(df_ventas)

data = {
    'Fecha': ['2024-03-19', '2024-03-20', '2024-03-21', '2024-03-22', '2024-03-23', '2024-03-24'],
    'Producto': ['Manzanas', 'Peras', 'Naranjas', 'Plátanos', 'Uvas', 'Melocotones'],
    'Cantidad': [23, 15, 18, 30, 8, 20],
    'Precio': [1.2, 1.5, 1.0, 0.8, 2.0, 1.7]
}
df_ventas = pd.DataFrame(data)
print(df_ventas)

# df_ventas.to_csv(r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Ventas2.csv', index=False)