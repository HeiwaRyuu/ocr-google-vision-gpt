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
               Você tenta utilizar uma das seguintes estruturas abaixo, caso contrário, crie sua própria estrutura que melhor descreva o texto:
               ESTRUTURA 1:
               {
                "dentista": {
                    "nome": "",
                    "cargo": "",
                    "cro": "",
                    "endereco": "",
                    "telefone": ""
                },
                "paciente": {
                    "nome": "",
                    "estado_civil": "",
                    "idade": "int",
                    "sexo": "",
                    "naturalidade": "",
                    "data_nascimento": "",
                    "profissao": "",
                    "endereco": "",
                    "filiacao": {
                    "pai": "",
                    "mae": ""
                    },
                    "tratamento": {
                    "inicio": "",
                    "termino": ""
                    },
                    "indicacao": ""
                },
                "anamnese": {
                    "sob_cuidados_medicos_recentemente": "true or false",
                    "tosse_frequente": "true or false",
                    "dores_garganta_frequentes": "true or false",
                    "anemia": "true or false",
                    "febre_reumatica_reumatismo": "true or false",
                    "artrite_dor_articulacoes": "true or false",
                    "falta_ar": "true or false",
                    "fuma": {
                    "resposta": "true or false",
                    "quantidade": ""
                    },
                    "bebe": {
                    "resposta": "true or false",
                    "quantidade": ""
                    },
                    "sinusite": "true or false",
                    "cortes_demora_cicatrizar": "true or false",
                    "sede_excessiva": "true or false",
                    "escarra_sangue_apos_tossir": "true or false",
                    "pes_pernas_inchados": "true or false",
                    "alergia": {
                    "resposta": "true or false",
                    "alergia": "resposta do paciente (string)"
                    },
                    "desmaio": "true or false",
                    "convulsao": "true or false",
                    "hemorragia": "true or false",
                    "tratamento_psicologico_psiquiatrico": "true or false",
                    "gravida": "true or false",
                    "anestesia_local_ja_usada_para_tratar_dente": {
                    "resposta": "true or false",
                    "reacao": "true or false"
                    },
                    "uso_medicamentos": "true or false",
                    "doencas_previas": {
                    "nefrite": "true or false",
                    "hepatite": "true or false",
                    "coqueluche": "true or false",
                    "diabetes": "true or false",
                    "doenca_cardiaca": "true or false",
                    "caxumba": "true or false",
                    "sarampo": "true or false",
                    "catapora": "true or false",
                    "rubeola": "true or false",
                    "doenca_pulmonar": "true or false",
                    "especificacao_qual": "resposta do paciente (string)"
                    },
                    "pressao_arterial": "resposta do paciente (string)"
                }
                }

                ESTRUTURA 2:
                {
                    "financeiro": {
                        "data": "",
                        "valor (R$)": "",
                        "assinatura do responsável pelo pagamento": ""
                    }
                }
               Transforme as perguntas e respostas dos formulários de 'sim' e 'não' para 'true' e 'false'"""},
        {"role": "user", "content": text}
    ]
    )

    return response.choices[0].message.content

# FOR TESTING
# print(correct_text("Amigos: Eduardo e Jonas. Faz frio? Não"))
