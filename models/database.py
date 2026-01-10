import sqlite3

def get_connection():
    return sqlite3.connect("controle_caminhao.db")

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS viagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        origem TEXT,
        destino TEXT,
        frete REAL,
        diesel REAL,
        pedagio REAL,
        manutencao REAL,
        outros REAL,
        lucro REAL
    )
    """)

    conn.commit()
    conn.close()
