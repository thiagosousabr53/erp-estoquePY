from flask import Flask, render_template, request, redirect, url_for
from models import Despesa
from database import get_db_connection
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'uma_chave_muito_secreta')


# Rotas da Aplicação
@app.route('/')

def index():
    despesas = Despesa.get_all()
    total = Despesa.get_total()
    return render_template('index.html', despesas=despesas, total=total)

@app.route('/add', methods=['POST'])

def add_despesa():
    descricao = request.form['descricao']
    valor = float(request.form['valor'])
    data = request.form['data']
    Despesa.create(descricao, valor, data)
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])

def edit_despesa(id):
    despesa = Despesa.get_by_id(id)
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        data = request.form['data']
        Despesa.update(id, descricao, valor, data)
        return redirect(url_for('index'))
    return render_template('edit.html', despesa=despesa)

@app.route('/delete/<int:id>')
def delete_despesa(id):
    Despesa.delete(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)