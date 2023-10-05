from flask import Flask, redirect, render_template, request, session, url_for # importa bibliotecas

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Beatriz"
        return render_template("index.html", nome=nome) # combina o python com html


    from usuarios.controller import bp
    app.register_blueprint(bp)

    from alunos.controller import bp 
    app.register_blueprint(bp)

    return app # retorna o app criado

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000