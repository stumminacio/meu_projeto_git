'''
# não se pode dividir por 0

numero1 = 10
numero2 = 0

resultado = numero1 / numero2

print(resultado)'''
'''
try:
    # codigo que pode causar erro ou exceção.
except:
    # o que fazer caso aconteça de fato a exceção ou erro.
'''
'''
try:
    numero = 19
    divisor = 0

    resultado = numero / divisor
    print(resultado)
except:
    print("não foi possivel realizar a divisão, pois o divisor é 0.")
'''
'''
idade = int(input("digite sua idade: "))

print(f"sua idade é {idade}")'''
'''
try:
    idade = int(input("qual é sua idade? "))
    print(f"sua idade é {idade}")
except:
    print("esse campo aceita apenas numeros...")

try:
    idade = int(input("qual é sua idade? "))
    print(f"sua idade é {idade}")
except ValueError:
    print("esse campo aceita apenas numeros...")'''
'''
try:
    numero = int(input("digite um numero: "))

    resultado = 100 / numero

    print(resultado)
except ValueError:
    print("você precisa digitar um valor numérico...")
except ZeroDivisionError:
    print("não pode dividir por zero...")'''
'''
try:
    numero = int(input("digite um numero: "))

    resultado = 100 / numero
except ValueError as erro:
    print(f"ocorreu um erro!\n{erro}")
except ZeroDivisionError:
    print("não pode dividir por zero...")'''
'''
try:
    numero = int(input("digite seu numero: "))
    print("parabens, seu numero doi digitado corretamente!")
except ValueError:
    print("entrada invalida")
else:
    print("todos os numeros foram digitados corretamente!")'''
'''
try:
    numero = int(input("digite seu numero: "))
except ValueError:
    print("entrada invalida!")
finally:
    print("fim da operacao.")'''
'''
EXERCICIOS

while True:
    try:
        idade = int(input("digite sua idade: "))
        break
    except ValueError:
        print("digite apenas numeros")
    
print(f"sua idade é {idade}")'''

# calculadora:

def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

operacoes = {
    "1" : ("Adição", somar),
    "2" : ("Subtração", subtrair),
    "3" : ("Multiplicação", multiplicar),
    "4" : ("Divisão", dividir)

}

while True:
    print("\nCALCULADORA EM PYTHON")
    # criando o menu
    for codigo, (nome, _) in operacoes.items():
        print(f"{codigo} - {nome}")
    print("0 - Sair")
    # opcao do usuario
    escolha = input("Escolha uma opção: ").strip()
    
    if escolha == "0":
        print("Calculadora encerrada.")
        break

    if escolha not in operacoes:
        print("Opção inválida.")
        continue

    try:
            numero_1 = float(input("Digite o primeiro número: "))
            numero_2 = float(input("Digite o segundo número: "))
            nome, funcao = operacoes[escolha]
            resultado = funcao(numero_1, numero_2)
            print(f"Resultado da {nome}: {resultado:g}")
    except ValueError as erro:
            print(f"Erro: {erro}")