#COMO USAR PANDAS PARA CREAR FILTROS

#1. importarlo
import pandas as pd

#2. traer los datos
from data.simulador import generar_ventas

#3. convertir los datos en un DATAFRAME
dataFrame=pd.DataFrame(generar_ventas())

#4. aplciar los filtros (5)