from flask import Flask, request, Response
import datetime
import flask
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

@app.route("/alunos/add", methods=['POST']) # Deve ser POST pois um formulário HTML aceita...
def add_aluno(): # Adiciona alunos no banco
    try:
        data: tuple[str,str,datetime.date,str,int] = (request.form['cpf'],request.form['nome'],request.form['nascimento'],request.form['email'],request.form['unidade'])
        cm.addaluno(data)
        mydb.commit()
        return Response(status=200)
    except:
        return Response(status=404)
    
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)