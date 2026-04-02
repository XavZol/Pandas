import pandas as pd
import json as json


numeros = pd.Series([ 10, 20, 30 , 40, 50])
print(numeros)

promedio = numeros.mean()
print(f"El promedio es {promedio}")

total = numeros.sum()
print(total)

maximo = numeros.max()
print(maximo)

minimo = numeros.min()
print(minimo)
