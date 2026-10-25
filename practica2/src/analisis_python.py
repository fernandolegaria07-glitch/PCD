import json

class Categorica:

    # Se considera que los datos ya estan limpios una vez ya entran en el objeto
    def __init__(self, nombre, data, index):
        self.nombre = nombre
        self.data = data
        self.index = index
        self.conteo = {}
        for value in data:
            self.conteo[value] = self.conteo.get(value, 0) + 1 

    # Calculo para la seccion de valores unicos por la columna
    def valores_unicos(self):
        resul = {}
        resul['columna'] = self.nombre
        val_unicos = set(self.data)
        resul['n_valores_unicos'] = len(val_unicos)
        resul['valores'] = list(val_unicos)
        return resul

    def cat_mas_frec(self):
        resul = {}
        max_val = 0
        max_nom = ''
        for val in self.conteo.items():
            if max_val < val[1]:
                max_val = val[1]
                max_nom = val[0]
        resul['valor'] = max_nom
        resul['conteo'] = max_val
        return resul
    
    def top_3_cat(self):
        resul = []
        sort_conteo = {k: v for k, v in sorted(self.conteo.items(), key=lambda item: item[1])}
        items_conteo = sort_conteo.items()
        for tup in list(items_conteo)[len(items_conteo)-3:]:
            sm_resul = {}
            sm_resul['valor'] = tup[0]
            sm_resul['conteo'] = tup[1]
            resul.append(sm_resul)
        return resul

class Numerica:

    def __init__(self, nombre, data, index):
        self.nombre = nombre
        self.index = index

        self.data = list(filter(lambda x : x is not None, data))

    def estadisticas(self):
        return {
            'columna': self.nombre,
            'n_valores_validos': len(self.data),
            'minimo': min(self.data),
            'maximo': max(self.data),
            'promedio': round(sum(self.data) / len(self.data), 2),
            'mediana': sorted(self.data)[int((len(self.data) - 1) / 2)]
        }

def a_float(texto):
    try:
        return float(texto)
    except (ValueError, TypeError):
        return -1



dir_archivo = '../../datos/reportes_transito-ruido_100.csv'

with open(dir_archivo, 'r') as archivo:
    cols = archivo.readline().strip().split('|')
    data = []
    for i in archivo:
        data.append(i.strip().split('|'))
    for x in range(len(cols)):
        if cols[x] == 'zona':
            data_col_cat = []
            for row in data:
                if row[x].strip() != '':
                    data_col_cat.append(row[x].strip().title())
            col_cat = Categorica(cols[x], data_col_cat, x)
        if cols[x] == 'vehiculos_afectados':
            data_num_1 = Numerica(cols[x], filter(lambda x: x > 0, map(a_float,[row[x] for row in data])), x)
        if cols[x] == 'duracion_incidente_min':
            data_num_2 = Numerica(cols[x], filter(lambda x: x > 0, map(a_float,[row[x] for row in data])), x)
    
    final_json = {
        "archivo": "reportes-transito-ruido.csv",
        "pareja": "Hugo Hernandez - Fernando Legaria",
        "seed": 55,

      "valores_unicos_categorica": col_cat.valores_unicos(),

      "conteo_por_categoria": col_cat.conteo,

      "categoria_mas_frecuente": col_cat.cat_mas_frec(),

      "top_3_categorias": col_cat.top_3_cat(),

      "estadisticas_numerica_1": data_num_1.estadisticas(),
      "estadisticas_numerica_2": data_num_2.estadisticas(),

    }


    with open('../resultados/analisis_python.json', 'w', encoding='utf-8') as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print('Resultado generado en la carpeta de resultados como analisis_python.json')
