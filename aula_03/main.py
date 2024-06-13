
curso = {
    "descrição": "Programando com python",
    "disciplinas": [
        "Variáveis",
        "Operadores",
        "Condicionais",
        "Coleções"
    ],
    "dias_aula": ("Seg", "Ter", "Qua", "Qui", "Sex"),
    "carga_horaria": 32
}

# imprime o nome do curso
# print( curso["descrição"] )
# imprime a terceira disciplina
# print( curso["disciplinas"][2] )
# imprime a quarta feira do dias_aula
# print(curso["dias_aula"][2])
# adiciona a chave/valor para o nome da escola.
curso["nome_escola"] = "Ka Solution"

# print(curso)


alunos = ["Julio", "Camilla", "Danielly", "Tawany"]


# print(alunos[0])
# print(alunos[1])
# print(alunos[2])
# print(alunos[3])

# for x in alunos:
#     print(f"Nome do aluno: {x}")

# for x in range(10):
#     print(x)

# for x in range(1, 10):
#     print(x)

# for x in range(1, 10, 2):
#     print(x)

# for x in range(len(alunos)):
#     print(alunos[x])


curso = {
    "descrição": "Programando com python",
    "disciplinas": [
        "Variáveis",
        "Operadores",
        "Condicionais",
        "Coleções"
    ],
    "dias_aula": ("Seg", "Ter", "Qua", "Qui", "Sex"),
    "carga_horaria": 32
}

# for chave, valor in curso.items():
#     print(f"A chave: {chave} tem o valor: {valor}")

# for aluno in alunos:
#     if aluno == "Danielly":
#         print("Achamos o aluno!")
#         break
#     else:
#         print("ainda não achamos!")


x = [1]

for i in x:
    try:
        numero = input("Digite um numero: ")
        numero = int(numero)
        x.clear()
    except:
        print("Erro! Tente novamente: ")


print(f"numero digitado: {numero}")

