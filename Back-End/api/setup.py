from unittest import result
from flask import Flask, request, Response, render_template
from datetime import date
import flask
import json
import mysql.connector
from dbcommands import Commands

app = Flask(__name__)
mydb = mysql.connector.connect(user='root', password='Senha1234',
                              host='127.0.0.1',
                              database='cadastro')
mycursor = mydb.cursor()
cm = Commands(mycursor)

cm.search()

@app.route("/help")
def pagina_ajuda():
    return "<p>PÁGINA HELP DA API</p>"

@app.route("/alunos/add", methods=['POST']) 
def add_aluno(): # Adiciona alunos no banco
    try:
        dados: tuple[str,str,date,str,str,int] = (request.form['cpf_aluno'],request.form['nome_aluno'],request.form['nascimento_aluno'],request.form['email_aluno'],request.form['senha_aluno'],request.form['unidade_id_aluno']) # (CPF_ALUNO, NOME_ALUNO, NASCIMENTO_ALUNO, EMAIL_ALUNO, SENHA_ALUNO, UNIDADE_ID_ALUNO)
        email_usuario = request.headers['email-usuario']
        senha_usuario = request.headers['senha-usuario']
        resultado = cm.add_alunos(dados,email_usuario,senha_usuario)
        if resultado == 200: # Se o usuario que fez a requisição for coordenador...
            mydb.commit()
            return Response(status=200)
        else: # Caso não seja...
            return Response(status=403)
    except:
        return Response(status=500)

@app.route("/alunos/delete", methods=['DELETE'])
def delete_alunos(): # Remove alunos do banco
    try:
        cpf_aluno = request.args.get('cpf') # (CPF_ALUNO)
        email_usuario = request.headers['email-usuario']
        senha_usuario = request.headers['senha-usuario']
        resultado = cm.delete_alunos(cpf_aluno,email_usuario,senha_usuario)
        if resultado == 200: # Se o usuario que fez a requisição for coordenador...
            mydb.commit()
            return Response(status=200)
        else: # Caso não seja...
            return Response(status=403)
    except:
        return Response(status=500)
    
@app.route("/alunos/modificar", methods=['POST']) 
def modificar_alunos(): # Altera dados
    try:
        cpf_aluno = request.args.get('cpf') # (CPF_ALUNO)
        campo = request.form.get('campo')
        novo_dado = request.form.get('novo_dado')
        email_usuario = request.headers.get('email-usuario')
        senha_usuario = request.headers.get('senha-usuario')
        resultado = cm.modificar_alunos(campo,cpf_aluno,novo_dado,email_usuario,senha_usuario)
        if resultado == 200: # Se o usuario que fez a requisição for coordenador...
            mydb.commit()
            return Response(status=200)
        else: # Caso não seja...
            return Response(status=403)
    except:
        return Response(status=500)
    
    

@app.route("/coordenadores/add", methods=['POST']) 
def add_coordenadores(): # Adiciona alunos no banco
    try:
        dados: tuple[str,str,date,str,str,int] = (request.form['cpf_co'],request.form['nome_co'],request.form['nascimento_co'],request.form['email_co'],request.form['senha_co'],request.form['unidade_id_co']) # (CPF_ALUNO, NOME_ALUNO, NASCIMENTO_ALUNO, EMAIL_ALUNO, SENHA_ALUNO, UNIDADE_ID_ALUNO)
        email_usuario = request.headers.get('email-usuario')
        senha_usuario = request.headers.get('senha-usuario')
        resultado = cm.add_alunos(dados,email_usuario,senha_usuario)
        if resultado == 200: # Se o usuario que fez a requisição for coordenador...
            mydb.commit()
            return Response(status=200)
        else: # Caso não seja...
            return Response(status=403)
    except:
        return Response(status=500)

# @app.route("/alunos/remove", methods=['POST']) # Deve ser POST pois um formulário HTML aceita...
# def add_aluno(): # Adiciona alunos no banco
#     dados: tuple[str,str,datetime.date,str,int] = (request.form['cpf'],request.form['nome'],request.form['nascimento'],request.form['email'],request.form['unidade'])
#     cm.addalunos(dados)
#     mydb.commit()
#     return Response(status=200)


    
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)