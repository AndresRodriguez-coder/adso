def mostrar_texto():
    print('Hola')

mostrar_texto()  # Llama a la función y muestra "Hola"

def multiplicar():
    a = 5
    b = 8
    print(a * b)

multiplicar()  # Llama a la función y muestra 40 (5 * 8)

# Ámbito de las variables. Las variables declaradas DENTRO de la función no son accesibles desde fuera, solo desde la propia función.
# Las de fuera, sin embargo, sí son accesibles desde dentro de la función.

def multiplicar():
    print(a * b)  # Usa las variables globales 'a' y 'b'

a = 5
b = 8
multiplicar()  # Llama a la función y muestra 40 (5 * 8)

# Las funciones pueden devolver valores con la instrucción return.
# En el siguiente caso, devolvemos la multiplicación, y el resultado lo guardamos en una variable, que luego imprimimos sumándole un valor.

def multiplicar():
    a = 5
    b = 8
    return a * b  # Devuelve el resultado de la multiplicación

resultado = multiplicar()  # Guarda el resultado de la función en la variable 'resultado'
print(resultado + 5)  # Muestra 45 (40 + 5)

# Podemos devolver cualquier tipo de dato, y tratarlo como tal fuera de la función.

def validar_dato():
    if a == 5:
        return True
    else:
        return False

a = 5
resultado = validar_dato()  # Llama a la función y guarda el resultado
print(resultado)  # Muestra True, ya que 'a' es igual a 5

# El potencial de la función es poder pasarle un dato para que opere con él, lo que se llama argumento.

def validar_dato(a, b):
    if a == b:
        return True
    else:
        return False

a = 5
b = 3
resultado = validar_dato(a, b)  # Llama a la función con los argumentos 'a' y 'b'
print(resultado)  # Muestra False, ya que 'a' no es igual a 'b'

# Si lo combinamos con un bucle for, nos queda un código mucho más sencillo que si lo hiciéramos contemplando cada caso.
# En este caso, recorremos una lista de números y vemos si el valor introducido por pantalla existe en la lista.

def validar_dato(a):
    if a == b:
        return True
    else:
        return False

numeros = [1, 2, 3, 4, 5, 6]
print("Introduce un número para ver si está en la lista")
b = int(input())  # Solicita un número al usuario

for numero in numeros:
    if validar_dato(numero):  # Llama a la función para validar si el número está en la lista
        print("El número", b, "está en la lista")
        break
else:
    print("El número", b, "no está en la lista")

# Una función con argumentos espera dichos argumentos en el orden en que está definida.

def validar(dato1, dato2):
    # Verifica que se hayan pasado exactamente dos argumentos
    if not (isinstance(dato1, (int, float)) and isinstance(dato2, (int, float))):
        raise ValueError("Se esperaban exactamente dos datos numéricos.")
    return True

validar(10, 20)