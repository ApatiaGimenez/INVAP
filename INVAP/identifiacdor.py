
import pandas as pd


# Lee los archivos CSV
df_permitidos = pd.read_csv('Codigos_disponibles.csv')
df_encuestas = pd.read_csv('Codigos_encuestas.csv')

# Convierte las columnas a conjuntos para facilitar la comparación
codigos_permitidos = set(df_permitidos['Codigo'])
codigos_encuestas = set(df_encuestas['Codigo'])

# Encuentra los códigos de encuestas que no están en los códigos permitidos
codigos_no_permitidos = codigos_encuestas - codigos_permitidos

# Imprime los códigos no permitidos
print("Códigos no permitidos:")
for codigo in codigos_no_permitidos:
    print(codigo)

# Calcula el número de encuestas que quedaron fuera
num_encuestas_fuera = len(codigos_no_permitidos)
print("Número de encuestas que quedaron fuera:", num_encuestas_fuera)