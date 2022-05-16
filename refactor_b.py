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

def cargar_datos(fichero: str):
    with open(fichero,'rb') as file:
        total_filas = len(file.readlines())
    return cargar_lineas("2020_Accidentalidad.csv",1, total_filas)

datos_lista = cargar_datos("2020_Accidentalidad.csv")

# for linea in datos_lista:
#     print(linea)   

def totales(lista: list):
    diccionario = dict()

    for fila in lista:
        if fila[3] not in diccionario:
            diccionario[fila[3]] = 1
        else:
            diccionario[fila[3]] += 1
    return diccionario

# Prueba de funcionamiento:

total_accidentes_por_edades = totales(datos_lista)

# for k, e in total_accidentes_por_edades.items():
#     print(k, e)

def totales_mortales(lista: list):
    diccionario = dict()
    mortales = [4] # solo hay 1 código para lesividad mortal

    for fila in lista:
        if fila[3] not in diccionario:
            valor = [1,0]
            if fila[4] in mortales:
                valor[1] = 1
            diccionario[fila[3]] = tuple(valor)
        else:
            valor = list(diccionario.get(fila[3]) )
            valor[0] += 1
            if fila[4] in mortales:
                valor[1] += 1
            diccionario[fila[3]] = tuple(valor)
    return diccionario.items()

# Prueba de funcionamiento:

total_accidentes_y_muertes_por_edades = totales_mortales(datos_lista)

# for edades, dos_totales in total_accidentes_y_muertes_por_edades:
#     print(edades, dos_totales)
    
# print()

# Total accidentes mortales / 1000 accidentes, por rangos de edad:

tasa_accidentes_mortales_por_mil = [(k, m*1000/n) for k, (n, m) in total_accidentes_y_muertes_por_edades]
                                    
# for k_tasa  in tasa_accidentes_mortales_por_mil:
#     print(k_tasa)  

# 0 <= datos_lista['hora'] <= 23
# por tanto, los impares se agrupan con el par anterior
def totales_mortales_por_horario(lista: list):
    diccionario = dict()
    lesividad_mortal = [4]

    for dato in lista:
        aux = int(dato[0])
        if aux % 2: # 0->Par->false. Aqui entra si es impar
            aux -= 1

        if aux not in diccionario:
            valor = [1,0]
            if dato[4] in lesividad_mortal:
                valor[1] = 1
        else:
            valor = diccionario.get(aux)
            valor[0] += 1
            if dato[4] in lesividad_mortal:
                valor[1] += 1        
        diccionario[aux] = valor

    mortales_hora = diccionario.items()
    mortales_hora = [ tuple([ accidente[0], (accidente[1][1]/accidente[1][0])*1000 ]) for accidente in mortales_hora]

    return sorted(mortales_hora, key=lambda x: x[0])

def emparejar_abcisas(lista: list):
    return [ tuple([str(tuple([acc[0],acc[0]+2])),acc[1]]) for acc in lista]


tasas_accidentes_y_muertes_por_horario = totales_mortales_por_horario(datos_lista)

print(tasas_accidentes_y_muertes_por_horario)

print()

datos_para_grafica = emparejar_abcisas(tasas_accidentes_y_muertes_por_horario)

print(datos_para_grafica)

# [(0, 1.9230769230769231), (2, 4.178272980501393), (4, 1.949317738791423), (6, 0.8635578583765112), 
# (8, 1.1415525114155252), (10, 1.5337423312883436), (12, 0.8234971177600878), (14, 1.112099644128114),
#  (16, 0.5351886540005352), (18, 0.4287245444801715), (20, 1.1999040076793857), (22, 1.187178472497032)]

# [('(0, 2)', 1.9230769230769231), ('(2, 4)', 4.178272980501393), ('(4, 6)', 1.949317738791423), 
# ('(6, 8)', 0.8635578583765112), ('(8, 10)', 1.1415525114155252), ('(10, 12)', 1.5337423312883436), 
# ('(12, 14)', 0.8234971177600878), ('(14, 16)', 1.112099644128114), ('(16, 18)', 0.5351886540005352), 
# ('(18, 20)', 0.4287245444801715), ('(20, 22)', 1.1999040076793857), ('(22, 24)', 1.187178472497032)]