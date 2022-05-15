import pandas as pd

def cargar_cabecera(fichero: str):
   df = pd.read_csv(fichero, encoding='iso-8859-1', nrows=0, sep=';')
   # df.rename(columns={'Unnamed: 13':'', 'Unnamed: 14':''},inplace=True)
   # la opcion anterior para columnas fijas. 
   # la nueva para cualquiera (list comprehension)

   return ['' if 'Unname' in col else col for col in df.columns ]
            
cabecera = cargar_cabecera("2020_Accidentalidad.csv")
#print(cabecera)
###############

def rango_edad(cadena: str):
    datos = cadena.split(' ')
    return tuple((-1,-1)) if len(datos) < 2 else \
           ( tuple((int(datos[1]),int(datos[3]))) if len(datos) > 4 \
           else tuple((int(datos[2])+1,100)) )

def redondeo_hora(cadena: str):
    return int(cadena.split(':')[0])           

def lesividad(cadena: str):
    return int(cadena) if cadena else 0
# 
def cargar_lineas(fichero: str, inicio=1, fin=10):
    df = pd.read_csv(fichero, encoding='iso-8859-1', nrows=fin, sep=';')
    df['HORA'] = df['HORA'].apply(redondeo_hora)
    df['RANGO DE EDAD'] = df['RANGO DE EDAD'].apply(rango_edad)
    
    # quitamos los NaN
    df['LESIVIDAD*'] = df['LESIVIDAD*'] .fillna(0)
    df['ESTADO METEREOLÓGICO'] = df['ESTADO METEREOLÓGICO'] .fillna('')
    df['LESIVIDAD*'] = df['LESIVIDAD*'].apply(lesividad)

    aux = df.loc[inicio-1:fin-1,['HORA','DISTRITO','ESTADO METEREOLÓGICO','RANGO DE EDAD','LESIVIDAD*']].values.tolist()
    return aux

lineas_lista = cargar_lineas("2020_Accidentalidad.csv", 1, 4)

#for linea in lineas_lista:
# print(linea)
    

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

# Si no decimos qué líneas nos interesa, se cargarán las diez primeras.
# (Esto puede hacerse con dos parámetros por defecto.)

print()

lineas_lista = cargar_lineas("2020_Accidentalidad.csv")

#for linea in lineas_lista:
# print(linea)

def cargar_datos(fichero: str):
    with open(fichero,'rb') as file:
        total_filas = len(file.readlines())
    return cargar_lineas("2020_Accidentalidad.csv",1, total_filas)

datos_lista = cargar_datos("2020_Accidentalidad.csv")

'''for linea in full_data:
    print(linea)'''


### apartado C
# realestate.groupby(['zip','baths']).size().unstack()

def totales(lista: list):
    df = pd.DataFrame(lista, columns=['hora','distrito','clima','rango','lesividad'])
    print(df)
    pass

totales(datos_lista)

'''total_accidentes_por_edades = totales(datos_lista)

for k, e in total_accidentes_por_edades.items():
    print(k, e)'''