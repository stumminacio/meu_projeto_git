'''
def nome_completo(nome, sobrenome1, sobrenome2):
    return f"{nome} {sobrenome1} {sobrenome2}"

print(nome_completo("Inácio", "Oliveira", "Stumm"))'''
'''
# a biblioteca unittest é utilizada para criar testes unitários em Python, 
# os testes unitários são uma forma de verificar se uma determinada função 
# ou método está funcionando corretamente, garantindo que o código esteja 
# livre de erros e funcionando conforme o esperado.
import unittest

def nome_completo(nome, sobrenome1, sobrenome2):
    return f"{nome} {sobrenome1} {sobrenome2}"

# testcase é uma classe que herda de unittest.TestCase,
# e é utilizada para agrupar um conjunto de testes relacionados a uma 
# determinada funcionalidade ou módulo.
class teste_nome_completo(unittest.TestCase):
    def test_nome_completo(self):
        resultado = nome_completo("Inácio", "Oliveira", "Stumm")
        # o método assertEqual é utilizado para verificar se o resultado
        # obtido a partir da função nome_completo é igual ao valor esperado.
        # se os valores forem iguais, o teste passa; caso contrário, o teste falha.
        self.assertEqual(resultado, "Inácio Oliveira Stumm")

# o bloco if __name__ == '__main__': é utilizado para verificar se o
# script está sendo executado diretamente (como um programa principal) ou se
# está sendo importado como um módulo em outro script. Se o script estiver
# sendo executado diretamente, o código dentro desse bloco será executado.
if __name__ == '__main__':
    unittest.main()'''
'''
import unittest

def nome_completo(nome, sobrenome1, sobrenome2):
    return f"{nome} {sobrenome1} {sobrenome2}"

class TesteNomeCompleto(unittest.TestCase):
    def test_nome_completo_1(self):
        resultado = nome_completo("Inácio", "Oliveira", "Stumm")
        self.assertEqual(resultado, "Inácio Oliveira Stumm")
    def test_nome_completo_2(self):
        resultado = nome_completo("Maria", "Silva", "Souza")
        self.assertEqual(resultado, "Maria Silva Souza")

unittest.main(argv=[''], exit=False)
'''
'''
class aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

aluno1 = aluno("Inácio", 13)
print(aluno1.apresentar())
'''
'''
# A biblioteca unittest é uma ferramenta poderosa para criar testes unitários em Python, 
# permitindo verificar se funções e métodos estão funcionando corretamente. 
# A seguir, apresento uma lista de alguns dos principais métodos de asserção 
# disponíveis na biblioteca unittest:

# PRINCIPAIS:

# assertEqual(a, b) verifica se os valores são iguais;
# assertNotEqual(a, b) verifica se os valores são diferentes;
# assertTrue(a) verifica se o valor é verdadeiro;
# assertFalse(a) verifica se o valor é falso;
# assertIsNone(a) verifica se o valor é None;
# assertIsNotNone(a) verifica se o valor não é None;
# assertIn(a, b) verifica se o valor está presente em uma lista ou coleção;
# assertNotIn(a, b) verifica se o valor não está presente em uma lista ou coleção;

# OUTRAS:

# assertRaises(exception, func, *args, **kwargs) verifica se uma exceção é levantada ao chamar uma função com determinados argumentos.
# assertRaisesRegex(exception, regex, func, *args, **kwargs) verifica se uma exceção é levantada ao chamar uma função com determinados argumentos e se a mensagem da exceção corresponde a uma expressão regular específica;
# assertAlmostEqual(a, b, places=7) verifica se os valores são aproximadamente iguais até um determinado número de casas decimais;
# assertNotAlmostEqual(a, b, places=7) verifica se os valores não são aproximadamente iguais até um determinado número de casas decimais;
# assertGreater(a, b) verifica se o valor a é maior que o valor b;
# assertGreaterEqual(a, b) verifica se o valor a é maior ou igual ao valor b;
# assertLess(a, b) verifica se o valor a é menor que o valor b;
# assertLessEqual(a, b) verifica se o valor a é menor ou igual ao valor b;
# assertCountEqual(a, b) verifica se duas listas ou coleções possuem os mesmos elementos, independentemente da ordem;
# assertMultiLineEqual(a, b) verifica se duas strings multilinha são iguais;
# assertSequenceEqual(a, b) verifica se duas sequências (listas, tuplas, etc.) são iguais;
# assertListEqual(a, b) verifica se duas listas são iguais;
# assertTupleEqual(a, b) verifica se duas tuplas são iguais;
# assertSetEqual(a, b) verifica se dois conjuntos (sets) são iguais;
# assertDictEqual(a, b) verifica se dois dicionários são iguais;
# assertDictContainsSubset(a, b) verifica se um dicionário contém um subconjunto de outro dicionário;
# assertLogs(logger, level) verifica se um determinado logger registra mensagens em um determinado nível de log;
# assertWarns(warning, func, *args, **kwargs) verifica se um determinado aviso é emitido ao chamar uma função com determinados argumentos;
# assertWarnsRegex(warning, regex, func, *args, **kwargs) verifica se um determinado aviso é emitido ao chamar uma função com determinados argumentos e se a mensagem do aviso corresponde a uma expressão regular específica;
'''
import random

