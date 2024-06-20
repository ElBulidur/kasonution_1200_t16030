# PERSISTENCIA
# NOME | EMAIL | SENHA
import mysql.connector

# FAZER CONEXÃO
try:

    def pegar_conexao ():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="kasolution"
        )

        return conn
        # print("Conexão feita com sucesso!")

    # TRABALHA (CRUD) // CREATE(Criar) - READ(leitura) - UPDATE(atualização) - DELETE(deletar)

    # CREATE
    def criar_usuario(nome, email, senha):
        conn = pegar_conexao()
        # sql 
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        valores = [nome, email, senha]

        # cursor
        cursor = conn.cursor()

        # executar o sql
        cursor.execute(sql, valores)

        # COMMITAR
        conn.commit()
        
        # FECHA A CONEXÃO
        conn.close()

        print("Usuário criado com sucesso!")
        
    # READ
    def pegar_todos_usuarios():
        conn = pegar_conexao()
        #sql
        sql = "SELECT * FROM usuarios"

        #cursor
        cursor = conn.cursor()

        #executar o sql
        cursor.execute(sql)

        usuarios = []

        for linha in cursor:
            usuarios.append(linha)

        conn.close()

        # print(usuarios)
        # print(usuarios[0][1])
        return usuarios

    def pegar_usuario(id):
        conn = pegar_conexao()
        sql = "SELECT nome, email, senha FROM usuarios WHERE id=%s"

        cursor = conn.cursor()

        cursor.execute(sql, [id])

        registro = cursor.fetchone()

        if registro:
            return registro
        else:
            return f"Não encontramos o usuário com id {id} no banco de dados!"

    #UPDATE
    def atualizar_usuario(id, nome, email, senha):
        conn = pegar_conexao()

        sql = "UPDATE usuarios SET nome=%s, email=%s, senha=%s WHERE id=%s"

        id = 4
        valores = [nome, email, senha, id]

        cursor = conn.cursor()

        cursor.execute(sql, valores)

        if cursor.rowcount:
            conn.commit()
            conn.close()
            print("Usuário atualizado com sucesso!")
        else:
            conn.close()
            print(f"Não existe no banco de dados o usuario com id {id}!")

    # DELETE
    def deletar_usuario(id):
        conn = pegar_conexao()

        sql = "DELETE FROM usuarios WHERE id=%s"

        cursor = conn.cursor()

        cursor.execute(sql, [id])

        if cursor.rowcount:
            conn.commit()
            conn.close()
            print("Usuário deletado com sucesso!")
        else:
            conn.close()
            print(f"Não existe no banco de dados o usuario com id {id}!")

except mysql.connector.Error as error:
    print( f"Erro: {error}")

# criar_usuario("Camilla", "camilla@email.com", "123456")

# print( pegar_todos_usuarios())

# print( pegar_usuario(30))

# atualizar_usuario(3, "Celso", "celso@email", "sljahdbskl;ncvadcdas")

# deletar_usuario(4)

