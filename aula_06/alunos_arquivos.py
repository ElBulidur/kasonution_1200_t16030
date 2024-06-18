import os
import csv
import pandas as pd
import openpyxl


try:
    arquivo = "notas_alunos.xlsx"

    if os.path.exists(arquivo): # tem arquivo
        print("Já te o arquivo na pasta!")

    pasta = "../aula_012"

    if os.path.isdir(pasta): # tem a pasta
        print("Tem a pasta!")

    # print( os.getcwd()) # C:\projetos python\aula_06

    # os.chdir("../programa") # navegar até a pasta desejada
    
    # print( os.getcwd()) # C:\projetos python\programa

    # os.mkdir("novos_arquivos") # Cria pasta

    # os.rmdir("novos_arquivos") # remove pasta

    # print( os.listdir() ) # listar arquivos e pastas em um diretorio

    # os.system("cls") # comando

    alunos_novos = [
        ["Julio", "julio@email"],
        ["Celso", "celso@email"]
    ]

    arg_csv = open("alunos_novos.csv", "w")

    # gravar = csv.writer(arg_csv, delimiter=";")

    # gravar.writerow(["Nome", "Email"])
    # gravar.writerows(alunos_novos)

    arg_csv.close()



# EXCEL


    pasta = openpyxl.load_workbook(filename="vendas.xlsx")

    dados = []

    for x in pasta["Principal"].iter_rows(values_only=True):
        dados.append(x)

    print(dados)









   












    

    

    





except:
    print("Arquivo não encontrado!")