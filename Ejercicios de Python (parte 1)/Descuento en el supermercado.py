"""Descuento en el supermercado"""

importe = float(input("Ingrese el monto de su compra: "))
if importe > 3500:
    importe = importe - (importe * 0.10)

print(f"El importe final que debe abonar es: {importe}")