import psycopg2
import random
import logging
logging.basicConfig(level=logging.INFO)


def get_products():
    try:
        connection = psycopg2.connect(
            host='127.0.0.1',
            user='postgres',
            password='08112007',
            database='HW-39shop'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        products_list = cursor.fetchall()
        return products_list
    except Exception as _ex:
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


def get_max_id_products():
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
            """SELECT MAX(id) FROM products;"""
        )

        max_id_product = cursor.fetchone()[0]  # Получаем одно значение
        return max_id_product

    except Exception as _ex:
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


def get__one__products(id):
    if id < 0:
        raise ValueError("ID cannot be negative")
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
        logging.info(f"Fetching product with ID {id}")
        cursor.execute("""SELECT * FROM products WHERE id = %s""", (id,))
        product = cursor.fetchone()
        return product

    except Exception as _ex:
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


def add_product(name, description, img, price, number):
    try:
        connection = psycopg2.connect(
            host='127.0.0.1',
            user='postgres',
            password='08112007',
            database='HW-39shop'
        )
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO products (name, description, img, price, number) VALUES (%s, %s, %s, %s, %s)""",
            (name, description, img, price, number)
        )
        connection.commit()  # Добавьте commit, чтобы сохранить изменения
        return "Product added successfully"
    except Exception as _ex:
        logging.error('[INFO] Error while working with PostgreSQL', exc_info=True)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


def delete_product(id):
    if id < 0:
        raise ValueError("ID cannot be negative")

    host = '127.0.0.1'
    user = 'postgres'
    password = '08112007'
    db_name = 'HW-39shop'

    try:
        # Підключення до бази даних
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cursor = connection.cursor()
        logging.info(f"Attempting to delete product with ID {id}")

        # Виконання SQL-запиту на видалення
        cursor.execute("""DELETE FROM products WHERE id = %s;""", (id,))

        # Підтвердження змін
        connection.commit()
        logging.info(f"Product with ID {id} has been deleted")

    except Exception as _ex:
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


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
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:

        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


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
            database=db_name
        )
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM feedback""")
        feedback_list = cursor.fetchall()
        return feedback_list


    except Exception as _ex:
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


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
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


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
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


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
        cursor.execute("""SELECT * FROM users WHERE email = %s""", (email,))
        user_info = cursor.fetchone()
        print(user_info)
        return user_info


    except Exception as _ex:
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')


def get_users_by_id(id):
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
        cursor.execute("""SELECT * FROM users WHERE id = %s""", (id,))
        user_info = cursor.fetchone()
        return user_info


    except Exception as _ex:
        logging.error('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            logging.info('[INFO] PostgreSQL connection closed')
