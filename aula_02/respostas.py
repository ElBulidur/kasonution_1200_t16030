"""
    Laboratório 2
        Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. Usando operações de
        divisão inteira e resto da divisão, escrever um programa que solicite ao usuário um valor para saque e, a partir
        deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do
        saque.

        Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor
        quantidade possível de cédulas.


        55 = 1,0,0,1 

"""
# pegar o valor para saque
# Criar variaveis para adicionar a quantidade das cédulas.

# Valor_Saque = float (input (" digite valor multiplo de 5,10,20,50: "))
# div_real_5 = Valor_Saque / 5
# div_real_10 = Valor_Saque / 10
# div_real_20 = Valor_Saque / 20
# div_real_50 = Valor_Saque / 50
# print(f"Notas de 5: {div_real_5}")
# print(f"Notas de 10: {div_real_10}")
# print(f"Notas de 20: {div_real_20}")
# print(f"Notas de 50: {div_real_50}")


valor_saque = valor = 135 #float(input ("Digite valor multiplo de 5: ")) # 55


if valor_saque % 5 != 0:
    print("Este caixa aceita somente multiplos de 5!")
else:
    c50 = c20 = c10 = c5 = 0
    
    if valor_saque >= 50:
        c50 = valor_saque // 50 
        # valor_saque = valor_saque % 50 # 5
        valor_saque %= 50 

    if valor_saque >= 20:
        c20 = valor_saque // 20 # 0
        valor_saque = valor_saque % 20 # 5
    
    if valor_saque >= 10:
        c10 = valor_saque // 10
        valor_saque = valor_saque % 10
    
    if valor_saque >= 5: c5 = valor_saque // 5

    # print(f"Saque de: {valor} | {int(c50)} notas de 50,00, {c20} notas de 20,00, {c10} notas de 10,00 e {c5} notas de 5,00.")
    
    

nome =  "julio pereira"

print(nome)
print(nome[0])
print(nome[-1])
print(nome[4:7])
print(nome.capitalize())
print(nome.upper())
print(nome)




lista = [0, 1.2, "julio", True]