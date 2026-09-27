"""Sistema de compra en una tienda"""

#Datos del cliente
name = input("Deme su Nomble: ")
edad = int(input("Deme su edad: "))

if edad >= 18:
    print("Puede pasar")
else:
    print("No puede pasar")

#productos
productos = {
    "arroz" : 1500,
    "aceite" : 1600,
    "salami" : 950,
    "sopita" : 500,
    "huevos" : 150,
    "pepinos" : 120
}

#productos disponibres
print("---productos disponibles---")

for producto, precio in productos.items():
    print(producto, "-", "$", precio)

#Elegir producto
producto = input("Ingrese el producto que desea comprar: ").lower()
cantidad = int(input("Ingrese la cantidad: "))

#verificar producto

if producto in productos:
    print("producto: disponible")
    precio = productos[producto]
    subtotal = precio * cantidad

    print("Precio:", precio)
    print("Cantidad:", cantidad)
    print("Subtotal: RD$", subtotal)

#verificando si el cliente es mayor o menor de edad
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

 #Descuento del 10% si ases una compla mayor de 5000
    if subtotal >= 5000:
        DESCUENTO = subtotal * 0.10
    else:
        DESCUENTO = 0

    total = subtotal - DESCUENTO

    print("-----Resumen de la compra-----")

    print("Cliente:", name)
    print("Edad:", edad)
    print("Producto:", producto)
    print("Cantidad:", cantidad)
    print("Precio unitario: RD$", precio)
    print("Subtotal: RD$", subtotal)
    print("Descuento: RD$", DESCUENTO)
    print("Total: RD$", total)

    print("Gracias por su compra,", name)

else:
    print("error: no disponible")
