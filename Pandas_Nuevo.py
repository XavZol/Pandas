import pandas as pd
import json as json
serie = pd.Series([5 , 10 , 15 , 20 , 25])
print(serie)


# Los convertimos a booleanos
filtro = serie > 15
serie_filtrada = serie[filtro]
print(filtro)

# Indexamos los resultados ya convertidos
print(serie_filtrada)

serie2 = pd.Series(["banana", "pera", "melon", "manzana"])
print(serie2)


print(f"{dir(serie2.to_json)}")

type(serie2)

filtro2 = serie2.str.contains("m")
print(filtro2)
print(serie2[filtro2])