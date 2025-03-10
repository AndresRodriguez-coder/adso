from pymongo import MongoClient
from pprint import pprint
#conectar a mongodb

client = MongoClient("mongodb://localhost:27017/")
db = client["Escuela1"]
estudiantes = db["Estudiantes1"]
datos_estudiantes = [
    {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería", "nota": 9.2},
    {"nombre": "Carlos", "edad": 22, "carrera": "Medicina", "nota": 8.7},
    {"nombre": "Elena", "edad": 21, "carrera": "Derecho", "nota": 9.5},
    {"nombre": "Fernando", "edad": 23, "carrera": "Arquitectura", "nota": 8.3},
    {"nombre": "Lucía", "edad": 19, "carrera": "Psicología", "nota": 9.0},
    {"nombre": "Miguel", "edad": 24, "carrera": "Economía", "nota": 8.6},
    {"nombre": "Sofía", "edad": 20, "carrera": "Diseño Gráfico", "nota": 9.8},
    {"nombre": "Javier", "edad": 22, "carrera": "Administración", "nota": 8.4},
    {"nombre": "Raquel", "edad": 21, "carrera": "Biología", "nota": 9.1},
    {"nombre": "David", "edad": 23, "carrera": "Matemáticas", "nota": 8.9}
]
estudiantes.insert_many(datos_estudiantes)
# Mostrar todos los documentos de la colección
print("\nLista de alumnos en la base de datos 'Escuela1':")
#mostrar todos los documentos
for estudiante in estudiantes.find():
    print(estudiante)

### 1. Encontrar los alumnos con nota mayor a 8
print("\nAlumnos con nota mayor a 8: ")
for estudiante in estudiantes.find({"nota": {"$gt": 8}}):
    pprint(estudiante)

### 2. Encontrar los alumnos que tienen 20 años
print("\nAlumnos de 20 años:")
for estudiante in estudiantes.find({"edad": 20}):
    pprint(estudiante)

### 3. Actualizar la nota de Ana a 9.5
estudiantes.update_one({"nombre": "Ana"}, {"$set": {"nota": 9.5}})
estudiante_act = estudiantes.find_one({"nombre":"Ana"})
print("\nNota de Ana actualizada.", estudiante_act)


### 4. Incrementar la edad de todos los alumnos en 1 año
estudiantes.update_many({}, {"$inc": {"edad": 1}})
print("\nEdad de todos los alumnos incrementada en 1 año.")

### 5. Encontrar alumnos con nota entre 7 y 9 y menores de 22 años
print("\nAlumnos con nota entre 7 y 9 y menores de 22 años:")
for estudiante in estudiantes.find({"nota": {"$gte": 7, "$lte": 9}, "edad": {"$lt": 22}}):
    pprint(estudiante)

### 6. Calcular el promedio de las notas de todos los alumnos
resultado = estudiantes.aggregate([{"$group": {"_id": None, "promedio_nota": {"$avg": "$nota"}}}])
for res in resultado:
    print(f"\nPromedio de notas de todos los alumnos: {res['promedio_nota']:.2f}")

### 7. Agrupar alumnos por carrera y calcular el promedio de notas
print("\nPromedio de notas por carrera:")
resultado = estudiantes.aggregate([
    {"$group": {"_id": "$carrera", "promedio_nota": {"$avg": "$nota"}}}
])
for res in resultado:
    print(f"Carrera: {res['_id']}, Promedio de nota: {res['promedio_nota']:.2f}")

#Crear un índice en el campo "carrera"
estudiantes.create_index("carrera")
print("\nÍndice creado en el campo 'carrera'.")

#Explicación sobre el índice
"""
Los índices mejoran el rendimiento de las consultas al evitar búsquedas completas en la colección.
Si buscamos por 'carrera', MongoDB usará el índice en lugar de recorrer todos los documentos.
"""

#Realizar una consulta con el índice creado
print("\nConsulta con índice en 'carrera' (Ingeniería):")
for estudiante in estudiantes.find({"carrera": "Ingeniería"}):
    pprint(estudiante)

#Eliminar alumnos con nota menor a 6
estudiantes.delete_many({"nota": {"$lt": 6}})
print("\nAlumnos con nota menor a 6 eliminados.")

#Crear la colección "Cursos" con un arreglo de alumnos inscritos
cursos = db["Cursos"]
cursos.insert_many([
    {"nombre": "Matemáticas Avanzadas", "alumnos": ["Ana", "Carlos", "David"]},
    {"nombre": "Psicología General", "alumnos": ["Lucía", "Raquel"]},
    {"nombre": "Ingeniería de Software", "alumnos": ["Javier", "Fernando", "Sofía"]},
])
print("\nColección 'Cursos' creada con alumnos inscritos.")

#Encontrar todos los cursos en los que está inscrito un alumno específico (ejemplo: Ana)
print("\nCursos en los que está inscrita Ana:")
for curso in cursos.find({"alumnos": "Ana"}):
    pprint(curso)