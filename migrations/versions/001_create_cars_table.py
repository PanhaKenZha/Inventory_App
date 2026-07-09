version = "001_create_cars_table"


def up(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS cars (
            id INT AUTO_INCREMENT PRIMARY KEY,
            make VARCHAR(100) NOT NULL,
            model VARCHAR(100) NOT NULL,
            year INT NOT NULL,
            color VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            sold BOOLEAN NOT NULL DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


def down(cursor):
    cursor.execute("DROP TABLE IF EXISTS cars")
