version = "004_add_password_hash_to_users"


def up(cursor):
    cursor.execute(
        """
        ALTER TABLE users
        ADD COLUMN password_hash VARCHAR(255) NULL
        """
    )


def down(cursor):
    cursor.execute("ALTER TABLE users DROP COLUMN password_hash")
