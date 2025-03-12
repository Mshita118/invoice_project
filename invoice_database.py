import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="mshita",
        password="Tachi_0118",
        database="invoice_db"
    )


def insert_client(name, address):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO clients (name, address) VALUES (%s, %s)"
        cursor.execute(query, (name, address))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
