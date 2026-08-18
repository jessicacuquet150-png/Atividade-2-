class Funcionario:

    def __init__(self, nome: str, cpf: str, salario: float):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome} = CPF: {self.cpf} = Salário: R$ {self.salario:,.2f}")

    def aumentar_salario(self, percentual: float):
        if percentual > 0:
            self.salario += self.salario * (percentual / 100)
            print(f"Salário de {self.nome} reajustado em {percentual}%. Novo valor: R$ {self.salario:,.2f}")
        else:
            print("O percentual de aumento deve ser maior que zero.")

class Gerente(Funcionario):

    def __init__(self, nome: str, cpf: str, salario: float, setor: str):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def receber_bonificacao(self):
        self.salario += self.salario * 0.10
        print(f"Parabéns, {self.nome},você recebeu uma bonificação de 10% pelo desempenho no setor de {self.setor}! Novo salário: R$ {self.salario:,.2f}")

gerente_tech = Gerente("Carla Mendes", "123.456.789-00", 8500.0, "Tecnologia")
gerente_tech.exibir_dados()
gerente_tech.aumentar_salario(5)
gerente_tech.receber_bonificacao()