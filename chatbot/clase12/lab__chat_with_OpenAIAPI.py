import openai

from config import API_KEY

# Configura tu clave de API de OpenAI
openai.api_key = API_KEY 


def generar_respuesta(pregunta):
    respuesta = openai.completions.create(
        model="text-davinci-003", # gpt-3.5-turbo-instruct
        prompt=pregunta,
        max_tokens=50
    )
    return respuesta.choices[0].text.strip()

def main():
    print("Bienvenido al Chatbot de OpenAI")

    while True:
        pregunta = input("Escribe tu pregunta (o 'salir' para finalizar): ")

        if pregunta.lower() == 'salir':
            print("¡Hasta luego!")
            break

        respuesta = generar_respuesta(pregunta)
        print("Respuesta:", respuesta)

if __name__ == "__main__":
    main()