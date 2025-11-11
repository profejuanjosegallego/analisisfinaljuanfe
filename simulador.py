#contruir un codigo de py que genere mil datos asociado a las ventas de un local de ropa 

#MOCK ejercicio que utilizamos para sumilar datos 
#def funcion en py

from datetime import datetime,timedelta

def generar_ventas():

    productos=[
        {"nombre": "camiseta POLO","precio":150000},
        {"nombre": "pantalon clasico","precio":300000},
        {"nombre": "chaqueta chevignon","precio":450000},
        {"nombre": "camisa leñadora","precio":200000},
        {"nombre": "Bermuda","precio":130000}
    ]

    tallas=["S","M","L","XL"]
    vendedores=["Juan Morales","Emma Aristizabal","Eliana Restrepo","Juan Muñoz","Juan gil",]

    fechaInicio=datetime(2025,1,1)