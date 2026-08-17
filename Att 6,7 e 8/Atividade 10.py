class Ordem_de_servico:
    total_os_criadas = 0
    os_abertas = 0

    def __init__(self, cliente, descriçao):
        Ordem_de_servico.total_os_criadas += 1
        Ordem_de_servico.os_abertas += 1

        self.id_os = Ordem_de_servico.total_os_criadas
        self.cliente = cliente
        self.descriçao = descriçao
        self.status = "aberta"
        
    def finalizar_os(self):
        if self.status != "Concluída":
            self.status = "Concluída"
            Ordem_de_servico.os_abertas -= 1
    
    @classmethod
    def verificar_os_abertas(cls):
        return cls.os_abertas

os1 = Ordem_de_servico("Maria Antunes", "Troca de tela de aparelhos eletronicos")
os2 = Ordem_de_servico("João Silva", "Formatação de aparelhos")
os3 = Ordem_de_servico("Joana santos", "Manutenção")
os2.finalizar_os()

print(f"id da OS 1: {os1.id_os}  =  Cliente: {os1.cliente}  =  Status: {os1.status}")
print(f"id da OS 2: {os2.id_os}  =  Cliente: {os2.cliente}  =  Status: {os2.status}")
print(f"id da OS 3: {os3.id_os}  =  Cliente: {os3.cliente}  =  Status: {os3.status}")
print("===="*15)
print(f"total de OS criadas: {Ordem_de_servico.total_os_criadas}")
print(f"total de OS abertas: {Ordem_de_servico.verificar_os_abertas()}")
