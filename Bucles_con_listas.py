#Lista
name = ['Ana', 'Pablo', 'Diego', 'Carmen']

#Para una lista de diccionarios
person = []
a = {'nombre':'Ana', 'edad': 28 }
b = {'nombre':'Pablo', 'edad': 35}
c = {'nombre':'Luis', 'edad': 38 }

person.append(a)
person.append(b)
person.append(c)

for person1 in person:
    print(person1['nombre'])
    print( person1['edad'])
    print( person)
    
lista_name = []

for person2 in person:
    lista_name.append(person2['nombre'])
print(lista_name)

#Lista de nunmeros

numbers = [1, 2, 3, 4, 5]
for index, number in enumerate(numbers):
    numbers[index] += 3
print(numbers)

