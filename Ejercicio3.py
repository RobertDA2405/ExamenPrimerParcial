'''
Crea una aplicacion que permita calcular el 10% de descuento a los productos cuyo precio sea mayor a 500 cordobas.
'''
#definimos las funciones
def calcular_descuento(precio):
    if precio > 500:
        descuento = precio * 0.10
        precio_con_descuento = precio - descuento
        return precio_con_descuento
    else:
        return precio

producto = str(input("Ingrese el nombre del producto: "))
precio_producto = float(input("Ingrese el precio del producto en córdobas: "))

precio_final = calcular_descuento(precio_producto)

print(f"Para el {producto} con precio {precio_producto} el precio final con descuento es:", precio_final, "córdobas")