import pandas as pd

def cargar_cabecera(fichero: str):
   df = pd.read_csv(fichero, encoding='iso-8859-1', nrows=0, sep=';')
   # df.rename(columns={'Unnamed: 13':'', 'Unnamed: 14':''},inplace=True)
   # la opcion anterior para columnas fijas. 
   # la nueva para cualquiera (list comprehension)

   return ['' if 'Unname' in col else col for col in df.columns ]
            
cabecera = cargar_cabecera("2020_Accidentalidad.csv")
print(cabecera)
###############


def cargar_lineas(fichero: str, inicio=1, fin=10):
    df = pd.read_csv(fichero, encoding='iso-8859-1', nrows=fin, sep=';')
    return df[['HORA','DISTRITO','ESTADO METEREOLÓGICO','RANGO DE EDAD','LESIVIDAD*']][inicio:fin]


'''
[23, 'RETIRO', 'Despejado', (25, 29), 0]
[22, 'MONCLOA-ARAVACA', 'Despejado', (21, 24), 6]
[20, 'FUENCARRAL-EL PARDO', 'Despejado', (45, 49), 14]
[20, 'FUENCARRAL-EL PARDO', 'Despejado', (25, 29), 7]
hora2-distrito5-estado7-rango10-lesiv12
2020S000057;01/01/2020;23:15;AVDA. CIUDAD DE BARCELONA / CALL. DOCTOR ESQUERDO;-;RETIRO;Choque contra obstáculo fijo;Despejado;Turismo;Conductor;DE 25 A 29 AÑOS;Hombre;;;
2020S000038;01/01/2020;22:35;CALL. VALLE DE TORANZO / CALL. SIERRA DE PAJAREJO;-;MONCLOA-ARAVACA;Caída;Despejado;Ciclomotor;Conductor;DE 21 A 24 AÑOS;Mujer;06;;
2020S000060;01/01/2020;20:15;GTA. MARIANO SALVADOR MAELLA;1;FUENCARRAL-EL PARDO;Caída;Despejado;Turismo;Conductor;DE 45 A 49 AÑOS;Hombre;14;;
2020S000060;01/01/2020;20:15;GTA. MARIANO SALVADOR MAELLA;1;FUENCARRAL-EL PARDO;Caída;Despejado;Motocicleta hasta 125cc;Conductor;DE 25 A 29 AÑOS;Hombre;07;;


[23, 'RETIRO', 'Despejado', (25, 29), 0]
[22, 'MONCLOA-ARAVACA', 'Despejado', (21, 24), 6]
[20, 'FUENCARRAL-EL PARDO', 'Despejado', (45, 49), 14]
[20, 'FUENCARRAL-EL PARDO', 'Despejado', (25, 29), 7]
[19, 'CENTRO', 'Despejado', (-1, -1), 0]
[19, 'CARABANCHEL', 'Despejado', (-1, -1), 14]
[19, 'CARABANCHEL', 'Despejado', (21, 24), 2]
[18, 'CHAMARTÍN', 'Despejado', (55, 59), 14]
[18, 'CHAMARTÍN', 'Despejado', (18, 20), 7]
[18, 'ARGANZUELA', '', (55, 59), 14]
'''
lineas_lista = cargar_lineas("2020_Accidentalidad.csv", 1, 4)

for linea in lineas_lista:
    print(linea)
    
# Si no decimos qué líneas nos interesa, se cargarán las diez primeras.
# (Esto puede hacerse con dos parámetros por defecto.)

print()

lineas_lista = cargar_lineas("2020_Accidentalidad.csv")

for linea in lineas_lista:
    print(linea)