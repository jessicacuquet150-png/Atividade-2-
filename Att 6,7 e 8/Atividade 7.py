class Bicicleta:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.velocidade = 0

    def pedalar(self):
        if self.velocidade < 60:
            self.velocidade = min(self.velocidade + 5, 60)
            print(f"A bike {self.modelo} acelerou   Velocidade: {self.velocidade} km")
        else:
            print(f"A bike {self.modelo}  está na velocidade máxima")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade = max(self.velocidade - 5, 0)
            print(f"Reduzindo velocidade: {self.velocidade} km")
        else:
            print("A bike parou")

    def radar_de_velocidade(self):
        print(f"RADAR: Velocidade atual da bike {self.modelo}: {self.velocidade} km")

minha_bike = Bicicleta("Gios")

print("====== Pedalando =======")
minha_bike.pedalar()  
minha_bike.pedalar() 

print("\n====== Conferindo radar ======")
minha_bike.radar_de_velocidade() 

print("\n====== Freando bike ======")
minha_bike.frear() 
minha_bike.frear()  
minha_bike.frear()