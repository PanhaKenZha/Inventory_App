import importlib
import os
import sys


CURRENT_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)

from db import DB_NAME, get_connection


MIGRATIONS = [
    "001_create_cars_table",
    "002_create_users_table",
    
]


def create_database():
    with get_connection(use_database=False) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")


def ensure_migrations_table(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS schema_migrations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            version VARCHAR(100) NOT NULL UNIQUE,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


def has_migration_run(cursor, version):
    cursor.execute(
        "SELECT id FROM schema_migrations WHERE version = %s",
        (version,),
    )
    return cursor.fetchone() is not None


def record_migration(cursor, version):
    cursor.execute(
        "INSERT INTO schema_migrations (version) VALUES (%s)",
        (version,),
    )



def run_migrations():
    create_database()

    with get_connection() as connection:
        with connection.cursor() as cursor:
            ensure_migrations_table(cursor)

            for migration_name in MIGRATIONS:
                module = importlib.import_module(
                    f"migrations.versions.{migration_name}"
                )

                if has_migration_run(cursor, module.version):
                    print(f"Skipped {module.version}")
                    continue

                module.up(cursor)
                record_migration(cursor, module.version)
                print(f"Applied {module.version}")


if __name__ == "__main__":
    run_migrations()
