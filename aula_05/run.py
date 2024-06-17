# FUNÇÃO COM LISTA DE PARAMETROS

def somar_carrinho(*args):
    total_a_pagar = 0

    for x in args:
        total_a_pagar += x
    
    print(total_a_pagar)


# somar_carrinho(10, 45, 48, 23,34)


def calcular_taxas_impostos(valor:int, **kargs):
    valor_ajustado = valor
    
    if kargs.get("taxa"):
        valor_ajustado = valor + kargs.get("taxa")

    if kargs.get("inss"):
        valor_ajustado = valor + kargs.get("inss")

    if kargs.get("icms"):
        valor_ajustado = valor + kargs.get("icms")

    if kargs.get("desconto"):
        valor_ajustado = valor * kargs.get("desconto")

    print(valor_ajustado)

calcular_taxas_impostos(200.00, taxa=50, icms=23, desconto=.3)