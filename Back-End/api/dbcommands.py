from datetime import date


class Commands():
    def __init__(self,cursor):
        self.cursor = cursor
        self.TABELAS = {'alunos':['cpf','nome','nascimento','email','senha','unidade_id'],'coordenadores':['cpf','nome','nascimento','email','senha','unidade_id']}
        
        
    def argumentos_query(self,tabela,argumentos):
        chaves = list(argumentos.keys())
        valores = list(argumentos.values())
        query = ""
        for argumento in chaves:
            if argumento not in self.TABELAS[tabela]:
                return False
            else:
                query += f"{argumento}='{valores[chaves.index(argumento)]}' "
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
        
    def add(self,tabela,dados,email_usuario,senha_usuario): # (CPF_ALUNO, NOME_ALUNO, NASCIMENTO_ALUNO, EMAIL_ALUNO, SENHA_ALUNO, UNIDADE_ID_ALUNO)
        loginconfirmacao = self.loginconfirmacao('coordenadores',email_usuario,senha_usuario) # Faz a confirmação do coordenador, já que é o único que pode adicionar alunos
        if loginconfirmacao == True:
            campos = self.TABELAS[tabela]
            campos_query = "("
            campos_str = "("
            for elemento in campos:
                campos_query += f',{elemento}'
                campos_str += ",%s"
            campos_str += ')'
            campos_query += ')'
            campos_query = campos_query.replace(",","",1)
            campos_str = campos_str.replace(",","",1)
            query = (f"INSERT INTO {tabela} {campos_query} VALUES {campos_str}")
            print(query)
            self.cursor.execute(query,tuple(dados)) # Transforma o dicionario em lista e adiciona
            return 200 # Caso seja coordenador retorne 200
        else:
            return 403 #Caso não seja coordenador retorne 403
    
    def delete_alunos(self,cpf_aluno,email_usuario,senha_usuario): # (CPF_ALUNO, EMAIL_USUARIO, SENHA_USUARIO)
        loginconfirmacao = self.loginconfirmacao('coordenadores',email_usuario,senha_usuario) # Faz a confirmação do coordenador, já que é o único que pode adicionar alunos
        if loginconfirmacao == True:
            query = (f"DELETE FROM alunos WHERE cpf='{cpf_aluno}'")
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
        parametros = self.argumentos_query(tabela,argumentos)
        if loginconfirmacao == True:
            query = (f"SELECT * FROM {tabela} WHERE {parametros}")
            self.cursor.execute(query)
            resultado = self.cursor.fetchall()
            return resultado
        else:
            return 403