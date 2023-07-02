import psycopg2
from psycopg2 import Error

name = ''
quantity = 0
photo = ''
price = 0
a = 1

try:
    connection = psycopg2.connect(user="postgres",
                                  password="MiFi",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="bot_catalog")

    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM catalog_fire"

    cursor.execute(postgreSQL_select_Query)
    catalog_pos = cursor.fetchmany(a)
    for pos in catalog_pos:
        name = pos[0]
        quantity = pos[1]
        photo = pos[2]
        price = pos[3]
    print(name, quantity, photo, price)   
  
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")