class Batalha:
    def __init__(self, vida_jogador, vida_inimigo):
        self.vida_jogador = vida_jogador
        self.vida_inimigo = vida_inimigo

    def atacar(self):
        dano = random.randint(10, 30)
        self.vida_inimigo -= dano
        print(f"\nVocê atacou o inimigo e causou {dano} de dano!")
        print(f"Vida do inimigo: {self.vida_inimigo} \n")
        dano_inimigo = random.randint(1, 10)
        self.vida_jogador -= dano_inimigo 
        print(f"O inimigo atacou e causou {dano_inimigo} de dano em você!")
        print(f"Sua vida: {self.vida_jogador} \n")

    def defender(self):
        print("\nVocê se defendeu e reduziu o dano do ataque do inimigo!")
        dano_inimigo = random.randint(5, 15)
        self.vida_jogador -= dano_inimigo // 2
        print(f"O inimigo atacou e causou {dano_inimigo // 2} de dano em você!")
        print(f"Sua vida: {self.vida_jogador} \n")

    def fugir(self):
        print("Você fugiu da batalha! O inimigo não conseguiu te alcançar.")

    def continuar_batalha(self):
        while self.vida_jogador > 0 and self.vida_inimigo > 0:
            opcao = input("Escolha sua ação (atacar, defender, fugir): ").lower()
            if opcao == "atacar":
                self.atacar()
            elif opcao == "defender":
                self.defender()
            elif opcao == "fugir":
                self.fugir()
                break
            else:
                print("Opção inválida! Tente novamente.")

            if self.vida_inimigo <= 0:
                print("Parabéns! Você derrotou o inimigo!")
                break
            elif self.vida_jogador <= 0:
                print("Você foi derrotado pelo inimigo! Game Over.")
                break

print("\nDerrotando monstros em um jogo de RPG! \n")

vida_jogador = 100
vida_inimigo = 80
batalha = Batalha(vida_jogador, vida_inimigo)

print("Você encontrou um inimigo! Prepare-se para a batalha. \n")
print(f"Sua vida: {vida_jogador}")
print(f"Vida do inimigo: {vida_inimigo} \n")



# o metodo lower() é utilizado para converter a entrada do usuário 
# para letras minúsculas, facilitando a comparação com as opções válidas.
opcao = input("Escolha sua ação (atacar, defender, fugir): ").lower()

if opcao == "atacar":
    batalha.atacar()
elif opcao == "defender":
    batalha.defender()
elif opcao == "fugir":
    batalha.fugir()
batalha.continuar_batalha()
