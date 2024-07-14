import openai
from openai import OpenAI
from dotenv import load_dotenv
import os
# Load the environment variables from .env file
load_dotenv()
# Accessing variables

def correct_text(text):
    """Sends the text to ChatGPT for correction."""
    
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4o",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": 
            """Você é um assistente que corrige textos de OCR e, você corrige os erros
               de um prontuário de um consultório odontológico no Brasil, em português do Brasil, reescreva o texto de maneira a corrigir os erros nas palavras geradas pelo OCR.
               Você transforma o texto corrigido em um formulário estruturado em JSON.
               Transforme as perguntas e respostas dos formulários de 'sim' e 'não' para 'true' e 'false'"""},
        {"role": "user", "content": text}
    ]
    )

    return response.choices[0].message.content

# FOR TESTING
# print(correct_text("Amigos: Eduardo e Jonas. Faz frio? Não"))