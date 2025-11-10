tipo=int(input("Ingrese el tipo de artículo: "))
n1=float(input("Ingrese el precio del articulo: "))
n2=n1-(n1*0.125)
n3=n1-(n1*0.083)
n4=n1-(n1*0.032)

if tipo==1:
    print("El descuento es del 12.5%")
    print("El valor fial del producto es: ", n2)
elif tipo==2:
    print("El descuento es del 8.3%")
    print("El valor final del producto es: ", n3)
elif tipo==3:
    print("El descuento es de 3.2%") 
    print("El valor final del producto es: ", n4)
else:
    print("Descuento invalido")
