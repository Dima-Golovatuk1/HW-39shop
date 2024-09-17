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
        print(products_list)
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
        return product

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def put_feedback(name, feedback, id):
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
            """INSERT INTO feedback (user_name, feedback, id_product) VALUES (%s, %s, %s)""",
            (name, feedback, id)
        )
        connection.commit()

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def get_feedback():
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
            """SELECT * FROM feedback"""
        )
        feedback_list = cursor.fetchall()
        return feedback_list

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def register_user(name, email, psw):
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
            """INSERT INTO users (name, email, password) VALUES (%s, %s, %s)""",
            (name, email, psw)
        )
        connection.commit()

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def get_users():
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
            """SELECT * FROM users"""
        )
        user_list = cursor.fetchall()
        return user_list

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def get_user(self, user_id):
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
            """SELECT * FROM users WHERE id = %s""", (user_id,)
        )
        user = cursor.fetchone()
        return user

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')


def get_users_by_email(email):
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
            cursor.execute("""SELECT * FROM users WHERE email = %s""", (email))
        )
        user_info = cursor.fetchone()
        print(user_info)
        return user_info

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')



get_users_by_email("dimagolovatuk80@gmail.com")