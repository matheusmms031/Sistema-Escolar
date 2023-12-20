import mysql.connector
from dbcommands import Commands


mydb = mysql.connector.connect(user='root', password='Senha1234',
                              host='127.0.0.1',
                              database='cadastro')
mycursor = mydb.cursor()
cm = Commands(mycursor)

print(cm.loginconfirmacao('teste','123'))
