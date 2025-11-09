num1=float(input("Ingrese su primer número: "))
num2=float(input("Ingrese su segundo número: "))
num3=float(input("Ingrese su tercer número: " ))
num4=float(input("Ingrese su cuarto número: "))

if num1>num2 and num1>num3 and num1>num4:
    print("El número ", num1, " es mayor")
elif num2>num1 and num2>num3 and num2>num4:
    print("El número", num2, " es mayor")    
elif num3>num1 and num3>num2 and num3>num4:
    print("El número", num3, " es mayor")   
else:
    print("El numero ", num4, " es mayor")     