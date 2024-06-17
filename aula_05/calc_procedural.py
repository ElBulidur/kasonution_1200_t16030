valor_1 = int(input("Coloque o PRIMEIRO valor: "))
valor_2 = int(input("Coloque o SEGUNDO valor: "))

print("")
print("="*50)
print("")
print("Opções: ")
print("1 para somar, 2 para subtrair, 3 para dividir ou 4 para multiplicar")
opcao = input("Coloque o numero da operação desejada: ")
print("")
print("="*50)
print("")

if opcao == "1":
    print(f"A soma de {valor_1} com {valor_2} é: {valor_1 + valor_2}")
elif opcao == "2":
    print(f"A subtração de {valor_1} com {valor_2} é: {valor_1 - valor_2}")
elif opcao == "3":
    print(f"A divisão de {valor_1} com {valor_2} é: {valor_1 / valor_2}")
elif opcao == "4":
    print(f"A multiplicação de {valor_1} com {valor_2} é: {valor_1 * valor_2}")
else:
    print("Esta opção não existe!!!")

