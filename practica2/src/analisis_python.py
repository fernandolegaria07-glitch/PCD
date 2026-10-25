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
        resul['valores'] = val_unicos
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
    print(col_cat.top_3_cat())
    
