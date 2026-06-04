import sqlite3

DB_NAME = "materials.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS materials (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            width REAL NOT NULL,

            height REAL NOT NULL,

            price REAL NOT NULL
        )
    """)

    conn.commit()

    conn.close()


def add_material_db(
        name,
        width,
        height,
        price
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO materials
        (name, width, height, price)

        VALUES (?, ?, ?, ?)
        """,
        (
            name,
            width,
            height,
            price
        )
    )

    conn.commit()
    conn.close()


def get_all_materials():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, width, height, price FROM materials"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_material_db(name):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM materials
        WHERE name = ?
        """,
        (name,)
    )

    conn.commit()
    conn.close()


def update_material_db(
        old_name,
        new_name,
        width,
        height,
        price
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE materials

        SET
            name = ?,
            width = ?,
            height = ?,
            price = ?

        WHERE name = ?
        """,
        (
            new_name,
            width,
            height,
            price,
            old_name
        )
    )

    conn.commit()
    conn.close()
