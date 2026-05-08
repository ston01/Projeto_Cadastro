import sqlite3
def conectar():
    con = sqlite3.connect('dados.db')
    con.row_factory = sqlite3.Row
    return con


def criar_tabela():
    con = conectar()
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
                )''')
    con.commit()
    con.close()


def inserir_usuario(nome, idade):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
    con.commit()
    con.close()


def listar_usuarios():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT nome, idade FROM usuarios")
    dados = cursor.fetchall() # Retorna uma lista de tuplas
    con.close()
    return dados