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


def insert_detail(client_id, building_count, unit_price):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO details (client_id, building_count, unit_price)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (client_id, building_count, unit_price))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def fetch_details():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
        SELECT details.id, clients.name, details.building_count, details.unit_price, details.total_price, details.created_at
        FROM details
        INNER JOIN clients ON details.client_id = clients.id
        """
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
