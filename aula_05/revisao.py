# FUNÇÃO
# sem retorno e sem parammetro
#Criando
def imprimir_ola():
    print("Ola mundo!")

#Executando
# imprimir_ola()

# com retorno e sem parametro
def msg_boasvindas():
    # definir o horario do dia.
    hora = 16
    if hora < 12:
        return "Bom dia para você!"
    elif hora < 18:
        return "Boa tarde para você!"
    else:
        return "Boa noite para você!"


boas_vindas = msg_boasvindas()

# print(boas_vindas)


# sem retorno e com parametro
def msg_bem_vindo_usuario(nome_usuario: str):
    print(f"{nome_usuario.capitalize()}, seja bem vindo!")

# msg_bem_vindo_usuario("julio")

# com retorno e com parametro
def define_valor_total_produto(valor_produto, quantidade):
    return valor_produto * quantidade


valor_total = define_valor_total_produto(35.92, 43)

# print(valor_total)

# com retorno e com parametro opcionais(com valor padrão)
def definir_desconto(valor, desconto=0.1):
    if desconto > 0.3:
        desconto = 0.3

    return valor * desconto

valor_com_desconto = definir_desconto(100)

# print(valor_com_desconto)



