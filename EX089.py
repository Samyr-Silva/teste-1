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


##FUNÇÃO PRA MOSTRAR OS LIVROS CADASTRADOS
def MostrarLivros():
    for c, l in enumerate(livros_cadastrados):
        print(f'{c+1}º -\t\t{l}')


##CHECA A DISPONIBILIDADE DE UM LUVRO
def Disponibilidade(nome):
    if nome in livros_cadastrados:
        print(f'Temos o livro "{nome}" na biblioteca!!')
    else:
        print(f'Não temos o livro "{nome}" na biblioteca!!')
        res = str(input('Quer cadastrar[ S/N ]: ')).strip().upper()[0]
        while res not in 'SN':
            res = str(input('Quer cadastrar[ S/N ]: ')).strip().upper()[0]
        if res == 'S':
            print('O livro foi adicionado a biblioteca!!')
            livros_cadastrados.append(nome)
        else:
            print(f'O livro "{nome}" não foi adicionado a bilbioteca!!')


livro_1 = Biblioteca('Não Mais')
livro_1.CadastrarLivro()
livro_2 = Biblioteca('Cansei de falar')
livro_2.CadastrarLivro()
livro_3 = Biblioteca('THOR')
livro_3.CadastrarLivro()
livro_4 = Biblioteca('AMERICA%')
livro_4.CadastrarLivro()
livro_1.PedirLivro()
livro_1.DevolverLivro()
Disponibilidade('Não Mais')
MostrarLivros()
