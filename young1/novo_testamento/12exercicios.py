'''
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, 
com um dígito após o ponto decimal.

Saída

Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

distancia = int(input("Digite a distância percorrida (em Km): "))
combustivel = float(input("Digite o total de combustível gasto (em litros): "))
def consumo_medio(distancia, combustivel):
    consumo = distancia / combustivel
    return f"{consumo:.3f} km/l"

print(f"distancia: {distancia} km, combustível: {combustivel} l")
print(f"Consumo médio: {consumo_medio(distancia, combustivel)}")

# nota: na funcao consumo_medio, no return, dentro do f-string, o valor de consumo é formatado para ter 3 casas decimais usando :.3f. 
# Isso garante que o resultado seja apresentado com a precisão desejada.
'''

'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada

O arquivo de entrada contém um valor inteiro N.

Saída

Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.


def converter_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas}:{minutos}:{segundos_restantes}"

tempo_em_segundos = int(input("Digite o tempo em segundos: "))
print(f"tempo convertido: {converter_tempo(tempo_em_segundos)}")

# nota: a função converter_tempo realiza a conversão de segundos para o formato horas:minutos:segundos.
# os metodos de divisão inteira (// = divisão inteira, sem resto) e módulo (% = resto da divisão) são usados para calcular as horas, minutos e segundos restantes.
# o resultado é formatado em uma string no formato desejado e retornado.
'''