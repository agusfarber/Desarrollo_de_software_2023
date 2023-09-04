import random
lista_atletas = []
def generar_lista_de_atletas():

	
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": random.random()*120
		}
		lista_atletas.append(atleta)
	return lista_atletas

def mostrar_lista_de_atletas():
	for elem in lista_atletas: 
		print(f"Numero: {elem['numero']}, Nombre:{elem['nombre']},Tiempo de llegada: {elem['tiempo_llegada']}")

def ganador():
	g=None
	num=0
	for elem in lista_atletas:
		if elem["tiempo_llegada"] < g :
			num= elem["numero"]	
	return num

def buscar_atleta(n):
	tiemplleg=0.0
	
	for elem in lista_atletas:
		if elem["numero"] == n:
			tiemplleg=elem["tiempo_llegada"]
			nomb=elem["nombre"]
			
	return nomb,tiemplleg

generar_lista_de_atletas()
mostrar_lista_de_atletas()
num =ganador()
print(f"El numero del ganador es {num}")
numatleta=int(input("Ingrese el numero del atleta a buscar "))
(nom,tiemp)=buscar_atleta(numatleta)
print(f"Atleta numero {numatleta}")
print(f"Nombre {nom}")
print(f"Tiempo llegada: {tiemp:.2f}")