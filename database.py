import sqlite3

def get_db_connection():
    conn = sqlite3.connect(
        'despesas.db',
        check_same_thread=False  # Permite acesso multi-thread
    )
    conn.execute('PRAGMA journal_mode = WAL;')  # Modo WAL para evitar locks
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    try:
        with open('schema.sql', 'r') as f:
            conn.executescript(f.read())
        conn.commit()
    finally:
        conn.close()