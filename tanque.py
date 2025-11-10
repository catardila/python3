litros=float(input("Ingrese la cantidad de litros que tiene el tanque: "))

if litros<250:
    print("La llave debe ser abierta para llenar el tanque")
elif litros>450:
    print("La llave del tanque debe ser cerrada")
else:
    print("El tanque esta en un nivel adecuado")