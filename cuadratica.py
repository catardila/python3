a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))
discriminante=b**2-4*a*c

if a==0:
    print("No es una ecuación cuadratica")
elif discriminante < 0:
    print("La ecaucion no tiene solución")
else:
    print("La ecuacuón si tiene solución" )
