import pandas as pd

def cargar_cabecera(fichero: str):
   df = pd.read_csv(fichero, encoding='iso-8859-1', nrows=0, sep=';')
   # df.rename(columns={'Unnamed: 13':'', 'Unnamed: 14':''},inplace=True)
   # la opcion anterior para columnas fijas. 
   # la nueva para cualquiera (list comprehension)

   return ['' if 'Unname' in col else col for col in df.columns ]
            
cabecera = cargar_cabecera("2020_Accidentalidad.csv")
print(cabecera)
