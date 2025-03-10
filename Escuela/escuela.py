from pymongo import MongoClient
from pprint import pprint

# Conectar a MongoDB y crear la base de datos 'escuela'
cliente = MongoClient("mongodb://localhost:27017/")
base_datos = cliente["escuela"]
coleccion_estudiantes = base_datos["estudiantes"]

# Insertar 5 documentos en la colección 'estudiantes'
documentos_estudiantes = [
    {"nombre": "Ana", "edad": 20, "curso": "Matemáticas", "nota": 9.2},
    {"nombre": "Carlos", "edad": 22, "curso": "Medicina", "nota": 8.7},
    {"nombre": "Elena", "edad": 21, "curso": "Derecho", "nota": 9.5},
    {"nombre": "Fernando", "edad": 23, "curso": "Arquitectura", "nota": 8.3},
    {"nombre": "Lucía", "edad": 19, "curso": "Psicología", "nota": 9.0}
]
coleccion_estudiantes.insert_many(documentos_estudiantes)

# Encontrar todos los estudiantes con nota mayor a 8
print("\nEstudiantes con nota mayor a 8:")
for estudiante in coleccion_estudiantes.find({"nota": {"$gt": 8}}):
    pprint(estudiante)

# Encontrar estudiantes que tienen 20 años
print("\nEstudiantes de 20 años:")
for estudiante in coleccion_estudiantes.find({"edad": 20}):
    pprint(estudiante)

# Actualizar la nota de "Ana" a 9.5
coleccion_estudiantes.update_one({"nombre": "Ana"}, {"$set": {"nota": 9.5}})
estudiante_actualizado = coleccion_estudiantes.find_one({"nombre": "Ana"})
print("\nNota de Ana actualizada:", estudiante_actualizado)

# Incrementar la edad de todos los estudiantes en 1 año
coleccion_estudiantes.update_many({}, {"$inc": {"edad": 1}})
print("\nEdad de todos los estudiantes incrementada en 1 año.")

# Encontrar estudiantes con nota entre 7 y 9 y menores de 22 años
print("\nEstudiantes con nota entre 7 y 9 y menores de 22 años:")
for estudiante in coleccion_estudiantes.find({"nota": {"$gte": 7, "$lte": 9}, "edad": {"$lt": 22}}):
    pprint(estudiante)

# Calcular el promedio de las notas de todos los estudiantes
resultado_promedio = coleccion_estudiantes.aggregate([{"$group": {"_id": None, "promedio_nota": {"$avg": "$nota"}}}])
for res in resultado_promedio:
    print(f"\nPromedio de notas de todos los estudiantes: {res['promedio_nota']:.2f}")

# Agrupar estudiantes por curso y calcular la nota promedio por curso
print("\nPromedio de notas por curso:")
resultado_curso = coleccion_estudiantes.aggregate([
    {"$group": {"_id": "$curso", "promedio_nota": {"$avg": "$nota"}}}
])
for res in resultado_curso:
    print(f"Curso: {res['_id']}, Promedio de nota: {res['promedio_nota']:.2f}")

# Crear un índice en el campo 'curso'
coleccion_estudiantes.create_index("curso")
print("\nÍndice creado en el campo 'curso'.")

# Explicación sobre el índice
"""
Los índices mejoran el rendimiento de las consultas al evitar búsquedas completas en la colección.
Si buscamos por 'curso', MongoDB usará el índice en lugar de recorrer todos los documentos,
lo que acelera la consulta significativamente.
"""

# Realizar una consulta que utilice el índice creado
print("\nConsulta con índice en 'curso' (Matemáticas):")
for estudiante in coleccion_estudiantes.find({"curso": "Matemáticas"}):
    pprint(estudiante)

# Eliminar estudiantes con nota menor a 6
coleccion_estudiantes.delete_many({"nota": {"$lt": 6}})
print("\nEstudiantes con nota menor a 6 eliminados.")

# Crear la colección 'cursos' con un arreglo de estudiantes inscritos
coleccion_cursos = base_datos["cursos"]
coleccion_cursos.insert_many([
    {"nombre": "Matemáticas Avanzadas", "alumnos": ["Ana", "Carlos"]},
    {"nombre": "Psicología General", "alumnos": ["Lucía"]},
    {"nombre": "Ingeniería de Software", "alumnos": ["Fernando", "Elena"]}
])
print("\nColección 'cursos' creada con estudiantes inscritos.")

# Encontrar todos los cursos en los que está inscrito un estudiante específico (ejemplo: Ana)
print("\nCursos en los que está inscrita Ana:")
for curso in coleccion_cursos.find({"alumnos": "Ana"}):
    pprint(curso)