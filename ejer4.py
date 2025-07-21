# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 20:48:00 2025

@author: aitor
"""

import pandas as pd
import numpy as np
datos = pd.read_csv('Data.csv', encoding='latin-1')
print(datos.info())
print(datos.head())
print(datos.iloc[0:80])
print(datos.iloc[[0,2,3,100,230]])
print(datos.iloc[:, 0:2])
print(datos.iloc[[0,23,63,43],[0,6,2]])
print(datos.iloc[0:10, 0:5])