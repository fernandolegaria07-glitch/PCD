ruta_csv = "../../datos/reportes_transito-ruido_100.csv" 

n_filas = 0
columnas = []
data = []
primeras_5_filas = []
tema = 'reportes_transito'

# Datos previos para la muestra de columna categorica
pos_cat = 4
conteo_valores = []
frecuencias_valores = {}

# Datos para la muestra de columna numerica (de la rama de tu amigo)
pos_num = 2
conteo_validos = 0
min = 10000000
max = 0

with open(ruta_csv, "r", encoding="utf-8") as archivo:
    
    linea_cabecera = archivo.readline().strip()
    columnas = linea_cabecera.split("|")
    
    # Extraemos el nombre de la columna hasta que el archivo ya se leyó
    columna_numerica = columnas[pos_num]
    
    for linea in archivo:
        linea_limpia = linea.strip()

        if n_filas < 5:
            primeras_5_filas.append(linea_limpia)
        linea_limpia = linea_limpia.split("|")
        data.append(linea_limpia)
        n_filas += 1

        # Lógica combinada (tuya y de tu amigo)
        cat = linea_limpia[pos_cat].lower().title()
        if cat != '':
            if cat in frecuencias_valores:
                frecuencias_valores[cat] += 1
            else:
                frecuencias_valores[cat] = 1

        num = linea_limpia[pos_num]
        if num != '':
            num = float(num)
            if num > 0:
                conteo_validos += 1
                if num > max:
                    max = num
                if num < min: 
                    min = num

# Transformacion de datos previos a datos mostrables
columna_categorica = columnas[pos_cat]
frecuencias_lista = [*frecuencias_valores.items()]
valores_unicos = len(frecuencias_lista)
valor_mas_frec = frecuencias_lista[0]

# Calculo del valor mas frecuente
for tup in frecuencias_lista:
    if valor_mas_frec[1] < tup[1]:
        valor_mas_frec = tup

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
   
# Tu código de formato
print(f"\n--- Columna categórica: {columna_categorica} ---")
print(f"Valores únicos: {valores_unicos}")
print(f"Valor más frecuente: {valor_mas_frec[0]} ({valor_mas_frec[1]} apariciones)")