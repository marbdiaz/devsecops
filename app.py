import sqlite3

def conectar_banco():
    # ERRO DE SEGURANÇA 1: Credencial hardcoded no código fonte
    password_db = "senha_super_secreta"#
    print(f"Conectando ao banco com a senha: {password_db}")

def buscar_usuario(nome_usuario):
    # ERRO DE SEGURANÇA 2: Concatenação direta de string (risco de SQL Injection)
    conn = sqlite3.connect('banco_exemplo.db')
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = ?"
    cursor.execute(query, (nome_usuario,))
    return cursor.fetchall()

if __name__ == "__main__":
    conectar_banco()