from dbcommands import Commands
import pytest
import mysql.connector
import datetime


mydb = mysql.connector.connect(user='root', password='Senha1234',
                              host='127.0.0.1',
                              database='cadastro')
mycursor = mydb.cursor()
cm = Commands(mycursor)



@pytest.mark.loginconfirmacao #TESTES DE CONFIRMAÇÃO DE LOGIN
def test_logincorfimacao_quando_receber_login_de_coordenador():
    email_teste_coordenador = "c_emailteste"
    senha_teste_coordenador = "c_senhateste"
    resultado = cm.loginconfirmacao('coordenadores',email_teste_coordenador,senha_teste_coordenador)
    assert resultado == True

@pytest.mark.loginconfirmacao
def test_logincorfimacao_quando_receber_login_de_coordenador_errado():
    email_teste = "emailerrado"
    senha_teste = "senhaerrado"
    resultado = cm.loginconfirmacao('coordenadores',email_teste,senha_teste)
    assert resultado == False
    
@pytest.mark.alunos
def test_consulta_alunos_com_dados_existentes():
    email_teste_coordenador = "c_emailteste"
    senha_teste_coordenador = "c_senhateste"
    resultado = cm.consulta('alunos',{'cpf':'a_cpfteste','email':'a_emailteste'},email_teste_coordenador,senha_teste_coordenador)
    assert resultado == [("a_cpfteste","a_nometeste",datetime.date(1999, 9, 9),"a_emailteste","a_senhateste",1)]

@pytest.mark.alunos
def test_consulta_alunos_com_dados_inexistentes():
    email_teste_coordenador = "c_emailteste"
    senha_teste_coordenador = "c_senhateste"
    resultado = cm.consulta('alunos',{'cpf':'naoexiste','email':'naoexiste'},email_teste_coordenador,senha_teste_coordenador)
    assert resultado == []
    
@pytest.mark.alunos
def test_add_alunos():
    email_teste_coordenador = "c_emailteste"
    senha_teste_coordenador = "c_senhateste"
    dados = ('cpf','nome','2006','email','senha','1')
    resultado = cm.add('alunos',dados,email_teste_coordenador,senha_teste_coordenador)
    assert resultado == {'status_code':200,'data':{'cpf':'cpf','nome':'nome','nascimento':'2006','email':'email','senha':'senha','unidade_id':'1'}}
    
@pytest.mark.unidades
def test_consulta_unidades_com_dados_existentes():
    email_teste_coordenador = "c_emailteste"
    senha_teste_coordenador = "c_senhateste"
    resultado = cm.consulta('unidades',{'id':'1'},email_teste_coordenador,senha_teste_coordenador)
    assert resultado == [(1,'nometeste','localizacaoteste',None)]
    
@pytest.mark.unidades
def test_consulta_unidades_com_dados_inexistentes():
    email_teste_coordenador = "c_emailteste"
    senha_teste_coordenador = "c_senhateste"
    resultado = cm.consulta('unidades',{'id':'naoexiste'},email_teste_coordenador,senha_teste_coordenador)
    assert resultado == []

def test_argumentos_query_com_and():
    parametros = {'cpf':'a_cpfteste','email':'a_emailteste'}
    resultado = cm.argumentos_query(parametros)
    assert resultado ==  "cpf='a_cpfteste' && email='a_emailteste'"

