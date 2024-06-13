"""
    Laboratório 3

    Em um clube, o valor da entrada varia de acordo com a idade do associado.
    Os critérios são:

        - Até 17 anos - R$ 50,00;
        - Entre 18 e 59 anos - R$ 60,00;
        - A partir de 60 anos - R$ 20,00.

    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago.
"""

# CAMILLA
# nome_associado = input ("Digite seu nome: ")
# idade_associado = int (input ("Digite sua idade: "))
# if idade_associado < 18:
#     entrada = 50.00
# elif idade_associado > 17 and idade_associado < 60:
    # entrada = 60.00
# else:
#     entrada = "{:.2f}".format(20.00)

# print (f"{nome_associado}, irá pagar {entrada} reais")


#DANIELLY
# nome_associado = input ("Digite seu nome: ")
# idade_associado = int(input ("Digite sua idade: "))

# if idade_associado <= 17:
#     print(f"Nome do Associado: {nome_associado} - Valor do Ingresso: R$50,00")
# elif idade_associado >=18 and idade_associado <= 59:
#      print(f"Nome do Associado: {nome_associado} - Valor do Ingresso: R$60,00")
# else:
#      print(f"Nome do Associado: {nome_associado} - Valor do Ingresso: R$20,00")

# nome_associado = input ("Digite o nome do associado: ")
# idade_associado = int (input ("Digite a idade do associado: "))
# if idade_associado <= 17:
#     entrada = 50.00
# elif idade_associado >= 18 and idade_associado < 60:
#     entrada = 60.00
# else:
#     entrada = 20.00
# print (f"{nome_associado}, irá pagar {entrada} reais")

# capturando os dados do usuário
nome = input ("digite seu nome: ")
idade = int (input ("digite sua idade: "))

# definindo valor da entrada
if idade <= 17:    entrada = 50.00
elif idade > 17 and idade < 60:    entrada = 60.00
else:    entrada = 20.00

# imprimindo resultado
print (f"{nome} vai pagar {entrada} reais")

