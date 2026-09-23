print(" ")
'''
Explicação sobre POO

    POO significa Programação Orientada a Objetos, ela é separada em quatro pilares: 
Abstração, Encapsulamento, Herança e Polimorfismo.

    abstração: é a capacidade de representar entidades do mundo real em classes e 
objetos, focando apenas nos aspectos relevantes e ignorando detalhes desnecessários.

    encapsulamento: é o princípio de ocultar os detalhes internos de uma classe, 
permitindo o acesso aos dados apenas por meio de métodos públicos, 
garantindo a integridade e segurança dos dados.

    herança: é o mecanismo que permite criar novas classes a partir de 
classes existentes, permitindo a reutilização de código e a criação de 
hierarquias de classes.

    polimorfismo: é a capacidade de um objeto se comportar de diferentes maneiras 
dependendo do contexto, permitindo que métodos com o mesmo nome possam ter 
implementações diferentes em classes distintas.'''
''' 
exemplo de abstração:

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self):
        print(f"{self.nome} Atacou!!")

personagem1 = Personagem("Inácio", 100, 20)
personagem1.atacar()
print(f"Nome: {personagem1.nome}")
print(f"Vida: {personagem1.vida}")
print(f"Ataque: {personagem1.ataque}")
class carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"o carro {self.marca} {self.modelo} está acelerando!!")

    def frear(self):
        print(f"o carro {self.marca} {self.modelo} está freando!!")

carro1 = carro("Chevrolet", "Onix")
carro1.acelerar()
carro1.frear()

carro2 = carro("Fiat", "Uno")
carro2.acelerar()
carro2.frear()'''
''' 
exemplo de encapsulamento:
class personagem:
    def __init__(self, nome, vida, ataque):
        # Atributos privados são definidos com dois underscores (__) antes do 
        # nome do atributo. eles podem ser usados para armazenar informações que 
        # não devem ser acessadas diretamente de fora da classe.
        self.__nome = nome
        self.__vida = vida
        self.__ataque = ataque

    def atacar(self):
        print(f"{self.__nome} Atacou!!")

    # aqui criamos funções para acessar os atributos privados,
    # essas funções são chamadas de métodos getters.
    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_ataque(self):
        return self.__ataque

    def set_nome(self, nome):
        self.__nome = nome
    def set_vida(self, vida):
        if vida >= 0:
            self.__vida = vida
    def set_ataque(self, ataque):
        if ataque >= 0:
            self.__ataque = ataque
personagem1 = personagem("Inácio", 100, 20)
personagem1.atacar()

# Tentativa de alterar o atributo privado diretamente, 
# isso não terá efeito, pois o atributo é privado.
personagem1.__vida = 50  
# apenas com o uso do método setter podemos alterar o valor do atributo privado.
personagem1.set_vida(50)

# Acessando os atributos privados diretamente de fora da classe não é permitido.
# print(f"Nome: {personagem1.__nome}")  # Isso resultará em um erro de atributo
# print(f"Vida: {personagem1.__vida}")  # Isso resultará em um erro de atributo
# print(f"Ataque: {personagem1.__ataque}")  # Isso resultará em um erro de atributo

# apenas criando uma função dentro da classe para acessar os atributos privados, 
# podemos obter seus valores de forma segura.
print(f"Nome: {personagem1.get_nome()}")
print(f"Vida: {personagem1.get_vida()}")
print(f"Ataque: {personagem1.get_ataque()}")'''
'''
exemplo de herança:
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

# colocando a classe Cachorro como subclasse da classe Animal,
# a classe Cachorro herda os atributos e métodos da classe Animal.
class Cachorro(Animal):
    pass

cachorro1 = Cachorro("Rex")
cachorro1.comer()  # Acessando o método da classe pai (Animal)'''
'''
exemplo de polimorfismo:
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} late.")

class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} mia.")

cachorro1 = Cachorro("Rex")
gato1 = Gato("Mingau")

cachorro1.fazer_som()  # Acessando o método da classe filha (Cachorro)
gato1.fazer_som()      # Acessando o método da classe filha (Gato)'''