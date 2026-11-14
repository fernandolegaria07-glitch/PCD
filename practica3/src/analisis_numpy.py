import time
import math
import numpy as np
import json

def a_float(texto):
    try:
        return float(texto.strip())
    except (ValueError, AttributeError):
        return np.nan
def redondear_sig(numero, cifras):
    if numero == 0:
        return 0
    desplazamiento = cifras - int(math.floor(math.log10(abs(numero)))) - 1
    return round(numero, desplazamiento)


def extraer_datos(dir_archivo):
    with open(dir_archivo, 'r') as f:
        lineas = f.read().strip().split('\n')
    cabecera = lineas[0].split('|')
    data = [linea.split('|') for linea in lineas[1:]]
    return cabecera, data


'''
    Devuelve en una diccionario con los nombres de cada valor, siendo el primer valor
    de la tupla el tiempo y el segundo el valor, sirviendo este ultimo para la comprobacion
'''
def tiempos_puro(data):
    inicio_media = time.perf_counter()
    total = 0.0
    for v in data:
        total += v
    media = total / len(data)
    tiempo_media = time.perf_counter() - inicio_media

    inicio_std = time.perf_counter()
    suma_std = 0.0
    for v in data:
        suma_std += (v - media) ** 2
    std = math.sqrt(suma_std / len(data))
    tiempo_std = time.perf_counter() - inicio_std
    return {
        'media': (tiempo_media, media),
        'std': (tiempo_std, std),
    }

def tiempos_numpy(data):
    inicio_media = time.perf_counter()
    media = np.mean(data)
    tiempo_media = time.perf_counter() - inicio_media
    inicio_std = time.perf_counter()
    std = np.std(data)
    tiempo_std = time.perf_counter() - inicio_std
    return {
        'media': (tiempo_media, media),
        'std': (tiempo_std, std),
    }

def benchmarking(data):
    t_py = tiempos_puro(data)
    t_np = tiempos_numpy(data)
    tiempo_py = t_py['std'][0] + t_py['media'][0]
    tiempo_np = t_np['std'][0] + t_np['media'][0]

    if not math.isclose(t_py['std'][1], t_np['std'][1]) or not math.isclose(t_py['media'][1], t_np['media'][1]):
        raise Exception('El valor estandar o la media no son correctos en el benchmarking')

    return {
        'n_filas': len(data),
        'tiempo_bucle_python_seg': redondear_sig(tiempo_py, 2),
        'tiempo_numpy_seg': redondear_sig(tiempo_np,2),
        'factor_velocidad': round(tiempo_py / tiempo_np, 2),
        'operacion_medida': 'Calcular media y desviacion estandar'
    }


class Numerica:
    def __init__(self, nombre, index, raw):
        self.std = None
        self.media = None
        if index == -1:
            raise Exception('Nombre invalido')
        self.nombre = nombre
        self.data = np.array([a_float(value[index]) for value in raw])
        self.mask = np.isnan(self.data)
        self.validos = self.data[~self.mask]

    def calcular_estadisticas(self):
        self.media = np.mean(self.validos)
        self.std = np.std(self.validos)
        return {
            'columna': self.nombre,
            'n_valores_validos': len(self.validos),
            'media': round(np.mean(self.validos), 2),
            'desviacion_estandar': round(np.std(self.validos), 2),
            'minimo': round(np.min(self.validos),2),
            'maximo': round(np.max(self.validos),2),
            'mediana': round(np.percentile(self.validos, 50),2),
            'percentil_25': round(np.percentile(self.validos, 25),2),
            'percentil_75': round(np.percentile(self.validos, 75),2),
        }

    def identificar_outliers(self, k=3):
        media = self.media
        std = self.std
        inferior = media - k * std
        superior = media + k * std
        outliers = self.validos[(self.validos < inferior) | (self.validos > superior)]
        return {
            'metodo': 'desviacion_estandar_3',
            'limite_inferior': round(inferior, 2),
            'limite_superior': round(superior, 2),
            'n_outliers': len(outliers),
            'porcentaje': round( (len(outliers) / len(self.validos)) * 100, 2),
            'outliers_minimo': round(np.min(outliers),2) if len(outliers) != 0 else None,
            'outliers_maximo': round(np.max(outliers),2) if len(outliers) != 0 else None,
        }


nombre_archivo = 'reportes_transito-ruido_100000.csv'
dir_archivo = f'../../datos/{nombre_archivo}'
seed = 55

cabecera, data = extraer_datos(dir_archivo)
nombre_num_1, nombre_num_2 =  'duracion_incidente_min', 'vehiculos_afectados'
num_1 = Numerica(index=cabecera.index(nombre_num_1), nombre=nombre_num_1, raw=data)
num_2 = Numerica(index=cabecera.index(nombre_num_2), nombre=nombre_num_2, raw=data)

resul = {
    'archivo': nombre_archivo,
    'pareja': 'Hugo Hernández - Fernando Legaria',
    'seed': seed,

    'numerica_1' : num_1.calcular_estadisticas(),
    'numerica_2' : num_2.calcular_estadisticas(),

    'outliers_numerica_1': num_1.identificar_outliers(),
    'outliers_numerica_2': num_2.identificar_outliers(),

    'benchmark': benchmarking(num_1.validos),
}

with open('../resultados/analisis_numpy.json', 'w', encoding='utf-8') as f:
    json.dump(resul, f, indent=2, ensure_ascii=False)
print('Resultado generado en la carpeta de resultados como analisis_numpy.json')

