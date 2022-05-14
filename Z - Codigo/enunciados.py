from posixpath import split
#a1
def redondeo_hora(cadena: str):
    return cadena.split(':')[0]

print(redondeo_hora('12:48'))

#a2
def rango_edad(cadena: str):
    datos = cadena.split(' ')
    return tuple((-1,-1)) if len(datos) < 2 else \
           ( tuple((int(datos[1]),int(datos[3]))) if len(datos) > 4 \
           else tuple((int(datos[2]),100)) )

for c in  ['DE 25 A 29 AÑOS', 'DESCONOCIDA', 'MAYOR DE 74 AÑOS']:
    print(c, " -> ", rango_edad(c))

#a3
def lesividad(cadena: str):
    return int(cadena) if cadena else 0

for c in  ['01', '02', '14', '', '77']:
    print(c, " -> ", lesividad(c))

'''
La cadena de entrada: 
2020S000073;01/01/2020;18:48;AVDA. PIO XII;81;CHAMARTÍN;Atropello a persona;Despejado;Turismo;Conductor;DE 55 A 59 AÑOS;Hombre;14;;

Piezas: 
['2020S000073', '01/01/2020', '18:48', 'AVDA. PIO XII', '81', 'CHAMARTÍN', 'Atropello a persona', 'Despejado', 'Turismo', 'Conductor', 'DE 55 A 59 AÑOS', 'Hombre', '14', '', '']

Distrito: 
CHAMARTÍN

La hora, sin y con redondeo: 
18:48
18

La edad, tal como viene y en  su rango: 
DE 55 A 59 AÑOS
(55, 59)
'''
def presentar_operaciones_basicas(cadena: str):
    print("La cadena de entrada: ")
    print(cadena, end="\n\n")

    print("Piezas: ")
    lista = cadena.split(';')
    print(lista, end="\n\n")

    print("Distrito: ")
    print(lista[5], end="\n\n")

    print("La hora, sin y con redondeo: ")
    print(lista[2])
    print(redondeo_hora(lista[2]), end="\n\n")

    print("La edad, tal como viene y en  su rango: ")
    print(lista[10])
    print(rango_edad(lista[10]))

       
linea_9 = "2020S000073;01/01/2020;18:48;AVDA. PIO XII;81;CHAMARTÍN;Atropello a persona;Despejado;Turismo;Conductor;DE 55 A 59 AÑOS;Hombre;14;;"
presentar_operaciones_basicas(linea_9)

# [18, 'CHAMARTÍN', 'Despejado', (55, 59), 14]
def extraer_datos(cadena: str):
    lista = cadena.split(';')
    return [redondeo_hora(lista[2]),lista[5],lista[7],\
            rango_edad(lista[10]),lista[12]]

print(len(linea_9.split(";")))
print(extraer_datos(linea_9))