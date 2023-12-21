from dbcommands import Commands
import mysql.connector
import datetime


mydb = mysql.connector.connect(user='root', password='Senha1234',
                              host='127.0.0.1',
                              database='cadastro')
mycursor = mydb.cursor()
cm = Commands(mycursor)

def test_logincorfimacao_quando_receber_login_de_coordenador():
    email_teste_coordenador = "c_emailteste"
    senha_teste_coordenador = "c_senhateste"
    resultado = cm.loginconfirmacao('coordenadores',email_teste_coordenador,senha_teste_coordenador)
    
    assert resultado == True
    
def test_logincorfimacao_quando_receber_login_de_coordenador_errado():
    email_teste = "emailerrado"
    senha_teste = "senhaerrado"
    resultado = cm.loginconfirmacao('coordenadores',email_teste,senha_teste)
    
    assert resultado == False
    
def test_consulta_aluno():
    email_teste_coordenador = "c_emailteste"
    senha_teste_coordenador = "c_senhateste"
    resultado = cm.consulta('alunos',{'cpf':'a_cpfteste'},email_teste_coordenador,senha_teste_coordenador)
    assert resultado == [("a_cpfteste","a_nometeste",datetime.date(1999, 9, 9),"a_emailteste","a_senhateste",1)]
    
