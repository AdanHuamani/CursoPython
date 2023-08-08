alumnos = {}
alumnos["nombre"] = input("Ingrese el nombre del alumno: ")
alumnos["apellidos"] = input("Ingrese los apellidos del alumno: ")
alumnos["DNI"] = int(input("Ingrese el DNI del alumno: "))
alumnos["programa_estudio"] = input("Ingrese el programa de estudios del alumno: ")
unidades_didacticas = []
num_unidades = int(input("Ingrese el número de unidades didácticas: "))

for i in range(num_unidades):
    unidad = {}
    unidad["nombre"] = input(f"Ingrese el nombre de la unidad {i+1}: ")
    unidad["promedio"] = float(input(f"Ingrese el promedio de la unidad {i+1}: "))
    if unidad["promedio"] >= 12:
        unidad["condicion"] = "aprobado"
    else:
        unidad["condicion"] = "desaprobado"

    unidades_didacticas.append(unidad)

alumnos["unidades_didacticas"] = unidades_didacticas

print(alumnos)