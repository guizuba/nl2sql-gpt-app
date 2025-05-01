from openai import OpenAI
import os

# Defina sua chave de acesso:
client = OpenAI(api_key="SUA CHAVE_API_AQUI")

def load_schema_context():
    with open("context/schema_description.txt", "r", encoding="utf-8") as f:
        return f.read()

def generate_sql_from_question(question):
    schema_context = load_schema_context()

    prompt = f"""
Você é um assistente que converte perguntas em linguagem natural para SQL.
Considere o seguinte esquema de banco de dados:

{schema_context}

Converta a seguinte pergunta em uma consulta SQL:
Pergunta: "{question}"
SQL:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ou "gpt-4"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )

    return response.choices[0].message.content.strip()
