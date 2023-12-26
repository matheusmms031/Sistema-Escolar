from asyncio import QueueEmpty
from datetime import date
from os import stat
import mysql.connector
from urllib import response

mydb = mysql.connector.connect(user='root', password='Senha1234',
                              host='127.0.0.1',
                              database='cadastro')


class Commands():
    def __init__(self,cursor):
        self.mydb = mydb
        self.cursor = cursor
        self.TABELAS = {'alunos':['cpf','nome','nascimento','email','senha','unidade_id'],'coordenadores':['cpf','nome','nascimento','email','senha','unidade_id'],'unidades':['id','nome','localização','cpf_coordenador']}
        
    def login(self,email,senha):
        tabelas_login = ['alunos','coordenadores']
        saida = {'status_code':0,'data':{}}
        for tabela in tabelas_login:
            query = f"SELECT * FROM {tabela} WHERE email='{email}' and senha='{senha}'"
            self.cursor.execute(query)
            resposta = self.cursor.fetchall()
            if len(resposta) != 0:
                resposta = resposta[0]
                saida['data']['usuario'] = tabela
                for coluna in self.TABELAS[tabela]:
                    saida['data'][coluna] = resposta[self.TABELAS[tabela].index(coluna)]
                saida['status_code'] = 200
                return saida
            else:
                saida['status_code'] = 500
        return saida
            
    
    def argumentos_query(self,argumentos):
        chaves = list(argumentos.keys())
        valores = list(argumentos.values())
        query = ""
        if len(chaves) == 1:
            if chaves[0] == 'nome' or chaves[0] == 'email':
                query = f"{chaves[0]} LIKE '{valores[0]}%'"
            else:
                query = f"{chaves[0]}='{valores[0]}'"
        else:
            for argumento in chaves:
                if argumento == 'nome' or chaves[0] == 'email':
                    query += f" && {argumento} LIKE '{valores[chaves.index(argumento)]}%'"
                else:
                    query += f" && {argumento}='{valores[chaves.index(argumento)]}'"
            query = query.replace("&&","",1).strip()
        print(query)
        return query
    
    def loginconfirmacao(self,usuario,email,senha): # Confirma se o email e a senha batem no banco
        query = f"SELECT * FROM {usuario} WHERE email='{email}' and senha='{senha}'"
        self.cursor.execute(query)
        quantidade = len(self.cursor.fetchall())
        if quantidade == 0:
            return False
        if quantidade != 0:
            return True
        
    def add(self,tabela,dados,email_usuario,senha_usuario): # 
        loginconfirmacao = self.loginconfirmacao('coordenadores',email_usuario,senha_usuario) # Faz a confirmação do coordenador, já que é o único que pode adicionar alunos
        dados = tuple(dados)
        if loginconfirmacao == True:
            campos = self.TABELAS[tabela]
            elemento_adicionado = {}
            campos_query = "("
            campos_str = "("
            for elemento in campos:
                elemento_adicionado[elemento] = dados[campos.index(elemento)]
                campos_query += f',{elemento}'
                campos_str += ",%s"
            campos_str += ')'
            campos_query += ')'
            campos_query = campos_query.replace(",","",1)
            campos_str = campos_str.replace(",","",1)
            query = (f"INSERT INTO {tabela} {campos_query} VALUES {campos_str}")
            print(query)
            self.cursor.execute(query,dados)
            status_code = 200 # Transforma o dicionario em lista e adiciona  # Caso seja coordenador retorne 200
        else:
            status_code = 403 #Caso não seja coordenador retorne 403
        response = {'status_code':status_code,'data':elemento_adicionado}
        print(response)
        return response
    
    def delete(self,tabela,parametros,email_usuario,senha_usuario): 
        loginconfirmacao = self.loginconfirmacao('coordenadores',email_usuario,senha_usuario) # Faz a confirmação do coordenador, já que é o único que pode adicionar alunos
        parametros = self.argumentos_query(parametros)
        if loginconfirmacao == True:
            query = (f"DELETE FROM {tabela} WHERE {parametros}")
            self.cursor.execute(query) # Transforma o dicionario em lista e adiciona
            return 200 # Caso seja coordenador retorne 200
        else:
            return 403 #Caso não seja coordenador retorne 403
        
    def modificar_alunos(self,seletor,cpf_aluno,novo_dado,email_usuario,senha_usuario): # (CPF_ALUNO, EMAIL_USUARIO, SENHA_USUARIO)
        loginconfirmacao = self.loginconfirmacao('coordenadores',email_usuario,senha_usuario) # Faz a confirmação do coordenador, já que é o único que pode adicionar alunos
        if loginconfirmacao == True:
            query = (f"UPDATE alunos SET {seletor}='{novo_dado}' WHERE cpf='{cpf_aluno}'")
            self.cursor.execute(query) # Transforma o dicionario em lista e adiciona
            return 200 # Caso seja coordenador retorne 200
        else:
            return 403 #Caso não seja coordenador retorne 403
        
    def consulta(self,tabela,argumentos,email_usuario,senha_usuario):
        loginconfirmacao = self.loginconfirmacao('coordenadores',email_usuario,senha_usuario)
        saida = {'status_code':0,'data':[]}
        parametros = self.argumentos_query(argumentos)
        if loginconfirmacao == True:
            if argumentos == "" or argumentos == {}:
                query = (f"SELECT * FROM {tabela}")
            else:
                query = (f"SELECT * FROM {tabela} WHERE {parametros}")
            self.cursor.execute(query)
            resultado = self.cursor.fetchall()
            for c in range(0,len(resultado)):
                saida['data'].append({})
                for coluna in self.TABELAS[tabela]:
                    saida['data'][c][coluna] = resultado[c][self.TABELAS[tabela].index(coluna)]
            saida['status_code'] = 200
        else:
            saida['status_code'] = 403
        return saida
        