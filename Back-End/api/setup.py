from flask import Flask, request, Response, render_template, jsonify, g
from datetime import date
import flask 
import json
from flask_cors import CORS

import mysql.connector
from dbcommands import Commands

app = Flask(__name__)
cors = CORS(app,origins="*")

mydb = mysql.connector.connect(user='root', password='Senha1234',
                              host='127.0.0.1',
                              database='cadastro')
mycursor = mydb.cursor()
cm = Commands(mycursor)

@app.route("/help")
def pagina_ajuda():
    return "<p>PÁGINA HELP DA API</p>"

@app.route("/alunos/add", methods=['POST']) 
def add_aluno(): # Adiciona alunos no banco
    dados: tuple[str,str,date,str,str,int] = (request.form['cpf_aluno'],request.form['nome_aluno'],request.form['nascimento_aluno'],request.form['email_aluno'],request.form['senha_aluno'],request.form['unidade_id_aluno']) # (CPF_ALUNO, NOME_ALUNO, NASCIMENTO_ALUNO, EMAIL_ALUNO, SENHA_ALUNO, UNIDADE_ID_ALUNO)
    email_usuario = request.headers['email-usuario']
    senha_usuario = request.headers['senha-usuario']
    resultado = cm.add('alunos',dados,email_usuario,senha_usuario)
    if resultado == 200: # Se o usuario que fez a requisição for coordenador...
        mydb.commit()
        return Response(status=200)
    else: # Caso não seja...
        return Response(status=403)

@app.route("/alunos/delete", methods=['DELETE'])
def delete_alunos(): # Remove alunos do banco
    argumentos = request.args.to_dict()
    email_usuario = request.headers['email-usuario']
    senha_usuario = request.headers['senha-usuario']
    resultado = cm.delete('alunos',argumentos,email_usuario,senha_usuario)
    if resultado == 200: # Se o usuario que fez a requisição for coordenador...
        mydb.commit()
        return Response(status=200)
    else: # Caso não seja...
        return Response(status=403)
    
@app.route("/alunos/modificar", methods=['POST']) 
def modificar_alunos(): # Altera dados
    cpf_aluno = request.args.get('cpf')
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
    
@app.route("/alunos/consulta", methods=['GET']) 
def consulta_alunos(): 
    argumentos = request.args.to_dict()
    email_usuario = request.headers.get('email-usuario')
    senha_usuario = request.headers.get('senha-usuario')
    resultado = cm.consulta('alunos',argumentos,email_usuario,senha_usuario)
    print(resultado)
    if resultado != 403: # Se o usuario que fez a requisição for coordenador...
        return jsonify(resultado)
    else:
        return Response(code=resultado)    
    

@app.route("/coordenadores/add", methods=['POST']) 
def add_coordenadores(): # Adiciona alunos no banco
    dados: tuple[str,str,date,str,str,int] = (request.form['cpf_coordenador'],request.form['nome_coordenador'],request.form['nascimento_coordenador'],request.form['email_coordenador'],request.form['senha_coordenador'],request.form['unidade_id_coordenador']) # (CPF_ALUNO, NOME_ALUNO, NASCIMENTO_ALUNO, EMAIL_ALUNO, SENHA_ALUNO, UNIDADE_ID_ALUNO)
    email_usuario = request.headers.get('email-usuario')
    senha_usuario = request.headers.get('senha-usuario')
    resultado = cm.add('coordenadores',dados,email_usuario,senha_usuario)
    if resultado == 200: # Se o usuario que fez a requisição for coordenador...
        mydb.commit()
        return Response(status=200)
    else: # Caso não seja...
        return Response(status=403)
    
@app.route("/coordenadores/delete", methods=['DELETE'])
def delete_coordenadores(): # Remove alunos do banco
    argumentos = request.args.to_dict()
    email_usuario = request.headers['email-usuario']
    senha_usuario = request.headers['senha-usuario']
    resultado = cm.delete('coordenadores',argumentos,email_usuario,senha_usuario)
    if resultado == 200: # Se o usuario que fez a requisição for coordenador...
        mydb.commit()
        return Response(status=200)
    else: # Caso não seja...
        return Response(status=403)
    
@app.route("/coordenadores/consulta", methods=['GET']) 
def consulta_coordenadores(): 
    argumentos = request.args.to_dict()
    email_usuario = request.headers.get('email-usuario')
    senha_usuario = request.headers.get('senha-usuario')
    resultado = cm.consulta('coordenadores',argumentos,email_usuario,senha_usuario)
    if resultado != 403: # Se o usuario que fez a requisição for coordenador...
        return jsonify(resultado)
    else:
        return Response(code=resultado)  
    
@app.route("/unidades/consulta", methods=['GET']) 
def consulta_unidade(): 
    argumentos = request.args.to_dict()
    email_usuario = request.headers.get('email-usuario')
    senha_usuario = request.headers.get('senha-usuario')
    resultado = cm.consulta('unidades',argumentos,email_usuario,senha_usuario)
    if resultado != 403: # Se o usuario que fez a requisição for coordenador...
        return jsonify(resultado)
    else:
        return Response(code=resultado)      

@app.route("/unidades/add", methods=['POST']) 
def add_unidade(): 
    dados = (request.form['nome_unidade'], request.form['localizacao_unidade'], request.form['coordenadora_cpf_unidade'])
    email_usuario = request.headers.get('email-usuario')
    senha_usuario = request.headers.get('senha-usuario')
    resultado = cm.add('unidades',dados,email_usuario,senha_usuario)
    if resultado == 200: # Se o usuario que fez a requisição for coordenador...
        mydb.commit()
        return Response(status=200)
    else: # Caso não seja...
        return Response(status=403)
    
@app.route("/unidades/delete", methods=['DELETE'])
def delete_unidades(): # Remove alunos do banco
    argumentos = request.args.to_dict()
    email_usuario = request.headers['email-usuario']
    senha_usuario = request.headers['senha-usuario']
    resultado = cm.delete('unidades',argumentos,email_usuario,senha_usuario)
    if resultado == 200: # Se o usuario que fez a requisição for coordenador...
        mydb.commit()
        return Response(status=200)
    else: # Caso não seja...
        return Response(status=403)
    
@app.route("/login",methods=["POST"])
def pagina_painel():
    email_usuario = request.form['email']
    senha_usuario = request.form['senha']
    saida = cm.login(email_usuario,senha_usuario)
    return jsonify(saida)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)