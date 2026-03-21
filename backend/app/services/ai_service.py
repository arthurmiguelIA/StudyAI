from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI

client = OpenAI()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def generate_summary(text: str):
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Resuma:\n{text}"}
        ]
    )
    return response.choices[0].message.content


def generate_flashcards(text: str):
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Crie flashcards para estudo."},
            {"role": "user", "content": f"Crie flashcards no formato Pergunta | Resposta:\n{text}"}
        ]
    )
    return response.choices[0].message.content


def generate_quiz(text: str):
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Crie perguntas de múltipla escolha."},
            {"role": "user", "content": f"Crie 5 perguntas com 4 alternativas e indique a correta:\n{text}"}
        ]
    )
    return response.choices[0].message.content