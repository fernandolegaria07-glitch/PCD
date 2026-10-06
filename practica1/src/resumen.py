file = open('../../datos/reportes_transito-ruido_100.csv', 'r')
data = []
line = file.readline()
while line:
    data.append(line.strip().split('|'))
    line = file.readline()
print(data[1])
file.close()
