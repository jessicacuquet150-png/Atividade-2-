class Animal:

    def __init__(self, nome: str, especie: str):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print("Este animal faz um som generico.")


class Cachorro(Animal):

    def __init__(self, nome: str, raca: str):
        super().__init__(nome=nome, especie="Canino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) diz: Au Au!")

class gato(Animal):

    def __init__(self, nome: str, raca: str):
        super().__init__(nome=nome, especie="felino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) diz: Miau")

class vaca(Animal):

    def __init__(self, nome: str, raca: str):
        super().__init__(nome=nome, especie ="Bovinio")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) diz: Muuuu")

Rex = Cachorro(nome="Rex", raca="Pitibul")
Tom = gato(nome="Tom", raca="Sianes")
Mimosa = vaca(nome="Mimosa", raca="Neolore")

animais = [Rex, Tom, Mimosa]

for animal in animais:
    animal.fazer_som()

