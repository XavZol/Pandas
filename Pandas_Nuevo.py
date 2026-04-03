import pandas as pd
import json as json

df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Nombre': ['Ana', 'Luis', 'Carlos'] })
df2 = pd.DataFrame({'ID': [1, 2, 4], 
                    'Edad': [25, 30, 23]})

print(df1)
print(df2)

df_combinado = pd.merge(df1, df2, on='ID' , how='outer')
print(df_combinado)

df_combinado = pd.merge(df1, df2, on='ID' , how='right')
print(df_combinado)

df_indexado = pd.merge(df1, df2, left_index=True, right_index=True)
print(df_indexado)
