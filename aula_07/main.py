# PIP
# VENV
import pandas as pd


alunos = {
    "nome": ["Julio", "Celso", "Danielly"],
    "notas": [90, 76, 50]
}

# df_alunos = pd.DataFrame(alunos)

# print(df_alunos.describe())

# df_alunos.to_excel("notas_alunos.xlsx")

# df_alunos.plot()

# LENDO DO ARQUIVO

df = pd.read_excel("arquivos/tab09.xls")

print(df.head())


