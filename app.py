from flask import Flask, redirect, render_template, request, session, url_for # importa bibliotecas

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"
    
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Loise"
        return render_template("index.html", nome=nome) # combina o python com html

    @app.route("/alunos")
    def alunos():
        import json
        from database.dados import alunos

        # Função lambda cria funções de 1 linha só
        # media = lambda t,p1,p2: t*.3+p1*.35+p2*.35
        def media(t, p1, p2):
            return t*.3+p1*.35+p2*.35
        
        return render_template("lista.html", alunos=alunos, media=media )

    @app.route("/login", methods=('POST', 'GET'))
    def login():
        error = None
        if request.method == 'POST':
            email = request.form.get('email')
            senha = request.form.get('senha')
            
            from database.dados import alunos
            for k,v in alunos.items():
                if email == v.get('usario') and senha == v.get('senha'):
                    session['user'] = v
                    return redirect(url_for('index'))
                else:
                    error = "Usuario ou senha invalidos!"
        return render_template("login.html", error=error)
    
    @app.route("/recuperarsenha", methods=('POST', 'GET'))
    def recuperarsenha():
        if request.method == 'POST':
            # 1-pegar email do formulário
            email = request.form.get('email')
            senha = request.form.get("senha")
            nova_senha = request.form.get('nova_senha')
            repita_senha = request.form.get('repita_senha')

            # 2-Verificar se email existe, se existe passo 3
            from database.dados import alunos
            for k,v in alunos.items():
                if email == v.get('usario') and senha == v.get('senha'):
                    if nova_senha == repita_senha:
                        alunos[k]["senha"] = nova_senha
        # 3-retornar formulário para redefinir senha

        # 4-Se formulário enviado em POST
        # verificar de novo se email existe e se as senhas são iguais
        # Se forem iguais, salva no banco de dados alunos['id']['senha'] = novasenha
        return render_template("recuperarsenha.html")

    return app # retorna o app criado

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000