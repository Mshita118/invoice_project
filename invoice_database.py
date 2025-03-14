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


def fetch_clients():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT id, name FROM clients"
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


def fetch_invoices():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM invoices"
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


def insert_invoice(client_id, date, subtotal, total):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO invoices (client_id, date, subtotal, total)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (client_id, date, subtotal, total))
        conn.commit()
    finally:
        cursor.close()
        conn.close()
