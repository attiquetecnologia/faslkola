import click
from flask import Flask, app, redirect, render_template, request, session, url_for
from flask.cli import with_appcontext
from database.connection import db

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldp://usuario:senha@localhost:3306/banco_dados"
    app.config["SQLALCHEMY_TRACK_MODFICATIONS"] = False

    db.init_app(app)
    app.cli.add(init_db_command)

    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Alexandre xandon 07"
        return render_template("index.html", nome=nome) # combina o python com html


    @app.route("/login", methods=('POST', 'GET'))
    def login():
        error = None
        if request.method == 'POST':
            email = request.form.get('email')
            senha = request.form.get('senha')

            from database.dados import alunos
            for k,v in alunos.items():
                if email == v.get('usuario') and senha == v.get('senha'):
                    session['user'] = v
                    return redirect(url_for('index'))
                else:
                    error = "Usuario ou senha inválidos!"

        return render_template("login.html", error=error)
    
    @app.route("/logout")
    def logout():
        return redirect(url_for("login"))
    
    @app.route("/recsenha", methods=('POST', 'GET'))
    def recsenha():
        error = None
        return render_template("recsenha.html", error=error)
    
    @app.route("/perfil")
    def perfil():

        if 'user' not in session and False:
            # se não tiver lgoado devolve para login
            return redirect(url_for('login'))

        # 1-Pegar dados do banco
        # for k,v ... in alunos... session['user']['email']==email

        if request.method == 'POST':
            # lógica salvar
            nome = request.form.get("nome")
            email = request.form.get("email")

            from database.dados import alunos
            for k,v,x in alunos.items():
                pass
    
        return render_template("usuarios/perfil.html") #, usuario=usuario
    
    from usuarios.controller import db
    app.register_blueprint(db)
    
    from alunos.controller import db
    app.register_blueprint(db)
    
    return app # retorna o app criado

def init_db():
    db.drop_all()
    # db.create_all()
    db.reflect()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""

    init_db()
    click.echo("Initialized the database.")


if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000
