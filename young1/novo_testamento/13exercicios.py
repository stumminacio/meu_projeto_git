'''
# primeiro exercicio usando polimorfismo:

# mostrando a classificação de animais com base em suas características para a 
# entrada de dados do usuário.
p1 = input(f"digite a primeira caracteristica do animal: \n caracteristicas possiveis: vertebrado ou invertebrado \n")
if p1 == "vertebrado":
    p2 = input(f"digite a segunda caracteristica do animal: \n caracteristicas possiveis: ave ou mamifero \n")
    if p2 == "ave":
        p3 = input(f"digite a terceira caracteristica do animal: \n caracteristicas possiveis: carnivoro ou onivoro \n")
    elif p2 == "mamifero":
        p3 = input(f"digite a terceira caracteristica do animal: \n caracteristicas possiveis: onivoro ou herbivoro \n")
else:
    p2 = input(f"digite a segunda caracteristica do animal: \n caracteristicas possiveis: inseto ou anelideo \n")
    if p2 == "inseto":
        p3 = input(f"digite a terceira caracteristica do animal: \n caracteristicas possiveis: hematofago ou herbivoro \n")
    elif p2 == "anelideo":
        p3 = input(f"digite a terceira caracteristica do animal: \n caracteristicas possiveis: hematofago ou onivoro \n")

# definindo a classe base Animal e suas subclasses Vertebrado e Invertebrado
class Animal:
    # método abstrato para classificar o animal com base nas características fornecidas
    def classificar(self, classe: str, alimento: str) -> str:
        # o metodo raise NotImplementedError é usado para indicar que as subclasses devem implementar este método
        raise NotImplementedError("As subclasses devem implementar este método.")

class Vertebrado(Animal):
    def classificar(self, classe: str, alimento: str) -> str:
        if classe == "ave":
            if alimento == "carnivoro":
                return "aguia"
            elif alimento == "onivoro":
                return "pomba"
        elif classe == "mamifero":
            if alimento == "onivoro":
                return "homem"
            elif alimento == "herbivoro":
                return "vaca"
class Invertebrado(Animal):
    def classificar(self, classe: str, alimento: str) -> str:
        if classe == "inseto":
            if alimento == "hematofago":
                return "pulga"
            elif alimento == "herbivoro":
                return "lagarta"
        elif classe == "anelideo":
            if alimento == "hematofago":
                return "sanguessuga"
            elif alimento == "onivoro":
                return "minhoca"

classes = {
    "vertebrado": Vertebrado(),
    "invertebrado": Invertebrado()
}

if p1 in classes:
    animal = classes[p1]
    resultado = animal.classificar(p2, p3)
    print(f"O animal é: {resultado}")'''
'''
# segundo exercicio, sem polimorfismo:

notas_validas = []

while len(notas_validas) < 2:
    nota = float(input("digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        notas_validas.append(nota)
    else:
        print("nota invalida, digite novamente.")

media = sum(notas_validas) / 2

print(f"media = {media:.2f}")
'''