import sqlite3

def get_conection():
    return sqlite3.connect("controle_caminhão.db")

def criar_tabelas():
    conn = get_conection()
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