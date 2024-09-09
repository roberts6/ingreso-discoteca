
edad = int(input("Por favor, ingresá tu edad: "))
permitido = edad >= 18 # es lo mismo que --> permitido = True if edad >= 18 else False 

if permitido :
    print("Bienvenido! ya podés ingresar")
else:
    print("Lo sentimos, pero por ley no podemos dejarte ingresar.")