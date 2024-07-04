''' --> Implemente uma classe chamada “Biblioteca” que represente uma
biblioteca virtual. Essa classe deve permitir cadastrar livros,
fazer empréstimos, devolver livros e verificar a disponibilidade de um livro. <-- '''

## LISTA COM OS LIVROS CADASTRADOS
livros_cadastrados = []
class Biblioteca:
    ##CONSTRUTOR
    def __init__(self, nome_livro):
        self.nome_livro = nome_livro

    ##MÉTODO DE CADASTRAR UM LIVRO
    def CadastrarLivro(self):
        livros = []
        print(f'O livro "{self.nome_livro}" foi cadastrado!!')
        livros_cadastrados.append(self.nome_livro)

    ##MÉTODO PRA REQUISITAR UM LIVRO
    def PedirLivro(self):
        if self.nome_livro not in livros_cadastrados:
            print(f'O livro "{self.nome_livro}" não temos em nossa biblioteca!')
        else:
            print(f'Foi requisitado o livro "{self.nome_livro}"')
            livros_cadastrados.remove(self.nome_livro)

    ##MÉTODO PARA DEVOLVER UM LIVRO
    def DevolverLivro(self):
        if self.nome_livro in livros_cadastrados:
            print(f'O livro "{self.nome_livro}" já está na biblioteca!!')
        else:
            print(f'O livro "{self.nome_livro}" foi adicionado novamente a biblioteca!!')
            livros_cadastrados.append(self.nome_livro)

    ##MÉTODO PRA CHECAR A DISPONIBILIDADE DE UM LIVRO
    '''def Disponibilidade(self, nome):
        if nome in livros_cadastrados:
            print(f'Temos o livro "{nome}" na biblioteca!!')
        else:
            print(f'Não temos o livro "{nome}" na biblioteca!!')
            res = str(input('Quer cadastrar [ S/N ]:')).strip().upper()[0]
            if res == 'S':
                nome = self.CadastrarLivro()'''

##FUNÇÃO PRA MOSTRAR OS LIVROS CADASTRADOS
def MostrarLivros():
    for c, l in enumerate(livros_cadastrados):
        print(f'{c+1}º -\t\t{l}')

##RESOLVER O PROBLEMA DE NOA ESTA CONSEGUINDO VER A DISPONIBILIDADE CORRETAMENTE
def Disponibilidade(nome):
    if nome in livros_cadastrados:
        print(f'Temos o livro "{nome}" na biblioteca!!')
    else:
        print(f'Não temos o livro "{nome}" na biblioteca!!')
        res = str(input('Quer cadastrar [ S/N ]:')).strip().upper()[0]
        if res == 'S':
           pass



livro_1 = Biblioteca('Não Mais')
livro_1.CadastrarLivro()
livro_2 = Biblioteca('Amar? AMEI!')
livro_2.CadastrarLivro()
livro_3 = Biblioteca('Cansei de falar')
livro_3.CadastrarLivro()
livro_4 = Biblioteca('THOR')
livro_4.CadastrarLivro()
livro_5 = Biblioteca('Capitºao')
livro_5.CadastrarLivro()
livro_6 = Biblioteca('AMERICA%')
livro_6.CadastrarLivro()
livro_1.PedirLivro()
livro_1.DevolverLivro()
#livro_2.Disponibilidade('Não Mais')
Disponibilidade('TARANTULS')
