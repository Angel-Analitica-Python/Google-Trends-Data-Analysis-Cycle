import mysql.connector

# Se crea una conexión a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="FACPYA_2004124",
  database="visualización_de_datos_y_desarrollo_de_escritorio"
)

# Se crea un cursor para realizar operaciones en la base de datos
cursor = conexion.cursor()

# Se ejecuta una consulta
cursor.execute("""
SELECT INTERESADOS.ID_INTERESADOS, INTERESADOS.ID_PAIS, INTERESADOS.ID_REGION, INTERESADOS.ID_TEMA, PAIS.PAIS, REGION.REGION, INTERES.TEMA
FROM INTERESADOS
INNER JOIN PAIS ON INTERESADOS.ID_PAIS = PAIS.ID_PAIS
INNER JOIN REGION ON INTERESADOS.ID_REGION = REGION.ID_REGION
INNER JOIN INTERES ON INTERESADOS.ID_TEMA = INTERES.ID_TEMA;
""")

# Se obtienen los resultados
resultados = cursor.fetchall()

for resultado in resultados:
    columna1, columna2, columna3 ,columna4 ,columna5 ,columna6 ,columna7= resultado
    print(columna1, columna2, columna3 ,columna4 ,columna5 ,columna6 ,columna7)

# Se cierra el cursor y la conexión
cursor.close()
conexion.close()

# Programa Realizado por:Angel Alejandro Galaviz Rivera 2004124