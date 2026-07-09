version = "003_create_categories_table"


def up(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(150) NOT NULL UNIQUE,
            description TEXT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


def down(cursor):
    cursor.execute("DROP TABLE IF EXISTS categories")
