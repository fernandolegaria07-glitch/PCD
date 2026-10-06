ruta_csv = "datos/reportes_transito-ruido_100.csv" 

n_filas = 0
columnas = []
primeras_5_filas = []

with open(ruta_csv, "r", encoding="utf-8") as archivo:
    
    linea_cabecera = archivo.readline().strip()
    columnas = linea_cabecera.split("|")
    
    for linea in archivo:
        linea_limpia = linea.strip()
        
        if n_filas < 5:
            primeras_5_filas.append(linea_limpia)
        
        n_filas += 1

print(f"Total de columnas: {len(columnas)}")
print(f"Nombres de columnas: {columnas}")
print(f"Total de filas (sin cabecera): {n_filas}")
print("\nPrimeras 5 filas:")
for fila in primeras_5_filas:
    print(fila)