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
    model="gpt-3.5-turbo",
    # response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": 
            """Você é um assistente que corrige textos de OCR. Você corrige todas as palavras erradas que o OCR possivelmente gerou."""},
        {"role": "user", "content": text}
    ]
    )

    return response.choices[0].message.content