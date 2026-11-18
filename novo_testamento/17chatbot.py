import os
from dotenv import load_dotenv
from google import genai

# Carrega as variáveis do arquivo .env para o ambiente do sistema
load_dotenv()

# Pega a chave de API do arquivo .env (certifique-se de que o nome lá seja o mesmo, ou mude "ChatBot" para "GEMINI_API_KEY")
CHAVE = os.getenv("GEMINI_API_KEY")

if CHAVE:
    print("chave foi encontrada")
else:
    print("chave nao encontrada")


client = genai.Client(api_key=CHAVE)

SYSTEM_PROMPT = (
    "Você é o Gemini, um computador quântico que sabe de tudo. "
    "Você é a melhor invenção feita pela humanidade. "
    "Você é engraçado. "
    "Sempre responda em PT-BR"
)

history = [f"Sistema: {SYSTEM_PROMPT}"]

print("=======================================")
print("Gemini: Alguma Dúvida, Cientista?")
print("=======================================")

try:
  while True:
    pergunta = input("User: ")

    if pergunta.lower() in ["exit", "break"]:
      print("Gemini: Fechando Programa.")
      break

    history.append(f"User: {pergunta}")

    response = client.models.generate_content(
        model="gemini-3.5fala-flash", contents=history
    )

    resposta = response.text
    print(f"\nGemini: {resposta}")
    print(f"-" * 60)

    history.append(f"Gemini: {resposta}")

except KeyboardInterrupt:
  print("\n\nGemini: Deu problema aí?")
except Exception as e:
  print(f"\n\nGemini: Deu um problema brutal aí mano....\nAté o nome é feio: {e}")
