

def menu_incial():
    valor_1 = input("Coloque o PRIMEIRO valor: ")
    valor_2 = input("Coloque o SEGUNDO valor: ")

    print("")
    print("="*50)
    print("")
    print("Opções: ")
    print("1 para somar, 2 para subtrair, 3 para dividir ou 4 para multiplicar")
    opcao = input("Coloque o numero da operação desejada: ")
    print("")
    print("="*50)
    print("")

    return valor_1, valor_2, opcao


# soma
def soma(x:int, y:int):

    print(int(x) + int(y))

# subtração (Danielly)
def subtracao(num_1:int,num_2:int):
    try:
        numero_1 = int(num_1)
        numero_2 = int(num_2)
        msg = "Operacao realizada com sucesso!"        
        resultado = numero_1 - numero_2
        codigo_retorno = 0
    except:
        msg = "Numeros inválidos!"
        resultado = 0
        codigo_retorno = 1
    
    return (msg, resultado, codigo_retorno)

# divisão (Tawany)
def divsao(num:int, val:int):
    resultado = 0

    try:
        num = int(num)
        val = int(val)
        resultado = num/val
        msg = "Processado com sucesso!"
    except:
        msg = "Deu erro!!"

    return  resultado, msg

# multiplicação (Camilla)
def multiplicacao (a:int, b:int):
    if type(a) == str or type(b) == str:
        print("Caractere inválido")
    else:
        return (float(a)*float(b))
