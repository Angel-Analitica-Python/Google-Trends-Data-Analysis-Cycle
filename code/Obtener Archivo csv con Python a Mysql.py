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

import csv

with open('BigData.csv', mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    cursor.execute("""
    SELECT INTERESADOS.ID_INTERESADOS, INTERESADOS.ID_PAIS, INTERESADOS.ID_REGION, INTERESADOS.ID_TEMA, PAIS.PAIS, REGION.REGION, INTERES.TEMA
    FROM INTERESADOS
    INNER JOIN PAIS ON INTERESADOS.ID_PAIS = PAIS.ID_PAIS
    INNER JOIN REGION ON INTERESADOS.ID_REGION = REGION.ID_REGION
    INNER JOIN INTERES ON INTERESADOS.ID_TEMA = INTERES.ID_TEMA;
    """)

    resultados = cursor.fetchall()

    # Escribir encabezados de columnas en el archivo CSV
    encabezados = ['ID_INTERESADOS', 'ID_PAIS', 'ID_REGION','ID_TEMA','PAIS','REGION','TEMA']
    escritor_csv.writerow(encabezados)

    # Escribir los resultados de la consulta en el archivo CSV
    for resultado in resultados:
        escritor_csv.writerow(resultado)

archivo_csv.close()

# Se cierra el cursor y la conexión
cursor.close()
conexion.close()

# Programa Realizado Por: Angel Alejandro Galaviz Rivera 2004124