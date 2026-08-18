class Aplicativo:
    def __init__(self, nome, consumo_bateria):
        self.nome = nome
        self.consumo_bateria = consumo_bateria

class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} foi ligado.")

    def executar_app(self, app):
        if not self.ligado:
            print(f"Não é possível executar o aplicativo '{app.nome}'. celular desligado")
        elif self.bateria < app.consumo_bateria:
            print(f"Bateria insuficiente para rodar o app '{app.nome}' Bateria atual: {self.bateria}%")
        else:
            self.bateria -= app.consumo_bateria
            print(f"Executando o aplicativo: '{app.nome}'. Bateria restante: {self.bateria}%")

aplicativo1 = Aplicativo("instagram", 15)
aplicativo2 = Aplicativo("Jogo", 40)

meu_celular = Celular("Samsung", "Galaxy S23")
meu_celular.executar_app(aplicativo1) 
print("      ")

meu_celular.ligar()
meu_celular.executar_app(aplicativo1)
meu_celular.executar_app(aplicativo2)