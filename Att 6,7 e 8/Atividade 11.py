class CofreDigital:
    """
    Classe que simula um cofre digital usando Programação Orientada a Objetos (POO).
    Demonstra o conceito de ENCAPSULAMENTO: oculta os dados sensíveis (__senha e __saldo)
    e expõe apenas métodos seguros de interação.
    """

    def __init__(self, titular: str, senha: str):
        # Atributo Público: Pode ser lido e alterado diretamente por fora da classe.
        self.titular = titular

        # Validação da Senha: Exige que seja uma string com exatamente 4 números.
        if not (isinstance(senha, str) and len(senha) == 4 and senha.isdigit()):
            raise ValueError("A senha deve ser uma string com exatamente 4 dígitos.")

        # Atributos Privados (prefixados com __): 
        # Não podem ser acessados diretamente fora da classe (ex: cofre.__saldo geraria erro).
        self.__senha = senha
        self.__saldo = 0.0

    @property
    def saldo(self) -> float:
        """
        GETTER (Propriedade de leitura): Permite consultar o saldo (cofre.saldo)
        sem expor o atributo privado para modificações diretas (ex: cofre.saldo = 1000 lança erro).
        """
        return self.__saldo

    def depositar(self, valor: float) -> None:
        """Aumenta o saldo do cofre se o valor for válido."""
        # Regra de negócio: impede depósitos negativos ou nulos
        if valor <= 0:
            print("-Erro:O valor do deposito deve ser positivo.")
            return

        # Alteração segura do atributo privado
        self.__saldo += valor
        print(f"-Deposito de R$ {valor:.2f} realizado.Saldo atual: R$ {self.__saldo:.2f}")

    def sacar(self, valor: float, senha_informada: str) -> None:
        """Realiza retiradas aplicando 3 camadas de validação."""
        # 1ª Validação: Segurança (senha precisa ser idêntica à cadastrada)
        if senha_informada != self.__senha:
            print("-Senha incorreta.Acesso foi negado.")
            return

        # 2ª Validação: Integridade (não permite valores <= 0)
        if valor <= 0:
            print("-Erro:O valor do saque deve ser positivo.")
            return

        # 3ª Validação: Saldo (não permite saldo negativo)
        if valor > self.__saldo:
            print(f"-Saldo insuficiente.Saldo disponível é: R$ {self.__saldo:.2f}")
            return

        # Execução do saque após passar em todas as verificações
        self.__saldo -= valor
        print(f"-Saque de R$ {valor:.2f} realizado com sucesso.Saldo restante: R$ {self.__saldo:.2f}")


# EXECUÇÃO DO CÓDIGO (PASSO A PASSO)

# Cria o cofre para Carlos com a senha "1234". Atributo __saldo inicia com 0.0
cofre = CofreDigital("Carlos", "1234")

# Tentativa 1: Falha porque o valor é negativo (-50 <= 0)
cofre.depositar(-50) 

# Tentativa 2: Sucesso! Saldo atualizado de 0.0 para 200.0
cofre.depositar(200.0) 

# Leitura segura: Usa o método decorado com @property para ler o saldo atual (200.0)
print(f"-Consulta segura de saldo: R$ {cofre.saldo:.2f}")

# Tentativa 3: Falha na 1ª validação ("0000" é diferente da senha real "1234")
cofre.sacar(50.0, "0000") 

# Tentativa 4: Falha na 3ª validação (Valor 300.0 é maior que o saldo atual de 200.0)
cofre.sacar(300.0, "1234")

# Tentativa 5: Sucesso! Passa nas 3 validações. Saldo final: 200.0 - 50.0 = 150.0
cofre.sacar(50.0, "1234")