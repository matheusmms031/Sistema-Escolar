from datetime import date


class Commands():
    def __init__(self,cursor):
        self.cursor = cursor
        self.TABELA_ALUNOS = ['cpf','nome','nascimento','email','senha','unidade_id']
        
    def argumentos_query(self,tabela,argumentos):
        chaves = list(argumentos.keys())
        valores = list(argumentos.values())
        query = ""
        match tabela:
            case 'alunos':
                for argumento in chaves:
                    if argumento not in self.TABELA_ALUNOS:
                        return False
                    else:
                        query += f"{argumento}='{valores[chaves.index(argumento)]}' "
        print(query)
        return query
    
    def loginconfirmacao(self,usuario,email,senha,): # Confirma se o email e a senha batem no banco
        query = f"SELECT * FROM {usuario} WHERE email='{email}' and senha='{senha}'"
        self.cursor.execute(query)
        quantidade = len(self.cursor.fetchall())
        if quantidade == 0:
            return False
        if quantidade != 0:
            return True
        
    def add_alunos(self,dados: dict[str,str,date,str,int],email_usuario,senha_usuario): # (CPF_ALUNO, NOME_ALUNO, NASCIMENTO_ALUNO, EMAIL_ALUNO, SENHA_ALUNO, UNIDADE_ID_ALUNO)
        loginconfirmacao = self.loginconfirmacao('coordenadores',email_usuario,senha_usuario) # Faz a confirmação do coordenador, já que é o único que pode adicionar alunos
        if loginconfirmacao == True:
            query = (f"INSERT INTO alunos (cpf,nome,nascimento,email,senha,unidade_id) VALUES (%s,%s,%s,%s,%s,%s)")
            self.cursor.execute(query,(dados['cpf_aluno'],dados['nome_aluno'],dados['nascimento_aluno'],dados['email_aluno'],dados['senha_aluno'],dados['unidade_id_aluno'])) # Transforma o dicionario em lista e adiciona
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