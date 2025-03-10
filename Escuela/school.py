from pymongo import MongoClient
from pprint import pprint

# Conectar a MongoDB y crear una nueva base de datos
client = MongoClient("mongodb://localhost:27017/")
db = client["Universidad"]  # Nueva base de datos
alumnos = db["Alumnos"]  # Nueva colección

# Datos a insertar
datos_alumnos = [
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

# Insertar los datos en la colección
alumnos.insert_many(datos_alumnos)

# Mostrar todos los documentos de la colección
print("\nLista de alumnos en la base de datos 'Universidad':")
for alumno in alumnos.find():
    pprint(alumno)