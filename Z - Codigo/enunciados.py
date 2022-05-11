import string

def redondeo_hora(str: string):
    return str.split(':')[0]

print(redondeo_hora('12:48'))