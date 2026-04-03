import pandas as pd
import json as json

fechas = pd.Series(pd.date_range('2024-01-01', periods=5)) #D: Día, M: Mes, Y: Año, h: Hora
print(fechas)

type(fechas[0])

fechas = pd.Series(pd.date_range('2024-01-01', periods=8, freq='ME')) #ME: Mes final, YE: Año final, h: Hora
print(fechas)


fechas = pd.Series(pd.date_range('2024-01-01', periods=8, freq='h')) #h: Hora, D: Día, M: Mes, Y: Año
print(fechas)

fechas = pd.Series(pd.date_range('2024-01-01', periods=8, freq='YE')) #YE: Año final, ME: Mes final, h: Hora
print(fechas)

fechas = pd.Series(pd.date_range('2024-01-01', periods=8, freq='5D' )) #D: Día, M: Mes, Y: Año, h: Hora, 5D: Cada 5 días, 2M: Cada 2 meses, 3Y: Cada 3 años
print(fechas)

ruta = r'C:\Users\javie\OneDrive\Desktop\Excel_DB\Mercado+de+Valores+España.csv'
df =pd.read_csv(ruta)
print(df)

df['Fecha'][0]

type(df['Fecha'][0])

df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
print(df)

df['Fecha'][0]
print(df)

pd.Timestamp('2024-01-02 00:00:00')
type(df['Fecha'][0])

pd.Timestamp('2024-02-15 00:00:00')
print(df['Fecha'][44])

pd.Timestamp('2024-02-15 00:00:00')
print(df['Fecha'][44].year)

pd.Timestamp('2024-02-15 00:00:00')
print(df['Fecha'][44].month)

df_mas = df['Fecha'] + pd.Timedelta(days=10) # datos temporales en días, horas, minutos, segundos, etc. pd.Timedelta(days=10) suma 10 días a cada fecha en la columna 'Fecha'
print(df_mas)

