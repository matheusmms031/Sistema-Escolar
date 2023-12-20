from datetime import date


class Commands():
    def __init__(self,cursor):
        self.cursor = cursor
        
    def loginconfirmacao(self,usuario,email,senha,): # Confirma se o email e a senha batem no banco
        query = f"SELECT * FROM {usuario} WHERE email='{email}' and senha='{senha}'"
        self.cursor.execute(query)
        quantidade = len(self.cursor.fetchall())
        if quantidade == 0:
            return False
        if quantidade > 0:
            return True
        
    def addalunos(self,dados: dict[str,str,date,str,int,str,str]):
        loginconfirmacao = self.loginconfirmacao('coordenadores',dados['email_usuario'],dados['senha_usuario']) # Faz a confirmação do coordenador, já que é o único que pode adicionar alunos
        if loginconfirmacao == True:
            query = (f"INSERT INTO alunos (cpf,nome,nascimento,email,unidade_id) VALUES (%s,%s,%s,%s,%s)")
            self.cursor.execute(query,dados)
            return 200
        else:
            return 403
        
    def search(self):
        self.cursor.execute('SELECT * FROM alunos')
        print(self.cursor.fetchall())