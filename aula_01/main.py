
# comentário em linha

"""
Comentario em bloco

"""

# VARIÁVEIS (tipagem dinâmica)
# snack case () # CamelCase 

primeiro_nome = "Julio" # Tipo String (texto)
altura = 1.72 # Tipo Real
quantidade_de_produto = 30 # Tipo inteiro
acabou = True # Tipo Boleano
valor_do_produto = 10.34 

# print("O professor "+primerio_nome)
#print(f"O Professor {primeiro_nome}") #Interpolação

#print("DANIELLY")
#print(f"O Professor {primeiro_nome} tem {altura} de altura e tem {quantidade_de_produto} carrinhos") #Interpolação
#print("CAMILLA")
#print (f"o paciente {primeiro_nome} pesa 100kg e mede {altura}, ele está acima do peso")


#print(f"O Professor {primeiro_nome} gastou R$ {quantidade_de_produto*valor_do_produto} comprando {quantidade_de_produto} de produtos") #Interpolação

# MULTIPLAS ATRIBUIÇÕES


#num_1, num_2, num_3 = 10, 20, 30

num_1 = num_2 = num_3 = 10

# print(f"NUM1: {num_1}")
# print(f"NUM2: {num_2}")
# print(f"NUM3: {num_3}")


aluno, bim_1, bim_2, bim_3, bim_4 = "Julio Pereira", 8, 7.8, 6, 7
media = (bim_1 + bim_2 + bim_3 + bim_4)/4

# print(f"Aluno: {aluno}")
# print(f"Bim 01: {bim_1}")
# print(f"Bim 02: {bim_2}")
# print(f"Bim 03: {bim_3}")
# print(f"Bim 04: {bim_4}")
# print(f"Media: {media}")

#cliente = input("Escreva o seu nome: ")
#print(f"Você digitou: {cliente}")


"""
    Escrever um programa em Python que solicite informações de uma pessoas, 
    como nome, idade, peso e altura. Apresentar na tela estas informações.
    Usar a formatação de interpolação

"""

# nome, idade, peso, altura = input("Escreva seu nome: "), input('Qual sua idade: '), input("Qual o seu peso: "), input("Só falta a altura. Diga! ")
# print(f"O cliente: {nome}, tem a idade de  {idade}, peso {peso} e altura de {altura}")

# print
# print(f"Cliente: {input('Escreva seu nome: ')} com idade de {input('Qual sua idade: ')}")




# nome = input ("Escreva seu nome: ")
# idade = input ("Escreva sua idade: ")
# cidade_natal = input ("Escreva sua cidade: ")
# quantos_filhos = input ("Escreva quantos filhos tem: ")
# print (f"Você digitou {nome}")
# print (f"Você digitou {idade}")
# print (f"Você digitou {cidade_natal}")
# print (f"Você digitou {quantos_filhos}")
# print (f"{nome}, tem {idade} anos, mora em {cidade_natal}, e tem {quantos_filhos} filho(s)")





# cliente = input("Escreva o seu nome: ")
# print(f"Você digitou: {cliente}")
# idade = input("Digite sua idade: ")
# print(f"Você digitou: {idade}")
# peso = input("Digite seu peso: ")
# print(f"Você digitou: {peso}")
# altura = input("Digite sua altura: ")
# print(f"Você digitou: {altura}")
# print(f"Nome: {cliente}, Idade: {idade}, Peso: {peso}, Altura {altura} ")