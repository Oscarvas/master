import pandas as pd

def cargar_cabecera(fichero: str):
    pd.read_csv('../'+fichero, encoding='latin1')[0]
            
cabecera = cargar_cabecera("2020_Accidentalidad.csv")
print(cabecera)
