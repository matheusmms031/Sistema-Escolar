import mysql.connector
from dbcommands import Commands


mydb = mysql.connector.connect(user='root', password='Senha1234',
                              host='127.0.0.1',
                              database='cadastro')
mycursor = mydb.cursor()
cm = Commands(mycursor)

# query = (f"UPDATE alunos SET cpf='cpfteste' WHERE cpf='1'")
# mycursor.execute(query)
# mydb.commit()

cm.modificar_alunos('cpf','cpfteste','1','teste2','123')
mydb.commit()
