# 1. Ingresar valor 1
# 2. Ingresar valor 2
# 3. Mostrar suma
# 4. Mostrar resta
# 5. Mostrar multiplicación
# 6. Mostrar división
# 7. Salir

# Elija una opción:
# El programa debe continuar pidiendo al usuario que seleccione una opción hasta que se ingrese 7 (Salir).
# Si se selecciona alguna de las opciones: 3, 4, 5 o 6 sin antes haber pasado por las opciones 1 y 2
# (ingresar valores) se debe mostrar un mensaje de error.

print("MENU OPCIONES")

op = int(input("Ingrese una opcion: "))
while op != 7:

    if op == 1:
        op1=float(input("Ingrese el valor 1: "))
    elif op == 2:
       op2=float(input("Ingrese el valor 2: "))
    elif op == 3:
        op1=float(input("Ingrese el valor 1: "))
        op2=float(input("Ingrese el valor 2: "))
        suma = op1 + op2
        print(f"SUMA: {suma}")
    elif op == 4:
        op1=float(input("Ingrese el valor 1: "))
        op2=float(input("Ingrese el valor 2: "))
        resta = op1 - op2
        print(f"RESTA: {resta}")
    elif op == 5:
        op1=float(input("Ingrese el valor 1: "))
        op2=float(input("Ingrese el valor 2: "))
        mult = op1 * op2
        print(f"MULTIPLICACION: {mult}")
    else:
        op1=float(input("Ingrese el valor 1: "))
        op2=float(input("Ingrese el valor 2: "))
        div = op1 / op2
        print(f"DIVISION: {div}")
print("*****FIN, GRACIAS *****")