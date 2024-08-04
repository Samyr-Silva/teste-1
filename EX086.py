# Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o
# número da conta, nome do titular e saldo. Adicione métodos para realizar depósitos e saques.

class ContaBancaria:

    ## construtor
    def __init__(self, num_conta, nome_titular, saldo):
        self.num_conta = num_conta
        self.nome_titular = nome_titular
        self.saldo = saldo


    ## metodo para ver informações
    def ExibirInfo(self):
        print('-'*30)
        print('DADOS ATUALIZADOS'.center(30))
        print('-'*30)
        print(f'\033[1;33mNúmero da conta:\033[m \t{self.num_conta}')
        print(f'\033[1;33mNome do titular:\033[m \t{self.nome_titular}')
        print(f'\033[1;32mSaldo:\033[m \t\t\t\t{self.saldo}')


    ## método pra depositar uma quantia, quantia é passada como parametro, ainda mostra as informacoes com o saldo atual
    def Depositar(self, quantia):
        print(f'\033[4;32mFoi depositado R${quantia} na sua conta\033[m')
        self.saldo += quantia
        self.ExibirInfo()


    ## método pra sacar uma quantia, quantia é passada como parametro, ainda mostra as informacoes com o saldo atual
    def Saque(self, cont):
        print(f'\033[4;31mFoi sacado R${cont} da sua conta\033[m')
        self.saldo -= cont
        self.ExibirInfo()


## Testes com varias pessoas
agente1 = ContaBancaria(85457, 'Romario', 100.0)
agente1.ExibirInfo()
agente1.Depositar(50.0)
agente1.Saque(100.0)

agente2 = ContaBancaria(88569, 'Luiza', 500.0)
agente2.ExibirInfo()
agente2.Saque(245.0)