# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 20:15:03 2025

@author: aitor
"""

import pandas as pd
import numpy as np

datos= {
    'Nombre':["Pedro", "Ana", "Luis", "Marta", "Juan"],
    'Calificacion':[8, 9, 7, 6, 10],
    'Deportes':["Futbol", "Baloncesto", "Tenis", "Natacion", "Ciclismo"],
    'Materia':['Matematicas', 'Historia', 'Ciencias', 'Lengua', 'Ingles'],
    'Edad':[15, 16, 15, 17, 16],
}
df= pd.DataFrame(datos)
print(df)
print('\n'*5)
datos2= {
    'Nombre':["Pedro", "Ana", "Luis", "N/A", "Juan"],
    'Calificacion':["8", "8", "8", np.nan, "10"],
    'Deportes':["Futbol", "N/A", "Tenis", "Natacion", "Ciclismo"],
    'Materia':['Matematicas', 'Historia', 'Ciencias', 'Lengua', 'N/A'],
    'Edad':["15", "16", "15", "17", "16"],
}
df2= pd.DataFrame(datos2)
print(df2)
print(df2.info())
print('\n'*5)
print(df2.describe())
nuevo= pd.DataFrame(df2)
nuevo= nuevo.replace(np.nan,"0")
print(nuevo)
columna= df2[df2['Nombre'] != "N/A"]
print(columna)
print('\n'*5)
nuevo['Calificacion'] = nuevo['Calificacion'].astype(int)
print(nuevo.describe())