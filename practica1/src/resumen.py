ruta_csv = "datos/reportes_transito-ruido_100000.csv" 

n_filas = 0
columnas = []
data = []
primeras_5_filas = []
tema = 'reportes_transito'

pos_cat = 4
conteo_valores = []
frecuencias_valores = {}

pos_num = 2 
conteo_validos = 0
min_val = 10000000
max_val = -10000000

celdas_vacias_totales = 0
celdas_vacias_por_columna = {}

with open(ruta_csv, "r", encoding="utf-8") as archivo:
    linea_cabecera = archivo.readline().strip()
    columnas = linea_cabecera.split("|")
    columna_numerica = columnas[pos_num]
    
    for col in columnas:
        celdas_vacias_por_columna[col] = 0

    for linea in archivo:
        linea_limpia = linea.strip()

        if n_filas < 5:
            primeras_5_filas.append(linea_limpia)
            
        linea_limpia = linea_limpia.split("|")
        data.append(linea_limpia)
        n_filas += 1

        for i in range(len(linea_limpia)):
            if linea_limpia[i] == '':
                celdas_vacias_totales += 1
                if i < len(columnas):
                    celdas_vacias_por_columna[columnas[i]] += 1

        if pos_cat < len(linea_limpia):
            cat = linea_limpia[pos_cat].lower().title()
            if cat != '':
                if cat in frecuencias_valores:
                    frecuencias_valores[cat] += 1
                else:
                    frecuencias_valores[cat] = 1
                    
        if pos_num < len(linea_limpia):
            num = linea_limpia[pos_num]
            if num != '':
                try:
                    num = float(num)
                    conteo_validos += 1
                    if num > max_val:
                        max_val = num
                    if num < min_val: 
                        min_val = num
                except ValueError:
                    pass

columna_categorica = columnas[pos_cat]
frecuencias_lista = [*frecuencias_valores.items()]
valores_unicos = len(frecuencias_lista)
valor_mas_frec = frecuencias_lista[0] if frecuencias_lista else ("N/A", 0)

for tup in frecuencias_lista:
    if valor_mas_frec[1] < tup[1]:
        valor_mas_frec = tup

reporte = f"=== RESUMEN DEL DATASET ===\n"
reporte += f"Archivo: {tema}-ruido_100000.csv\n"
reporte += f"Pareja: Hugo Hernandez Carrillo - Fernando Legaria Mendoza\n"
reporte += f"Seed: ?\n\n"

reporte += f"--- Dimensiones ---\n"
reporte += f"Filas: {n_filas}\n"
reporte += f"Columnas: {len(columnas)}\n"
reporte += f"Nombres de columnas: {', '.join(columnas)}\n\n"

reporte += f"--- Primeras 5 filas ---\n"
reporte += f"{linea_cabecera}\n"
for fila in primeras_5_filas:
    reporte += f"{fila}\n"

reporte += f"\n--- Columna categorica: {columna_categorica} ---\n"
reporte += f"Valores unicos: {valores_unicos}\n"
reporte += f"Valor mas frecuente: {valor_mas_frec[0]} ({valor_mas_frec[1]} apariciones)\n\n"

reporte += f"--- Columna numerica: {columna_numerica} ---\n"
reporte += f"Valores validos (no vacios): {conteo_validos}\n"
if conteo_validos > 0:
    reporte += f"Minimo: {min_val}\nMaximo: {max_val}\n\n"
else:
    reporte += f"Minimo: N/A (Es puro texto)\nMaximo: N/A (Es puro texto)\n\n"

reporte += f"--- Calidad de datos ---\n"
reporte += f"Celdas vacias totales: {celdas_vacias_totales}\n"
reporte += f"Celdas vacias por columna:\n"
for col, vacias in celdas_vacias_por_columna.items():
    reporte += f"  {col}: {vacias}\n"

print(reporte)

ruta_txt = "practica1/resultados/resumen.txt"
try:
    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write(reporte)
    print("\n[OK] Archivo txt generado automaticamente en la carpeta resultados.")
except FileNotFoundError:
    print(f"\n[ERROR] No se pudo guardar el txt. Asegurate de crear la carpeta ejecutando: mkdir practica1/resultados")