ruta_csv = "../../datos/reportes_transito-ruido_100.csv" 

n_filas = 0
columnas = []
primeras_5_filas = []
tema = 'reportes_transito'

with open(ruta_csv, "r", encoding="utf-8") as archivo:
    
    linea_cabecera = archivo.readline().strip()
    columnas = linea_cabecera.split("|")
    
    for linea in archivo:
        linea_limpia = linea.strip()

        if n_filas < 5:
            primeras_5_filas.append(linea_limpia)
        
        n_filas += 1

print("=== RESUMEN DEL DATASET ===")
print(f"Archivo: {tema}-ruido.csv")
print("Pareja: Hugo Hernandez Carrillo - Fernando Legaria Mendoza")
print("Seed: ?")

print('\n--- Dimensiones ---')

print(f"Filas: {n_filas}")
print(f"Total de columnas: {len(columnas)}")
print(f"Nombres de columnas: {columnas}")

print("\n--- Primeras 5 filas: ---")
print(linea_cabecera)
for fila in primeras_5_filas:
   print(fila)
