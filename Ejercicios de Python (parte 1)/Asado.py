"""Asado"""

invitados = int(input("Ingrese la cantidad de invitados: "))
precio = float(input("Ingrese el precio de 1Kg de carne: "))

comprar = invitados * 0.7
pagar = precio * comprar

print(f"Franco deberá comprar {comprar}Kg de carne y deberá pagar ${pagar}")