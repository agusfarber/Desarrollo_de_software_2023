"""Club deportivo"""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 13 and edad < 15:
    categoria = "infantiles"
elif edad >= 15 and edad < 17:
    categoria = "cadetes"
elif edad >= 17 and edad < 19:
    categoria = "juveniles"
elif edad >= 19:
    categoria = "mayores"
else:
    categoria = "sin categoría"

print(f"La categoría a la que pertenece {nombre} es: {categoria}")