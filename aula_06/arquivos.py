# PERSISTENCIA
# try:
#     int("sdfsaf")   
# except Exception as e:
#     log = open("logs.log", "w")
#     log.write(f"Erro: {e}\n")
#     log.close()

# 

alunos = ["Julio", "Camilla", "Celso"]

arquivo = open("alunos.txt", "w")

# arquivo.write("Alunos\n")
# for aluno in alunos:
#     arquivo.write(f"{aluno}\n")

arquivo.close()


# LEITURA
arq = open("../programa/main.py", "r")

# print(  arq.read(2)  ) # pegar caracteres
# print(  arq.readable()  ) # modificado
# print(  arq.readline()  ) # 
# print(  arq.readline()  ) # 

linhas_do_codigo = []

# for x in arq.readlines():
#     linhas_do_codigo.append(x)

# print(linhas_do_codigo)

arq.close()

