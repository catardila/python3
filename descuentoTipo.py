tipo=input("Ingrese el tipo de artículo (Textil, Electrodoméstico, Elemntos de cocina,videojuego): ")
precio=float(input("Ingrese el precio del artículo: "))

tipo=tipo.upper()

if tipo == "TEXTIL":
    descuento = 0
elif tipo == "ELECTRODOMESTICO":
    descuento = 3.7
elif tipo == "ELEMENTOS DE COCINA":
    descuento = 4.2
elif tipo == "VIDEOJUEGO":
    descuento = 7.8
else:
    print("Artículo inválido")
    descuento = 0 

final = precio - (precio * descuento / 100)

print(f"El descuento es de {descuento}%")
print(f"El precio con descuento incluido es de: {final}")
