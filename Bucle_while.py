contador = 0
while contador < 10:
    contador += 1
    print("Iteración", contador)

#While=True combinado con break nos permite un bucle infinito mientras no se cumpla la condición

while True:
    print("Introduzca un valor mayor que 5")
    a = int(input())
    if a > 5:
        print("Es correcto")
       
    else:
        print("Es incorrecto, pruebe de nuevo")
        break