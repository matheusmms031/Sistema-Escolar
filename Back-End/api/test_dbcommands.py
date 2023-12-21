from dbcommands import Commands
import mysql.connector


mydb = mysql.connector.connect(user='root', password='Senha1234',
                              host='127.0.0.1',
                              database='cadastro')
mycursor = mydb.cursor()
cm = Commands(mycursor)

def test_logincorfimacao_quando_receber_login_de_coordenador():
    email_teste = "teste2"
    senha_teste = "123"
    resultado = cm.loginconfirmacao('coordenadores',email_teste,senha_teste)
    
    assert resultado == True
    
def test_logincorfimacao_quando_receber_login_de_coordenador_errado():
    email_teste = "emailerrado"
    senha_teste = "senhaerrado"
    resultado = cm.loginconfirmacao('coordenadores',email_teste,senha_teste)
    
    assert resultado == False
    
