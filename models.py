from database import get_db_connection

class Despesa:
    @staticmethod
    def create(descricao, valor, data):
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO despesas (descricao, valor, data) VALUES (?, ?, ?)',
                (descricao, valor, data)
            )
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        try:
            despesas = conn.execute('SELECT * FROM despesas ORDER BY data DESC').fetchall()
            return despesas
        finally:
            conn.close()

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        try:
            despesa = conn.execute(
                'SELECT * FROM despesas WHERE id = ?', 
                (id,)
            ).fetchone()
            return despesa
        finally:
            conn.close()

    @staticmethod
    def update(id, descricao, valor, data):
        conn = get_db_connection()
        try:
            conn.execute(
                'UPDATE despesas SET descricao = ?, valor = ?, data = ? WHERE id = ?',
                (descricao, valor, data, id)
            )
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        try:
            conn.execute('DELETE FROM despesas WHERE id = ?', (id,))
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def get_total():
        conn = get_db_connection()
        try:
            total = conn.execute('SELECT SUM(valor) as total FROM despesas').fetchone()['total']
            return total if total is not None else 0.0
        finally:
            conn.close()