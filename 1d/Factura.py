precioFactura = int(input("Introduce el precio de la factura"))
facturaTotal = 0
while precioFactura != 0:
    facturaTotal += precioFactura
    precioFactura = int(input("Introduce el precio de la factura"))   
    
print("El precio final es %.2f" % facturaTotal)
print ("Fin del programa")
