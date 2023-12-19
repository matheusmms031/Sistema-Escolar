import datetime


class Commands():
    def __init__(self,cursor):
        self.cursor = cursor
        
    def addalunos(self,data: tuple[str,str,datetime.date,str,int]):
        query = ("INSERT INTO pessoas (cpf,nome,nascimento,email,unidade_id) VALUES (%s,%s,%s,%s,%s)")
        self.cursor.execute(query,data)
        
        
    def search(self):
        self.cursor.execute('SELECT * FROM alunos')
        print(self.cursor.fetchall())