python
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Configuração de um banco em memória para o laboratório
def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INTEGER, username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users VALUES (1, 'admin', 'p@ssword123')")
    conn.commit()
    return conn

@app.route('/login', list=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # VULNERABILIDADE: Concatenação direta de strings gerando SQL Injection
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        conn = sqlite3.connect(':memory:') # Simplificado para o escopo do lab
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                return "Login efetuado com sucesso!"
            return "Incorreto usuário ou senha."
        except Exception as e:
            return f"Erro no banco de dados: {str(e)}"
            
    return '''
        <form method="POST">
            Usuário: <input type="text" name="username"><br>
            Senha: <input type="password" name="password"><br>
            <input type="submit" value="Entrar">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
