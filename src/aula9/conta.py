import datetime

class Conta:
    "Essa classe representa informações sobre as contas de clientes."
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.historico = Historico()

    # Metodo depositar
    def deposita(self, valor):
        self.__saldo += valor
        self.historico.transacoes.append("deposito de {}".format(valor))

    # Metodo saque
    def saca(self, valor):
        if (self.__saldo < valor):
            return False
        else:
            self.__saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
    
    # Metodo transferência
    def transfere_para(self, destino, valor):
        """ Efetua uma transferência entre contas

        Args:
            destino (float): Conta destino
            valor (float): Valor a ser transferido

        Returns:
            bool: Um booleano informando se a transação aconteceu ou não.
        """
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferência de {} para conta {}".format(valor, destino._numero))
            return True
    def get_saldo(self):
        return self.__saldo

    # Metodo extrato
    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self._numero, self.__saldo))
        self.historico.transacoes.append("Demonstrativo saldo de {}".format(self.__saldo))


class Cliente:
    "Essa classe representa informações sobre os clientes."

    def __init__(self, nome, sobrenome, cpf) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def get_nome(self):
        print("imprimindo @setter nome()")
        self._nome.tittle()

    def set_nome(self, nome):
        print("imprimindo @setter nome()")
        self._nome = nome

class Historico:
    "Essa classe representa informações sobre o histórico de transações"

    def __init__(self) -> None:
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("Data da abertura: {}". format(self.data_abertura))
        print("Transações: ")
        for i in self.transacoes:
            print("-", i)

    