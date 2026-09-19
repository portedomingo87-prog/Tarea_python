#Sistema de compra en una tienda

#Datos del cliente
name = input("Deme su Nomble: ")
edad = int(input("Deme su edad: "))

if edad >= 18:
    print("Puede pasar")
else:
     print("No puede pasar")

#productos
pruductos = {
    "arroz" : 1500,
    "aceite" : 1600,
    "salami" : 950,
    "sopita" : 500
}

#productos disponoibres
print("---pruductos disponibles---")
print("1. arroz - $1500")
print("2. aceite - $1600")
print("3. salami - $950")
print("4. sopita - $500")

# Elegir producto
producto = input("Ingrese el producto que desea comprar: ").lower()
cantidad = int(input("Ingrese la cantidad: "))

#verificar producto

if producto in pruductos:
    print("pruducto: disponible")
    precio = pruductos[producto]
    subtotal = precio * cantidad

    print("Precio:", precio)
    print("Cantidad:", cantidad)
    print("Subtotal: RD$", subtotal)

else:
    print("error: no disponible")
    
#verificando si el cliente es mayor o menor de edad
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
 # Descuento del 10% si ases una compla mayor de 5000
if subtotal >= 5000:
        descuento = subtotal * 0.10
else:
        descuento = 0
    
        
print("-----Resumen de la compra-----")
    
print("Cliente:", name)
print("Edad:", edad)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio unitario: RD$", precio)
print("Subtotal: RD$", subtotal)
    
print("Gracias por su compra,", name)