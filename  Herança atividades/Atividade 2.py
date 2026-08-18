class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100

    def acelerar(self):
        if self.combustivel >= 5:
            self.combustivel -= 5
            print(f"O carro acelerou,combustível restante: {self.combustivel}%")
        else:
            print("Sem combustível suficiente para acelerar")

    def painel(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Combustível: {self.combustivel}%")

class CarroEletrico(Carro):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.bateria = 100

    def acelerar(self):
        if self.bateria >= 5:
            self.bateria -= 5
            print(f"O carro elétrico acelerou silenciosamente,bateria restante: {self.bateria}%")
        else:
            print("Bateria insuficiente,recarregue o veículo para acelerar.")

    def recarregar(self):
        self.bateria = 100
        print("Bateria recarregada para 100%")

    def painel(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Bateria: {self.bateria}%")

meu_eletrico = CarroEletrico("Tesla", "Model 3")

meu_eletrico.painel()
meu_eletrico.acelerar()
meu_eletrico.acelerar()
meu_eletrico.painel()
meu_eletrico.recarregar()
meu_eletrico.painel()