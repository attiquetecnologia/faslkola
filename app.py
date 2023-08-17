from flask import Flask, render_template # importa bibliotecas

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
<<<<<<< HEAD
        nome = "Manuela 123"
=======
        nome = "Rodrigo 123"
>>>>>>> 453f3749adee9167f80af2773a9c51ff6c0be93a
        return render_template("index.html", nome=nome) # combina o python com html

    @app.route("/alunos")
    def alunos():
        import json
        from database.dados import alunos
<<<<<<< HEAD
        return render_template("lista.html", alunos=alunos)
=======

        # Função lambda cria funções de 1 linha só
        # media = lambda t,p1,p2: t*.3+p1*.35+p2*.35
        def media(t, p1, p2):
            return t*.3+p1*.35+p2*.35
        
        return render_template("lista.html", alunos=alunos, media=media )
>>>>>>> 453f3749adee9167f80af2773a9c51ff6c0be93a

    @app.route("/login")
    def login():
        return "<H1>Login ainda não implementado</h1>"
    
    return app # retorna o app criado

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000