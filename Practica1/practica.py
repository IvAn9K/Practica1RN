import csv
import random
 
lista = []

#devuelve el maximo de la columna por parametro
def get_max_by_col(li, col):
    return max(li, key=lambda x: x[col])[col]

#devuelve el minimo de la columna por parametro
def get_min_by_col(li, col):
    return min(li, key=lambda x: x[col])[col]

with open('/home/ivan9k/Escritorio/uni/redesNeuronas/california_housing.csv', newline='') as File:  
    reader = csv.DictReader(File)
    for row in reader:
        lista.append(list((float(row['longitude']), float(row['latitude']), float(row['housing_median_age']), 
        float(row['total_rooms']), float(row['total_bedrooms']), float(row['population']), float(row['households']), 
        float(row['median_income']), float(row['median_house_value']))))

maximos = [get_max_by_col(lista, 0), get_max_by_col(lista, 1), get_max_by_col(lista, 2), get_max_by_col(lista, 3),
            get_max_by_col(lista, 4), get_max_by_col(lista, 5), get_max_by_col(lista, 6), get_max_by_col(lista, 7), get_max_by_col(lista, 8)]

minimos = [get_min_by_col(lista, 0), get_min_by_col(lista, 1), get_min_by_col(lista, 2), get_min_by_col(lista, 3), get_min_by_col(lista, 4),
            get_min_by_col(lista, 5), get_min_by_col(lista, 6), get_min_by_col(lista, 7), get_min_by_col(lista, 8)]

for i in range (0, len (lista)):
    for j in range (0, 9):
        lista [i][j] = (lista[i][j] - minimos[j]) / (maximos[j] - minimos[j])

random.shuffle(lista)

entrenamiento = lista[:int(0.6*len(lista))]

test = lista[int(0.6*len(lista)): int(0.8*len(lista))]
  
validacion = lista[int(0.8*len(lista)):]
    
Conjunto1 = open('datosEntrenamiento.csv', 'w')

with Conjunto1:
    writer = csv.writer(Conjunto1)

    for row in entrenamiento:
        writer.writerow(row)

Conjunto1.close()

Conjunto2 = open('datosTest.csv', 'w')

with Conjunto2:
    writer = csv.writer(Conjunto2)

    for row in test:
        writer.writerow(row)

Conjunto2.close()

Conjunto3 = open('datosValidacion.csv', 'w')

with Conjunto3:
    writer = csv.writer(Conjunto3)

    for row in validacion:
        writer.writerow(row)

Conjunto3.close()
