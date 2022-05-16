import csv
import itertools
from apartado_A import redondeo_hora,rango_edad,lesividad

#    return ['' if 'Unname' in col else col for col in df.columns ]
def cargar_cabecera(fichero: str):
    with open(fichero, encoding='iso-8859-1', newline='') as archivo:
        cabecera = archivo.readline().strip()
    return cabecera.split(sep=';')
        

cabecera = cargar_cabecera("2020_Accidentalidad.csv")
#print(cabecera)

def cargar_lineas(fichero: str, inicio=1, fin=10):

    with open(fichero, encoding='iso-8859-1', newline='') as archivo:
        accidentalidad = csv.DictReader(archivo,delimiter=';')
        
        lista = [ [
                redondeo_hora(fila['HORA']), \
                fila['DISTRITO'], \
                fila['ESTADO METEREOLÓGICO'], \
                rango_edad(fila['RANGO DE EDAD']), \
                lesividad(fila['LESIVIDAD*'])] \
                for fila in itertools.islice(accidentalidad, inicio-1, fin)]

        return lista

    
    # archivo.seek(inicio)
    # data = fin.read(fin - inicio)
    # (next(itertools.islice(csv.reader(archivo), inicio, fin)))

    # df = pd.read_csv(fichero, encoding='iso-8859-1', nrows=fin, sep=';')
    # df['HORA'] = df['HORA'].apply(redondeo_hora)
    # df['RANGO DE EDAD'] = df['RANGO DE EDAD'].apply(rango_edad)
    
    # # quitamos los NaN
    # df['LESIVIDAD*'] = df['LESIVIDAD*'] .fillna(0)
    # df['ESTADO METEREOLÓGICO'] = df['ESTADO METEREOLÓGICO'] .fillna('')
    # df['LESIVIDAD*'] = df['LESIVIDAD*'].apply(lesividad)

    # aux = df.loc[inicio-1:fin-1,['HORA','DISTRITO','ESTADO METEREOLÓGICO','RANGO DE EDAD','LESIVIDAD*']].values.tolist()

lineas_lista = cargar_lineas("2020_Accidentalidad.csv", 1, 4)

for linea in lineas_lista:
    print(linea)

# [23, 'RETIRO', 'Despejado', (25, 29), 0]
# [22, 'MONCLOA-ARAVACA', 'Despejado', (21, 24), 6]
# [20, 'FUENCARRAL-EL PARDO', 'Despejado', (45, 49), 14]
# [20, 'FUENCARRAL-EL PARDO', 'Despejado', (25, 29), 7]

print()

lineas_lista = cargar_lineas("2020_Accidentalidad.csv")

for linea in lineas_lista:
    print(linea)

# [23, 'RETIRO', 'Despejado', (25, 29), 0]
# [22, 'MONCLOA-ARAVACA', 'Despejado', (21, 24), 6]
# [20, 'FUENCARRAL-EL PARDO', 'Despejado', (45, 49), 14]
# [20, 'FUENCARRAL-EL PARDO', 'Despejado', (25, 29), 7]
# [19, 'CENTRO', 'Despejado', (-1, -1), 0]
# [19, 'CARABANCHEL', 'Despejado', (-1, -1), 14]
# [19, 'CARABANCHEL', 'Despejado', (21, 24), 2]
# [18, 'CHAMARTÍN', 'Despejado', (55, 59), 14]
# [18, 'CHAMARTÍN', 'Despejado', (18, 20), 7]
# [18, 'ARGANZUELA', '', (55, 59), 14]