import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="MiFi",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="db_for_bot")
    cursor = connection.cursor()
    request_to_bd = ''' INSERT INTO result
                        SELECT questions.quest_name, answers.ans_name 
                        FROM questions
                        FULL JOIN answers
                        ON answers.id_ans = questions.id_quest 
                        WHERE (answers.ans_product = questions.quest_product) or 
                        (answers.ans_order = questions.quest_order) or 
                        (answers.ans_sale = questions.quest_sale) or
                        (answers.ans_recom = questions.quest_recom) or
                        (answers.ans_another = questions.quest_another);'''
    cursor.execute(request_to_bd)
    connection.commit()
    print("Запрос успешно создан в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")