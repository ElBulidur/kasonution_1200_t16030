# random => numeros aleatorios
# import random
# numero = random.random() # numeros decimais aleatorio.
# numero = random.randint(1, 30) # numeros inteiro aleatorio dentro e um intervalo.

# import random as rd
# numero = rd.random() # numeros decimais aleatorio.
# numero = rd.randint(1, 30) # numeros inteiro aleatorio dentro e um intervalo.

# from random import *
# numero = random() # numeros decimais aleatorio.
# numero = randint(1, 30) # numeros inteiro aleatorio dentro e um intervalo.

# from random import random, randint

# numero = random()
# numero = randint(1, 30)

# from random import random as rd, randint as rdi

# numero = rd()
# numero = rdi(1, 30)

# print(numero)

# import statistics as sts

# numeros = [10, 10,10]

# print(sts.mean(numeros))


# FUNÇÕES

# retorno
# parametros

# Funcão que não retorna nada e  não tem parametros
def imprimir_ola():
    print("Ola mundo!")

# Funcão que retorna e  não tem parametros
def msg_ola():
    return "Ola por retorno"

# Funcão que não retorna e tem parametros
def msg_para_usuario(nome_usuario):
    try: 
        int(nome_usuario)
        print("Precisa ser o nomme do usuario")
    except:
        print(f"{nome_usuario} seja bem vindo!!!")


# Funcão que retorna e tem parametros
def somar(a, b):
    return a + b

# Funcão que não retorna e tem parametros com valor padrão
def gera_desconto(valor, desconto=0.1):
    print(f"Valor ajustado {valor*desconto}")


# retorno = imprimir_ola()
# msg_para_usuario(1)
# resultado_soma = somar(23, 56)
# print(resultado_soma)

# gera_desconto(100)

print(f"Imprimindo do arquivo MODULOS: {__name__}")
