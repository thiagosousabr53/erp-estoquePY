import sqlite3
from database import conectar_banco

try:
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    # Executa um comando SQL simples para testar
    cursor.execute("SELECT 1")  # Consulta de teste
    resultado = cursor.fetchone()
    
    print("✅ Conexão bem-sucedida! Resultado do teste:", resultado[0])
    
except sqlite3.Error as erro:
    print("❌ Erro na conexão:", erro)
    
finally:
    if conexao:
        conexao.close()  # Fecha a conexão