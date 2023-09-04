# -*- coding: utf-8 -*-
import csv
'''
La función cargar_productos() carga los datos de los productos
desde el archivo "productos.csv"
* parámetros: no recibe
* valor de retorno: devuelve una lista con la información de los productos,
donde cada producto es un diccionario que contiene los siguientes campos:
[
	{
		id: 1,
		nombre: 'Disco Solido SSD - 240GB - GIGABYTE',
		precio: 3696,
	},
    {
		id: 2,
		nombre: 'Mouse GAMER LOGITECH G300S GAMING',
		precio: 2904,
	},
]

Ejemplo de uso:
l = []
l = cargar_productos()
'''
def cargar_productos():
    productos = []
    with open('productos.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            np = {}
            np['id'] = int(row[0])
            np['nombre'] = row[1].strip()
            np['precio'] = float(row[2])
            productos.append(np)
    return productos