
# Codigo de procesamiento de datos python 
import pandas as pd

# Cargar datos desde un archivo CSV
data = pd.read_csv('datos.csv')

# Limpiar datos: eliminar filas con valores faltantes
data_limpia = data.dropna()

# Crear una nueva columna basada en datos existentes
data_limpia['nueva_columna'] = data_limpia['columna_existente'] * 2

# Filtrar datos: seleccionar filas que cumplan una condición
datos_filtrados = data_limpia[data_limpia['columna_existente'] > 10]
