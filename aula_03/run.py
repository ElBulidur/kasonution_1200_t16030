
# VARIÁVEIS
# STRING, INTEIRO, FLOAT(REAL), BOLEANA
# =

# ENTRADA E SAÍDA DE INFORMAÇÕES
# INPUT() => ENTRADA
# PRINT() => SAÍDA

# OPERADORES
# +-*/ MATEMÁTICO
# == >= > < != RELACIONAL
# or, and LÓGICOS

# ESTRUTURA CONDICIONAL
# IF, ELIF e ELSE

# COLEÇÕES

# Se ela é mutável ou não.
# Se os métodos dela retorna ou não informação.a

# nome = "julio"
# retorno = print(nome)
# nome_maiusculo = nome.istitle()
# print(nome_maiusculo)
# print(retorno)

# LISTA, DICIONARIO E TUPLAS

# LISTA
dados_aluno = ["Julio Pereira", 1.72, 26, False, [6, 7, 5, 0], 26]

situacao = "Aprovado" if dados_aluno[3] == True else "Reprovado"
media = sum(dados_aluno[4]) / len(dados_aluno[4])

# print(f"Nome do Aluno: {dados_aluno[0]}")
# print(f"Altura do Aluno: {dados_aluno[1]}")
# print(f"Idade do Aluno: {dados_aluno[2]}")
# print(f"Situação do Aluno: {situacao}")
# print(f"Media do Aluno: {media}")

# METODOS DE LISTA

# dados_aluno = [34, 65, 78, 34, 56] # Usado para o metodo sort

# print(dados_aluno)

# dados_aluno.append(["Aprovado", "Mais bagunçeiro"]) # adiciona informação no final da lista
# dados_aluno.clear() # Limpa a lista
# qtd_valor_na_lista = dados_aluno.count('Julio Pereira') # retorna quantidade de registros
# dados_aluno.sort() # ordena os valores
# print(dados_aluno.pop(0)) # Remove o elemento com base no indice e retorna o elemento.
# dados_aluno.remove(26) # remove o primeiro valor encontrado

# print(dados_aluno)

#Exemplo
# lista_amigos = [1, 4, 6,7]
# lista_ex_amigos = []


# lista_ex_amigos.append(lista_amigos.pop(1))

# print(lista_amigos)
# print(lista_ex_amigos)


# DICIONÁRIO

dicionario = {"chave1": "valor1", "chave2":"valor2"} # SINTAXI

dados_aluno_1 = {
    "nome": "Julio Pereira",
    "altura": 1.72,
    "idade": 26,
    "situacao": False,
    "notas": [6, 7, 5, 0]
}

dados_aluno_2 = {
    "nome": "Camilla",
    "altura": 1.90,
    "idade": 26,
    "situacao": False,
    "notas": [6, 7, 5, 0]
}

# print(dados_aluno)
# print(dados_aluno["nome"])
# print(dados_aluno.get("IPVA"))

# dados_aluno["ferias"] = True

alunos = {
    "aluno_1": dados_aluno_1,
    "aluno_2": dados_aluno_2
}

# print(dados_aluno)

# cliente = {}

# print(cliente)

# cliente["nome"] = "Julio"
# cliente["idade"] = 26
# # nome_cliente = cliente["nome"]

# print(cliente)

# cliente["idade"] = 60

# print(cliente)

# print(dados_aluno_1.keys()) # retorna as chaves
# print(dados_aluno_1.values()) # retorna os valores
# print(dados_aluno_1.items()) # retorna chave e valor


# #TUPLA

# dias_da_semana = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom")
# amizades = [(1,2), (1,5)]
# dias_trabalhados = [(0, 1, 2, 4)]

# print(relacionamento.count(23))  # retorna numeros de vezes que o registro repete.


