class PetVirtual:
    def __init__(self, nome: str):
        self.nome = nome
        self.fome = 5
        self.felicidade = 5

    def alimentar(self):
        if self.fome > 0:
            self.fome = max(0, self.fome - 2)
            print(f"{self.nome} Animal alimentado   -> Fome atual: {self.fome}")
        else:
            print(f"{self.nome} Ele está de barriga cheia")

    def brincar(self):
        self.felicidade += 2
        self.fome += 1
        print(f"Voce brincou com {self.nome}   -> Felicidade: {self.felicidade}   Fome: {self.fome}")

    def status(self):
        print(f"\n ======= Status de {self.nome.upper()} ======== ")
        print(f"Fome: {self.fome}   Felicidade: {self.felicidade}")
        
        if self.fome >= 8:
            print(f"Atenção: {self.nome} precisa comer!")
        print("  \n")

meu_pet = PetVirtual("Faiska")

meu_pet.status()
meu_pet.brincar()
meu_pet.brincar()
meu_pet.alimentar()
meu_pet.alimentar()
meu_pet.alimentar()
meu_pet.status()
