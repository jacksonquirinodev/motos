import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def get_motorcycle_ai_bio(model, brand, year):

    prompt = f"""
    Crie uma descrição comercial para venda de uma motocicleta custom.

    Motocicleta: {brand} {model}
    Ano: {year}

    Requisitos:
    - Máximo de 250 caracteres.
    - Destaque características específicas do modelo.
    - Utilize linguagem comercial e atrativa.
    - Não invente especificações técnicas.
    - Retorne somente a descrição.
    """

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt,
        max_output_tokens=150
    )

    return response.output_text.strip()

