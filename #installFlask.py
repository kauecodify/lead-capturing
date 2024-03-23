# Instalação do Flask
# pip install Flask

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Inicialização do aplicativo Flask
app = Flask(__name__)

# Configuração do banco de dados
DATABASE = 'database.db'

# Função para criar a tabela no banco de dados
def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Rota para a página inicial
@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Rota para adicionar usuários
@app.route('/add', methods=['POST'])
def add_users():
    name = request.form['name']
    email = request.form['email']
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    create_table()
    app.run(debug=True)

#renderizar lista de usuário na mesma pasta do script/flask