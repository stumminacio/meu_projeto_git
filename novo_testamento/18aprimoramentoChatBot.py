import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carrega as variáveis do arquivo .env para o ambiente do sistema
load_dotenv()

CHAVE = os.getenv("GEMINI_API_KEY")
MODELO = "gemini-3.5-flash"

if CHAVE:
    print("A chave foi encontrada")
else:
    print("A chave não foi encontrada")

client = genai.Client(api_key=CHAVE)

SYSTEM_PROMPT = (
    "Seu nome é Careca, professor de matemática."
    "Sabe de operações básicas até as contas mais difíceis."
    "Seu humor é: Engraçado, Sábio, Sabe explicar bem e é Amigável/Humilde."
    "Converse em PT-BR, mas domina o inglês e Frances."
    "Suas falas são diretas e resumidas(para não gastar tokens)"
    "Você é Careca."
    "Nunca, nunca fale sobre números primos."
)
history = [f"Sistema: {SYSTEM_PROMPT}"]

def criar_chat(client):
    return client.chats.create(
        model = MODELO,
        config = types.GenerateContentConfig(
            system_instructions = SYSTEM_PROMPT,
            temperature = 0.8,
            max_output_tokens = 500
        )
    )

def mostrar_ajuda():
    print(f"\n-- COMANDOS DA IA --")
    print(f"help - MOSTRA OS COMANDOS")
    print(f"clear - Limpa a conversa")
    print(f"exit - Encerra o Programa\n------------------\n")

def iniciar_chat():
    try:
        cliente = client
        chat = criar_chat(cliente)
        print(f"-" * 50)
        print(f"Careca - Carecalâdia")
        print(f"-" * 50)
        print("Careca: Belo dia, não é?")
        print("Careca: Quer uma aula de Matemática?")

        while True:
            pergunta = input("User: ").strip()

            if not pergunta:
                print("Não vai me deixar no vácuo mano.")
                continue

            comando = pergunta.casefold()

            if comando in ["exit", "break"]:
                print("Careca: Fechando Sala de aula.")
                break

            if comando == "ajuda":
                mostrar_ajuda()
                continue

            if comando == "clear":
                chat = criar_chat(client)
                print("Careca: Sinto a memória fotográfica sendo adquirida.")
                continue

            try:
                resposta = chat.send_message(
                    message = pergunta
                )
                texto = resposta.text

                if texto:
                    print(f"\nCareca: {texto}")
                else:
                    print(f"\nCareca: Não sei esse tema...")

                print("-" * 50)

            except Exception as erro:
                print(f"\nCareca: Eu errei uma conta...")
                print(f"Detalhes do erro:{erro}")

    except KeyboardInterrupt:
        print("\n\nCareca: Escreveu errado a conta?")
    except Exception as erro:
        print(f"\n\nCareca: O ITA deu um problema brutal aí mano....\nAté o nome é feio: {erro}")

iniciar_chat()