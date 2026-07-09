import os

import pymysql
from pymysql.cursors import DictCursor


DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "3306"))
DB_USER = os.environ.get("DB_USER", "panha")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "Nha@12629")
DB_NAME = os.environ.get("DB_NAME", "inventory_db")


def get_connection(use_database=True):
    config = {
        "host": DB_HOST,
        "port": DB_PORT,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "cursorclass": DictCursor,
        "autocommit": True,
    }
    if use_database:
        config["database"] = DB_NAME

    return pymysql.connect(**config)


def init_db():
    with get_connection(use_database=False) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")

    from migrations.migrate import run_migrations

    run_migrations()


def get_cars():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM cars ORDER BY id")
            return cursor.fetchall()


def get_car(car_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM cars WHERE id = %s", (car_id,))
            return cursor.fetchone()


def create_car(make, model, year, color, price):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO cars (make, model, year, color, price, sold)
                VALUES (%s, %s, %s, %s, %s, FALSE)
                """,
                (make, model, year, color, price),
            )


def get_users():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users ORDER BY id")
            return cursor.fetchall()


def get_user(user_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            return cursor.fetchone()


def create_user(name, email, phone):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users (name, email, phone)
                VALUES (%s, %s, %s)
                """,
                (name, email, phone),
            )


def get_categories():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM categories ORDER BY id")
            return cursor.fetchall()


def get_category(category_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM categories WHERE id = %s", (category_id,))
            return cursor.fetchone()


def create_category(name, description):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO categories (name, description)
                VALUES (%s, %s)
                """,
                (name, description),
            )
