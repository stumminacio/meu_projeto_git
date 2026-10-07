'''
# idades

idades = []
dado1 = int(input("qual a idade do individuo? "))
idades.append(dado1)
qnt_ind = 1

while idades[-1] > 0:
    novo_dado = int(input("qual a idade do individuo? "))
    idades.append(novo_dado)
    qnt_ind += 1

media_idades = sum(idades[:-1]) / (qnt_ind - 1)
print(f"A média das idades é: {media_idades:.2f}")'''
'''
#numero perfeito
Na matemática, um número perfeito é um número inteiro para o qual a soma
de todos  os seus divisores positivos próprios (excluindo ele mesmo) é igual 
ao próprio número. Por exemplo, o número 6 é perfeito, pois 1+2+3 é igual a 6. 
Sua tarefa é escrever um programa que imprima se um determinado número é perfeito 
ou não. 

Entrada 

A entrada contém vários casos de teste. A primeira linha da entrada contém um 
inteiro N (1  ≤ N ≤ 20), indicando o número de casos de teste da entrada. 
Cada uma das N linhas seguintes  contém um valor inteiro X (1 ≤ X ≤ 108), 
que pode ser ou não, um número perfeito. 

Saída 

Para cada caso de teste de entrada, imprima a mensagem “X é perfeito” ou “X não 
é  perfeito”, de acordo com a especificação fornecida.

testes = int(input("Digite o número de casos de teste: "))
for _ in range(testes):
    numero = int(input("Digite um número: "))
    soma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    
    if soma_divisores == numero:
        print(f"{numero} é perfeito")
    else:
        print(f"{numero} não é perfeito")'''