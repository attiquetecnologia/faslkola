from flask import Flask, redirect, render_template, request, session, url_for # importa bibliotecas

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Anna 005"
        return render_template("index.html", nome=nome) # combina o python com html

    @app.route("/alunos")
    def alunos():
        import json
        from database.dados import alunos
        return render_template("lista.html" , alunos=alunos)

    @app.route("/login", methods=('post', 'GET'))
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
                    error = "Usuario ou senha invalido!"
           
        return render_template("login.html" , error=error)

    def login():
        return "<H1>Login ainda não implementado</h1>"
    
    return app # retorna o app criado

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000