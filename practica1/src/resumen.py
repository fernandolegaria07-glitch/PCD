ruta_csv = "datos/reportes_transito-ruido_100000.csv" 

n_filas = 0
columnas = []
data = []
primeras_5_filas = []
tema = 'reportes_transito'

# Se inicializan variables (los índices se buscarán dinámicamente)
conteo_valores = []
frecuencias_valores = {}
conteo_validos = 0
min_val = float('inf')
max_val = float('-inf')

celdas_vacias_totales = 0
celdas_vacias_por_columna = {}

with open(ruta_csv, "r", encoding="utf-8") as archivo:
    linea_cabecera = archivo.readline().strip()
    columnas = linea_cabecera.split("|")
    
    # Detección dinámica de las columnas requeridas en la rúbrica
    pos_cat = columnas.index("zona") if "zona" in columnas else 0
    pos_num = columnas.index("duracion_incidente_min") if "duracion_incidente_min" in columnas else 0
    
    columna_numerica = columnas[pos_num]
    columna_categorica = columnas[pos_cat]
    
    for col in columnas:
        celdas_vacias_por_columna[col] = 0

    for linea in archivo:
        linea_limpia = linea.strip()
        linea_lista = linea_limpia.split("|")
        
        # Corrección de formato: Separar con barra y espacios
        if n_filas < 5:
            primeras_5_filas.append(" | ".join(linea_lista))
            
        data.append(linea_lista)
        n_filas += 1

        for i in range(len(linea_lista)):
            if linea_lista[i] == '':
                celdas_vacias_totales += 1
                if i < len(columnas):
                    celdas_vacias_por_columna[columnas[i]] += 1

        if pos_cat < len(linea_lista):
            cat = linea_lista[pos_cat].lower().title()
            if cat != '':
                if cat in frecuencias_valores:
                    frecuencias_valores[cat] += 1
                else:
                    frecuencias_valores[cat] = 1
                    
        if pos_num < len(linea_lista):
            num = linea_lista[pos_num]
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

frecuencias_lista = [*frecuencias_valores.items()]
valores_unicos = len(frecuencias_lista)
valor_mas_frec = frecuencias_lista[0] if frecuencias_lista else ("N/A", 0)

for tup in frecuencias_lista:
    if valor_mas_frec[1] < tup[1]:
        valor_mas_frec = tup

reporte = f"=== RESUMEN DEL DATASET ===\n"
reporte += f"Archivo: {tema}-ruido_100000.csv\n"
reporte += f"Pareja: Hugo Hernandez Carrillo - Fernando Legaria Mendoza\n"
# Corrección de la Semilla
reporte += f"Seed: 55\n\n"

reporte += f"--- Dimensiones ---\n"
reporte += f"Filas: {n_filas}\n"
reporte += f"Columnas: {len(columnas)}\n"
reporte += f"Nombres de columnas: {', '.join(columnas)}\n\n"

reporte += f"--- Primeras 5 filas ---\n"
# Corrección de formato de cabecera para que coincida visualmente
reporte += f"{' | '.join(columnas)}\n"
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