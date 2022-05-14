import csv

def cargar_cabecera(fichero: str):
    with open("./Z_Tarea/"+fichero) as excel:
        reader = csv.DictReader(excel)
        count = 0

        for row in reader:
            print (row)
            if count > 3:
                break
            count += 1    
            
cabecera = cargar_cabecera("2020_Accidentalidad.csv")
print(cabecera)
