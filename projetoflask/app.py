from flask import Flask, render_template, session,redirect, url_for, request

app = Flask(__name__)

app.secret_key = 'senha'

@app.route("/")
def hello_world():
    return "Olá, Mundo!"

@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    session['username'] = username
    return redirect(url_for('profile'))

@app.route('/logar', methods=['POST'])
def logar():
    users = ['gabriel', 'sofia']
    passwords = ['123456', 'senha']
    user_name = request.form['username']
    user_password = request.form['password']

    logado = False

    for user in users:
        if user == user.name:
            session['user_name'] = user
            logado = True
        else:
            logado = False
            return redirect(url_for('profile'))   
        
    return render_template('login.html', produtos=produtos, logado=logado)

@app.route('/produtos')
def produtos():

    produtos = ['maçã', 'banana', 'laranja']
    logado = True

    return render_template('produtos.html', produtos=produtos, logado=logado)


if __name__ == "__main__":
    app.run(debug=True)