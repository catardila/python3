min=int(input("Ingrese el número mínimo: "))
max=int(input("Ingrese el número máximo: "))
a=int(input("Ingrese el número entero a: "))

if a >= min and a <= max:
    print("El numero", a,"está dentro del intervalo [",min,",", max,"]")
else:
    print("El numero", a,"NO está dentro del intervalo [",min,",", max,"]")