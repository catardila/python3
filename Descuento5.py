precio=float(input("Ingrese el valor del artículo: "))
descuento=precio*0.05
total=precio-descuento

if precio>150000:
    print("El artículo tiene un descuento de: ", descuento)
    print("Valor total: ", total)
else:
    print("El articulo no tiene ningun tipo de descuento")    