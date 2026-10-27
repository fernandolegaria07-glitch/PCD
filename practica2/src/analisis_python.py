import json

class Categorica:

    # Se considera que los datos ya estan limpios una vez ya entran en el objeto
    def __init__(self, nombre, data):
        self.nombre = nombre
        self.data = data
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
        items_ordenados = sorted(self.conteo.items(), key=lambda item: (-item[1], item[0]))
        for tup in items_ordenados[:3]:
            sm_resul = {}
            sm_resul['valor'] = tup[0]
            sm_resul['conteo'] = tup[1]
            resul.append(sm_resul)
        return resul

class Numerica:

    def __init__(self, nombre, data):
        self.nombre = nombre

        self.data = list(filter(lambda x : x is not None, data))

    def estadisticas(self):
        sort_data = sorted(self.data)
        index = int((len(self.data)) / 2)
        if(len(self.data) % 2 == 1):
            mediana = sort_data[index]
        else:
            md1 = sort_data[index]
            md2 = sort_data[index-1]
            mediana = (md1 + md2) / 2

        return {
            'columna': self.nombre,
            'n_valores_validos': len(self.data),
            'minimo': min(self.data),
            'maximo': max(self.data),
            'promedio': round(sum(self.data) / len(self.data), 2),
            'mediana': round(mediana,2)
        }

def a_float(texto):
    try:
        return float(texto)
    except (ValueError, TypeError):
        return -1

def promedio_por_categoria(data, col_num, col_cat):
    dir_sumas = {}
    dir_conteo = {}
    dir_resul = {}
    for fila in data:
        try:
            if fila[col_num].strip() == '' or fila[col_cat].strip() == '':
                continue
            num = float(fila[col_num])
            if num < 0:
                continue
            cat_act = fila[col_cat].strip()
            dir_conteo[cat_act] = dir_conteo.get(cat_act, 0) + 1
            dir_sumas[cat_act] = dir_sumas.get(cat_act, 0) + float(num)
        except:
            continue
    for x, v in dir_conteo.items():
        dir_resul[x] = round(dir_sumas[x] / v,2)
    return dir_resul

def filtrado_percentil(col_num):
    n = len(col_num)
    sort_num = sorted(col_num)
    perMax = sort_num[int(0.9 * n)]
    final = list(filter(lambda x: x > perMax, sort_num))
    # Retorna umbral / n registros que cumplen / porcentaje
    return (perMax, len(final), round((len(final) / len(col_num)) * 100,2))

dir_archivo = '../../datos/reportes_transito-ruido_100.csv'

with open(dir_archivo, 'r') as archivo:
    cols = archivo.readline().strip().split('|')
    data = []
    for i in archivo:
        valores = i.strip().split('|')
        data.append(dict(zip(cols, valores)))
    for col in cols:
        if col == 'zona':
            data_col_cat = []
            for row in data:
                if row[col].strip() != '':
                    data_col_cat.append(row[col].strip())
            col_cat = Categorica(col, data_col_cat)
        if col == 'duracion_incidente_min':
            data_num_1 = Numerica(col, map(a_float, filter(lambda x : a_float(x) >= 0, [row[col] for row in data])))
        if col == 'vehiculos_afectados':
            data_num_2 = Numerica(col, map(a_float, filter(lambda x : a_float(x) >= 0, [row[col] for row in data])))
    
    filt_umb, filt_n, filt_per = filtrado_percentil(data_num_1.data)
    final_json = {
        "archivo": "reportes_transito-ruido.csv",
        "pareja": "Hugo Hernandez - Fernando Legaria",
        "seed": 55,

      "valores_unicos_categorica": col_cat.valores_unicos(),

      "conteo_por_categoria": col_cat.conteo,

      "categoria_mas_frecuente": col_cat.cat_mas_frec(),

      "top_3_categorias": col_cat.top_3_cat(),

      "estadisticas_numerica_1": data_num_1.estadisticas(),
      "estadisticas_numerica_2": data_num_2.estadisticas(),
      "promedio_por_categoria": promedio_por_categoria(data, data_num_1.nombre, col_cat.nombre),
      
      "filtrado": {
            "condicion": f"{data_num_1.nombre} > {filt_umb}",
            "umbral_usado": filt_umb,
            "n_registros_que_cumplen": filt_n,
            "porcentaje": filt_per
        }
    }


    with open('../resultados/analisis_python.json', 'w', encoding='utf-8') as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print('Resultado generado en la carpeta de resultados como analisis_python.json')

