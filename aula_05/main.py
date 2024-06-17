import modulo_calc as calc

print("="*30 + " PROGRAMA CALCULADORA " + "="*30)

num_1, num_2, opcao = calc.menu_incial()

if opcao == "1":
    calc.soma(num_1, num_2)
elif opcao == "2":
    msg, resultado, codigo = calc.subtracao(num_1, num_2)

    if codigo == 0:
        print(msg)
        print(f"Resultado: {resultado}")
    else:
        print(msg)
elif opcao == "3":
    resultado, msg = calc.divsao(num_1, num_2)

    if resultado < 1:
        print(msg)
    else:
        print(msg)
        print(f"Resultado: {resultado}")
elif opcao == "4":
    resultado = None
    
    try:
        resultado = calc.multiplicacao(int(num_1), int(num_2))
    except:
        print("Erro de entrada de dados!!!")


    if not resultado:
        print("Fim do programa!!!")
    else:
        print(f"Resultaod:{resultado}")



