n1 = int(input("Ingrese el límite inferior del primer intervalo: "))
a1 = int(input("Ingrese el límite superior del primer intervalo: "))

n2 = int(input("Ingrese el límite inferior del segundo intervalo: "))
a2 = int(input("Ingrese el límite superior del segundo intervalo: "))

n3 = int(input("Ingrese el límite inferior del tercer intervalo: "))
a3 = int(input("Ingrese el límite superior del tercer intervalo: "))

b=int(input("Ingrese el número entero b: "))

if (b > n1 and b < a1) or (b > n2 and b < a2) or (b > n3 and b < a3):
    print("El número", b, "está dentro de alguno de los intervalos.")
else:
    print("El número", b, "está fuera de los tres intervalos.") 