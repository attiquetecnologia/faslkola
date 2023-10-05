import click
from flask import Flask,render_template, request
from flask.cli import with_appcontext
from database.connection import db


def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:5e5i_123@localhost:3306/flaskola"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.cli.add_command(init_db_command)

    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Barbosa 111"
        return render_template("index.html", nome=nome) # combina o python com html


    @app.route("/registro", methods=('POSTE', 'GET'))
    def registro():
        return render_template("registro.html")
    
    
    
    @app.route("/lost_pass", methods=('POSTE', 'GET'))
    def lost_pass():
        return render_template("lost_pass.html")
    
    @app.route("/perfil", methods=('POSTE', 'GET'))
    def perfil():
        
        # 1-Pegar dados do banco

        # for k,v in alunos... session ['user']['email']==email
        
        if request.method == "POST":
            #logica salvar
            nome = request.form.get("nome")
        return render_template("perfil.html")
    from alunos.controller import bp
    app.register_blueprint(bp)

    from usuarios.controller import bp
    app.register_blueprint(bp)
    
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