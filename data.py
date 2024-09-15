import psycopg2
import random


def get_products():
    host = '127.0.0.1'
    user = 'postgres'
    password = '08112007'
    db_name = 'HW-39shop'


    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database = db_name
        )

        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM products"""
        )
        products_list = cursor.fetchall()
        return products_list

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def get__one__products(id):
    host = '127.0.0.1'
    user = 'postgres'
    password = '08112007'
    db_name = 'HW-39shop'

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM products LIMIT 1 OFFSET %s""", (id,)
        )
        product = cursor.fetchall()
        print(product)
        return product

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')


get__one__products(6)
