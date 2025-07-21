import pandas as pd
df= pd.read_csv('canciones.csv')
filas= len(df.index)
print("Número de filas: ", filas)
df.drop(df.index[[filas-1]], inplace=True)
filas= len(df.index)
print("Número de filas: ", filas)