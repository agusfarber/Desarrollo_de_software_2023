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
while op != 9:

    if op == 1:
        print("Ingrese el valor 1: ")
        op1 = int(input())
    else: 
        print("ERROR: debe ingresar la opcion 1")

    if op == 2:
        print("Ingrese el valor 2: ")
        op2 = int(input())
    else:
        print("ERROR: debe ingresar la opcion 2")
    
    if op == 3:
        suma = op1 + op2
        print(f"SUMA: {suma}")
    else:
        print("ERROR: debe ingresar la opcion 3")

    if op == 4:
        resta = (op1 - op2) * 2
        print(f"RESTA: {resta}")
    else:
        print("ERROR: debe ingresar la opcion 4")

    if op == 5:
        mult = op1 * op2
        print(f"MULTIPLICACION: {mult}")
    else:
        print("ERROR: debe ingresar la opcion 5")

    if op == 6:
        div = op1 / op2
        print(f"DIVISION: {div}")
    else: 
        print("ERROR: debe ingresar la opcion 6")