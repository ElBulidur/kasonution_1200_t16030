# ABSTRAÇÃO
class Pessoa:
    # PROPRIEDADES ou ATRIBUTOS
    def __init__(self, nome):
        self.nome = nome.upper()
        # self.sala = ""
        # self.carrilho_compra = 0

    # MÉTODOS / FUNÇÕES
    def fazer_login(self, user, password):
        usuario = "master"
        senha = "admin"

        if user == usuario and password == senha:
            return True
        else:
            return False

# OBJETO
cliente = Pessoa("Julio")
aluno = Pessoa("camilla")

#cliente.carrilho_compra = 290.90

print(f"ABSTRAÇÃO: {Pessoa}")

print(f"OBJETO: {cliente}")

print(f"ATRIBUTO: {cliente.nome}")


if cliente.fazer_login("master", "ad") == True:
    print("Logado com sucesso")
else:
    print("login errado!")
