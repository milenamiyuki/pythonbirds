class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 46):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    milena = Pessoa(nome = 'Milena')
    angela = Pessoa(milena, nome = 'Angela')
    print(Pessoa.cumprimentar(angela))
    print(id(angela))
    print(angela.cumprimentar())
    print(angela.nome)
    print(angela.idade)
    for filho in angela.filhos:
        print(filho.nome)