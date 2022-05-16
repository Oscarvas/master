import csv
import itertools
import readline

#    return ['' if 'Unname' in col else col for col in df.columns ]
# reader = csv.DictReader(archivo)
def cargar_cabecera(fichero: str):
    with open(fichero, encoding='iso-8859-1', newline='') as archivo:
        cabecera = archivo.readline().strip()
    return cabecera.split(sep=';')
        

cabecera = cargar_cabecera("2020_Accidentalidad.csv")
#print(cabecera)

def cargar_lineas(fichero: str, inicio=1, fin=10):

    with open(fichero, encoding='iso-8859-1', newline='') as archivo:
        reader = csv.DictReader(itertools.islice(archivo, inicio-1, fin+1),delimiter=';')
        
        for lines in reader:
            print(lines)

    return reader

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