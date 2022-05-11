import string

def redondeo_hora(str: string):
    return str.split(':')[0]

print(redondeo_hora('12:48'))

def lesividad(str: string):
    return int(str) if str else 0

for c in  ['01', '02', '14', '', '77']:
    print(c, " -> ", lesividad(c))