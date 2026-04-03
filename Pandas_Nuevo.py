import pandas as pd
import json as json

data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 52, 48],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}
df = pd.DataFrame(data)

print(df)

df['Salario'] = [30000, 40000, 80000, 40000]
df['Salario'] = df['Salario'] + 2000
print(df)

nombre = df['Nombre']
print(nombre)

mayores_25 = df[df['Edad'] >25]
print(mayores_25)

edades = df['Edad']
print(edades)

mayores_25 = df[edades > 40]
print(mayores_25)

type(edades)
type(mayores_25)
