import mysql.connector

#Processo de conectar com o servidor SQl
def leitura(idade,sexo):
    banco = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd="",
        database='csv'
    )
    cursor = banco.cursor()
    #Comando em SQL (Leitura de dados)
    comandosql =("select cidade,count(idade) from pessoas where idade > %s and sexo = %s group by cidade order by count(idade) desc;")
    dados = (idade,sexo)
    cursor.execute(comandosql,dados)
    #informaçao retirada do Db
    info = cursor.fetchall()
    return info

