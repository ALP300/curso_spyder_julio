# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 20:48:00 2025

@author: aitor
"""

import pandas as pd
import numpy as np
datos = pd.read_csv('Data.csv', encoding='latin-1')
print(datos.info())
print('\n'*10)
print(datos.head())
print('\n'*10)
nuevo= pd.DataFrame(datos)
nuevo= nuevo.replace(np.nan,"0")
print(nuevo.info())
print(nuevo.describe())
print(nuevo.describe())
nuevo= nuevo.replace("N/A","0")
nuevo= nuevo.replace("NR","0")
nuevo['WRank'] = nuevo['WRank'].astype(int)
nuevo['Wsets'] = nuevo['Wsets'].astype(int)
print(nuevo)
print('\n'*10)
print(nuevo.describe())