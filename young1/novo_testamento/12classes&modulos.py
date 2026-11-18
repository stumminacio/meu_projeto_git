'''
========================================
PRIMEIRA EXPLICAÇÃO DE CLASSES E OBJETOS
========================================

class Casa:
    pass

casa1 = Casa()
casa1.rua = "Rua das Flores"
casa1.bairro = "Centro"
casa1.cep = "12345-678"

print(type(casa1))
print(casa1.rua)
print(casa1.bairro)
print(casa1.cep)
'''
'''
========================================
SEGUNDA EXPLICAÇÃO DE CLASSES E OBJETOS
========================================

class Casa:

    def enderenco_completo(self):
        print(f"Rua: {self.rua}")
        print(f"Bairro: {self.bairro}")
        print(f"CEP: {self.cep}")

    # o self é uma referência para o próprio objeto, ou seja,
    # para a instância da classe. Ele é usado para acessar os
    # atributos e métodos da própria instância.

# aqui acessamos a classe Casa e criamos um objeto chamado casa1, 
# depois atribuímos valores aos atributos do objeto casa1 e 
# chamamos a funcao enderenco_completo() para exibir o 
# endereço completo da casa.

casa1 = Casa()
casa1.rua = "Rua das Flores"
casa1.bairro = "Centro"
casa1.cep = "12345-678"

casa1.enderenco_completo()    
'''
'''
========================================
TERCEIRA EXPLICAÇÃO DE CLASSES E OBJETOS
========================================

class Casa:

    # o metodo __init__ é um método especial em Python que 
    # é chamado automaticamente quando um objeto é criado a 
    # partir de uma classe. Ele é usado para inicializar os 
    # atributos do objeto com valores específicos.

    def __init__(self, rua, bairro, cep):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep

# aqui acessamos a classe Casa e criamos um objeto chamado casa1, 
# passando os valores dos atributos rua, bairro e cep como
# argumentos para o método __init__. Em seguida, imprimimos o
# valor do atributo rua do objeto casa1.

casa1 = Casa("Rua das Flores", "Centro", "12345-678")
print(f"Rua da casa 1: {casa1.rua}) 

casa2 = Casa("Rua das Palmeiras", "Jardim", "98765-432")
print(f"Rua da casa 2: {casa2.rua}")
'''
'''
=========================================
QUARTA EXPLICAÇÃO DE CLASSES E OBJETOS
=========================================

class Casa:

    def __init__(self, rua, bairro, cep):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep

    # o metodo get_bairro() é um método de acesso que retorna 
    # o valor do atributo bairro do objeto já definido. 
    # Ele não recebe nenhum argumento além do self, que é uma 
    # referência para o próprio objeto.
    def get_bairro(self):
        return self.bairro
    # o metodo set_bairro() é um método de modificação que altera
    # o valor do atributo bairro do objeto. Ele recebe um novo
    # valor como argumento e atualiza o atributo bairro com esse
    # valor. Em seguida, ele retorna o novo valor do atributo bairro.
    def set_bairro(self, novo_bairro):
        self.bairro = novo_bairro
        return self.bairro

# aqui acessamos a classe Casa e criamos um objeto chamado casa1,
# passando os valores dos atributos rua, bairro e cep como
# argumentos para o método __init__. Em seguida, chamamos o 
# método get_bairro() para obter o valor do atributo bairro do 
# objeto casa1 e imprimimos o resultado.

casa1 = Casa("Rua das Flores", "Centro", "12345-678")
print(f"Bairro da casa 1: {casa1.get_bairro()}")

# em seguida, chamamos o método set_bairro() para alterar o 
# valor do atributo bairro do objeto casa1 e imprimimos 
# o resultado.

print(f"Alterando o bairro da casa 1 para 'Jardim'")
casa1.set_bairro("Jardim")
print(f"Bairro da casa 1 após alteração: {casa1.get_bairro()}") '''
'''
==========================================
QUINTA EXPLICAÇÃO DE CLASSES E OBJETOS
==========================================

class Casa:

    def __init__(self, rua, bairro, cep):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep

    def get_bairro(self):
        return self.bairro

    def set_bairro(self, novo_bairro):
        self.bairro = novo_bairro
        return self.bairro

    # o metodo __str__ é um método especial em Python que é chamado 
    # quando você tenta imprimir um objeto. Ele retorna uma 
    # representação em string do objeto, que pode ser personalizada 
    # para exibir informações relevantes sobre o objeto.
    def __str__(self):
        return f"Casa localizada na {self.rua}, bairro {self.bairro}, CEP {self.cep}"

casa1 = Casa("Rua das Flores", "Centro", "12345-678")
# aqui chamamos o método __str__() implicitamente ao tentar
# imprimir o objeto casa1. O método retorna uma string que
# descreve a casa, incluindo a rua, o bairro e o CEP.
print(casa1)'''
'''
==========================================
SEXTA EXPLICAÇÃO DE CLASSES E OBJETOS
==========================================

class Equipe:
    
    def __init__(self, jogadores):
        self.jogadores = jogadores

    # o metodo __len__ é um método especial em Python que é chamado
    # quando você usa a função len() em um objeto. Ele retorna o
    # número de elementos ou a "tamanho" do objeto, que pode ser
    # personalizado para refletir a quantidade de elementos que o
    # objeto contém. No caso da classe Equipe, o método __len__
    # retorna o número de jogadores na equipe, que é obtido a
    # partir do atributo jogadores.
    def __len__(self):
        return len(self.jogadores)

equipe1 = Equipe(["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4"])
# aqui chamamos o método __len__() implicitamente ao usar a função
# len() no objeto equipe1. O método retorna o número de jogadores
# na equipe, que é 4, e imprimimos o resultado.
print(f"Número de jogadores na equipe 1: {len(equipe1)}")'''

'''
===========================================
EXERCÍCIOS DE CLASSES E OBJETOS
===========================================
'''
'''
============================================
PRIMEIRO EXERCÍCIO DE CLASSES E OBJETOS
============================================

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

pessoa1 = Pessoa("Inácio", 13)
print(pessoa1)'''