import numpy as np

nombre_archivo = 'reportes_transito-ruido_100000.csv'
dir_archivo = f'../../datos/{nombre_archivo}'
seed = 55

def a_float(texto):
    try:
        return float(texto.strip())
    except (ValueError, AttributeError):
        return np.nan


with open(dir_archivo, 'r' ) as f:
    lineas = f.read().strip().split('\n')
cabecera = lineas[0].split('|')
data = [linea.split('|') for linea in lineas[1:]]


index_num_1, index_num_2 = cabecera.index('vehiculos_afectados'), cabecera.index('duracion_incidente_min')
data_afectados = np.array([a_float(value[index_num_1]) for value in data])
data_duracion = np.array([a_float(value[index_num_2]) for value in data])

limpio_afectados = data_afectados[~np.isnan(data_afectados)]
limpio_duracion = data_duracion[~np.isnan(data_duracion)]


resul = {
    'archivo': nombre_archivo,
    'pareja': 'Hugo Hernández - Fernando Legaria',
    'seed': seed,

    'numerica_1' : {
        'columna': f'{cabecera[index_num_1]}',
        'n_valores_validos': sum(limpio_afectados),
        'media': round(limpio_afectados.mean(), 2),
        'desviacion_estandar': round(limpio_afectados.std(), 2),
        'minimo': limpio_afectados.min(),
        'maximo': limpio_afectados.max(),
        'mediana': np.percentile(limpio_afectados, 50),
        'percentil_25': np.percentile(limpio_afectados, 25),
        'percentil_75': np.percentile(limpio_afectados, 75),
    },

    'numerica_2' : {
        'columna': f'{cabecera[index_num_2]}',
        'n_valores_validos': sum(limpio_duracion),
        'media': round(limpio_duracion.mean(), 2),
        'desviacion_estandar': round(limpio_duracion.std(), 2),
        'minimo': limpio_duracion.min(),
        'maximo': limpio_duracion.max(),
        'mediana': np.percentile(limpio_duracion, 50),
        'percentil_25': np.percentile(limpio_duracion, 25),
        'percentil_75': np.percentile(limpio_duracion, 75),
    }
}