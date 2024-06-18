# ABSTRAÇÃO
class Calculador:

    def __init__(self):
        try:
            # ATRIBUTOS
            self.num1 = int(input("Coloque o PRIMEIRO valor: "))
            self.num2 = int(input("Coloque o SEGUNDO valor: "))
            self.opcao = input("Coloque o numero da operação desejada: ")

            self.executar_calculador()
        except:
            print("Impossivel criar o OBJETO")
            raise()

    # MÉTODOS
    def soma(self):
        return self.num1 + self.num2
    
    def subtrair(self):
        return self.num1 - self.num2
    
    def dividir(self):
        return self.num1 / self.num2
    
    def mult(self):
        return self.num1 * self.num2
    
    def executar_calculador(self):

        if self.opcao == "1":
            print(f"A soma é: {self.soma()}")
        elif self.opcao == "2":
            print(f"A subtração é: {self.subtrair()}")
        elif self.opcao == "3":
            print(f"A divisão é: {self.dividir()}")
        elif self.opcao == "4":
            print(f"A multiplicação é: {self.mult()}")
        else:
            print("Ops! Opção errada.")

# ===============================================================

Calculador()



    

