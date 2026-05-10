import sqlite3
def conectar():
    conn = sqlite3.connect('dados.db')
    conn.row_factory = sqlite3.Row
    return conn


def criar_tabela():
    conn = conectar()
    with conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    celular TEXT NOT NULL
                    )''')
    conn.close()


def inserir_usuario(nome, idade, email, celular):
    conn = conectar()
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, idade, email, celular) VALUES (?, ?, ?, ?)", (nome, idade, email, celular))
    conn.close()


def listar_usuarios():
    conn = conectar()
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()
    conn.close()
    return dados


def pesquisar_usuario(nome_busca):
    conn = conectar()
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nome LIKE ?", (f'%{nome_busca}%',))
        resultados = cursor.fetchall()
    conn.close()
    return resultados