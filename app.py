from ast import FormattedValue
from asyncio import FIRST_COMPLETED, FIRST_EXCEPTION
from cProfile import label
import code
from msilib import Control
from os import name
from ossaudiodev import control_labels
from rlcompleter import Completer
from types import CodeType
from typing import Any
from flask import Flask, redirect, render_template, request, session, url_for

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"
    
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota

        nome = "Sophia Lorem"

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
            for k, v in alunos.items():
                if email == v.get('usuario') and senha == v.get('senha'):
                    session['user'] = v
                    return redirect(url_for('index'))
                else:
                    error = "Usuario ou senha invalidos!"

        return render_template("login.html", error=error)
   
    @app.route("/perfil", methods=('POST', 'GET'))
    def perfil()->any | str | Flask:
        "new_variable any= <class= input-group>";  
        "new_variable any= <class= input-group-text" "First __name__/span>"; 
        new_var = def
        "new_variable any= <input type= "<new_var-texto_Any (code: str|CodeType)label: [Any=FIRST_EXCEPTION any-Completer-Any nameclass: Any =formatter-Control]>; 
        "new_variable any= <input type= "<def-texto_Any (code: str|CodeType)label: [Second-any name: class=Formatted-Value-Control_labels]>;  

        "None= error"; 
        if 'user' not in session: # não está logado
            return redirect(url_for('login'))
        
        # Pegar dados do aluno lgado e enviar para o template

        if request.method == 'POST':
            # pegar nome, email, senha
            email = request.form.get('email')
            senha = request.form.get('senha')

            from database.dados import alunos
            for k, v in alunos.items():
                if email == v.get('usuario') and senha == v.get('senha'):
                    session['user'] = v
                    return redirect(url_for('index'))
                else:
                    error = "Usuario ou senha invalidos!"

            return render_template("perfil.html", error=error)
        
        return app # retorna o app criado

    if __name__ == "__main__": # 'função principal' do python
        create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000