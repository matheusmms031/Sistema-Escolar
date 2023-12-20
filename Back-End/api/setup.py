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

@app.route("/alunos/add", methods=['POST']) # Rota /alunos/add
def add_aluno(): # Adiciona alunos no banco
    try:
        dados: dict[str,str,date,str,str,int,str,str] = json.loads(request.data) # (CPF_ALUNO, NOME_ALUNO, NASCIMENTO_ALUNO, EMAIL_ALUNO, SENHA_ALUNO, UNIDADE_ID_ALUNO, EMAIL_USUARIO, SENHA_USUARIO)
        resultado = cm.add_alunos(dados)
        if resultado == 200: # Se o usuario que fez a requisição for coordenador...
            mydb.commit()
            return Response(status=200)
        else: # Caso não seja...
            return Response(status=403)
    except:
        return Response(status=500)

@app.route("/alunos/delete", methods=['DELETE']) # Rota /alunos/add
def delete_alunos(): # Adiciona alunos no banco
    try:
        dados: dict[str,str,str] = json.loads(request.data) # (CPF_ALUNO, EMAIL_USUARIO, SENHA_USUARIO)
        resultado = cm.delete_alunos(dados)
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