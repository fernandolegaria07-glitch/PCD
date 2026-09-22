"""
Mi primer script de Programacion para la ciencia de datos
Demustra: print, input, f-strings y estructura de archivs.
"""

nombre = input("Nombre del estudiante: ")
pareja = input("Nombre de tu pareja de practicas: ")
tema = input("Tema asignado (ej. ventas online): ")

resumen = f"""
=== Programacion para la ciencia de datos === 
Estudiante: {nombre}
Pareja: {pareja}
Tema de practicas: {tema}
Semestre Agosto - Diciembre 2026
"""

print(resumen)

with open("../resultados/mi_info.txt", "w") as f:
    f.write(resumen)

print("Archivo guardado en resultado/mi_info.txt")

