# REQUESTS
# METHODOS
# 
import requests, json
from database import *


endpoint = "https://667370916ca902ae11b4360f.mockapi.io/usuarios"


#CREATE
# usuario = {
#     "nome": "NOVO USUARIO",
#     "email": "emailnovo@hotmail.com",
#     "senha": "bFasasV"
# }


# resposta = requests.post(url=endpoint, data=usuario)

# print(resposta)


# READ

# resposta = requests.get(url=endpoint)

# conteudo = json.loads(resposta.content)

# print(conteudo[0])

# criar_usuario(
#     conteudo[0]['nome'], 
#     conteudo[0]['email'], 
#     conteudo[0]['senha']
# )

# for linha in conteudo:
#     criar_usuario(
#     linha['nome'], 
#     linha['email'], 
#     linha['senha']
# )


#UPDATE
# id = 51
# dados_atualizar = {
#     "nome": "MEU NOVO NOME",
#     "email": "emailnovo@hotmail.com",
#     "senha": "bFasasV"
# }

# url_atualizar = f"{endpoint}/{id}"

# resposta = requests.put(url=url_atualizar, data=dados_atualizar)

# print(resposta.status_code)


#DELETE
# id = 2
# url_deletar = f"{endpoint}/{id}"

# resposta = requests.delete(url=url_deletar)

# print(resposta.status_code)






