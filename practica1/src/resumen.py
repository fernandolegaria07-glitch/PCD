with open('../../datos/reportes_transito-ruido_100.csv', 'r') as file: 
    data = []
    line = file.readline()
    filas = -1
    columnas = len(line.strip().split('|'))

    while line:
        data.append(line.strip().split('|'))
        line = file.readline()
        filas += 1
    print(data[1])
    file.close()
