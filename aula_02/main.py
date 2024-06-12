
# pega o primeiro
numero_1 = 5 #int(    input("Coloque o primeiro número (Só numero): ")     ) # 30

# pega o segundo
numero_2 = 1 # int( input("Coloque o segundo número (Só numero): ") )# 23


# OPERADORES ARITMÉTICOS
soma = numero_1 + numero_2  # soma
subtracao = numero_1 - numero_2 # subtracao
divisao = numero_1 / numero_2 # divisão
multiplicacao = numero_1 * numero_2 # multiplicação
media = (numero_1 + numero_2) / 2 # media

#soma = soma + 2 # forma completa
soma += 2 # forma reduzida

#subtracao = subtracao - 2 # forma completa
subtracao -= 2

#divisao = divisao / 2 # forma completa
divisao /= 2

#multiplicacao = multiplicacao * 2 # forma completa
multiplicacao *= 2

# DIVISÃO
div1 = numero_1 / numero_2 # Divisão Real
div2 = numero_1 // numero_2 # Divisão Inteira
div3 = numero_1 % numero_2 # Resto da divisão inteira



# imprime o tipo da variavel numero_1
# print(type(numero_1)) #class str

# imprime a variavel soma
# print(f"Soma: {soma}")
# print(f"Subtracao: {subtracao}")
# print(f"Divisao: {divisao}")
# print(f"Multiplicacao: {multiplicacao}")
# print(f"Media: {media}")

# print(f"Divisão Real: {div1}") # 1.3043478260869565
# print(f"Divisão Inteira: {div2}") # 1.0
# print(f"Resto da divisão inteira: {div3}") # 7.0


# pega o primeiro
num_1 = "20" #input("Coloque o primeiro número (Só numero): ") # 30

# pega o segundo
# num_2 = input("Coloque o segundo número (Só numero): ") # 23

# try:
#     num_1 = int(num_1)
# except:
#     pass


# n1 = 200
# n2 = 150

# OPERADORES RELACIONAIS E LÓGICOS
# print(n1 == n2) # iGUAL
# print(n1 != n2) # DIFERENTE
# print(n1 < n2) # MENOR
# print(n1 > n2) # MAIOR


# print(n1 > n2 or n1 == n2) # duas condições, mas só um precisa para ser verdadeiro
# print(n1 > n2 and n1 == n2) # duas condições e elas tem que ser verdadeira.

# print(num_1.isdigit())

if num_1.isdigit():
    num_1 = int(num_1)

    if num_1 > 1:
        print("O numero digitado é maior do que 01")

# print(type(num_1))

# nota_aluno = input("Coloque a nota do aluno: ")

# Imprime Aprovado se a nota for 7 para mais.
# Recuperação de for de 6 a 6.9
# Reprovado de for até 5.9

# nota_aluno = float(input("Coloque a nota do aluno: "))
# if nota_aluno >= 7:
#     print("Aluno aprovado")
# else:
#     print("Aluno reprovado")

# nota_aluno = float (input ("Coloque a nota do aluno: "))
# if nota_aluno >= 7:
#     print ("Aprovado")
# if nota_aluno < 7:
#     print ("Reprovado")

# Imprime Aprovado se a nota for 7 para mais.
# Recuperação de for de 6 a 6.9
# Reprovado de for até 5.9

nota_aluno = float (input ("Coloque a nota do aluno: "))

# EXEMPLO1
if nota_aluno == 0:
    pass
elif nota_aluno >= 7:
    print("APROVADO!")
elif nota_aluno >= 6:
    print("RECUPERAÇÃO!")
else:
    print("REPROVADO!!!")


# EXEMPLO2
# if nota_aluno == 0:
#     pass
# if nota_aluno >= 7:
#     print("APROVADO!")
# if nota_aluno >= 6 and nota_aluno < 7:
#     print("RECUPERAÇÃO!")
# if nota_aluno < 6:
#     print("REPROVADO!!!")

