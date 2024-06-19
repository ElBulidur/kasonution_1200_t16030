# PERSISTENCIA
# NOME | EMAIL | SENHA
import mysql.connector

# FAZER CONEXÃO
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="kasolution"
    )

    print("Conexão feita com sucesso!")
except mysql.connector.Error as error:
    print( f"Erro: {error}")


# TRABALHA (CRUD) // CREATE(Criar) - READ(leitura) - UPDATE(atualização) - DELETE(deletar)

# sql 
# cursor
# executar o sql


# FECHA A CONEXÃO
conn.close()

