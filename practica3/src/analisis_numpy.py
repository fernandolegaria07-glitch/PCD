import numpy as np

def a_float(texto):
    try:
        return float(texto.strip())
    except (ValueError, AttributeError):
        return np.nan

def extraer_datos(dir_archivo):
    with open(dir_archivo, 'r') as f:
        lineas = f.read().strip().split('\n')
    cabecera = lineas[0].split('|')
    data = [linea.split('|') for linea in lineas[1:]]
    return cabecera, data


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
            'minimo': np.min(self.validos),
            'maximo': np.max(self.validos),
            'mediana': np.percentile(self.validos, 50),
            'percentil_25': np.percentile(self.validos, 25),
            'percentil_75': np.percentile(self.validos, 75),
        }

    def identificar_outliers(self, k=3):
        media = self.media
        std = self.std
        inferior = media - k * std
        superior = media + k * std
        outliers = self.validos[(self.validos < inferior) & (self.validos > superior)]
        return {
            'metodo': 'desviacion_estandar_3',
            'limite_inferior': inferior,
            'limite_superior': superior,
            'n_outliers': len(outliers),
            'porcentaje': len(outliers) / len(self.validos),
            'outliers-minimo': np.min(outliers),
            'outliers-maximo': np.max(outliers),
        }


nombre_archivo = 'reportes_transito-ruido_100000.csv'
dir_archivo = f'../../datos/{nombre_archivo}'
seed = 55

cabecera, data = extraer_datos(dir_archivo)
nombre_num_1, nombre_num_2 = 'vehiculos_afectados', 'duracion_incidente_min'
num_1 = Numerica(index=cabecera.index(nombre_num_1), nombre=nombre_num_1, raw=data)
num_2 = Numerica(index=cabecera.index(nombre_num_2), nombre=nombre_num_2, raw=data)

resul = {
    'archivo': nombre_archivo,
    'pareja': 'Hugo Hernández - Fernando Legaria',
    'seed': seed,

    'numerica_1' : num_1.calcular_estadisticas(),
    'numerica_2' : num_2.calcular_estadisticas(),

    'outliers_numerica_1': num_1.identificar_outliers(),
    'outliers_numerica_2': num_2.identificar_outliers()
}