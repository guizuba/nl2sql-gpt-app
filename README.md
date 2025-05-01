# NL2SQL GPT App

Este projeto transforma perguntas em **linguagem natural** (NL = Natural Language) em **consultas SQL automaticamente**, usando **GPT (OpenAI)**, com suporte para execução local em arquivos `.csv` e visualização dos resultados em terminal ou interface Streamlit.

---

## Funcionalidades

- Recebe uma pergunta como: _"Qual foi o total de vendas em março de 2024?"_
- Envia a pergunta ao GPT para gerar a SQL com base no schema
- Executa a SQL localmente nos dados simulados (`.csv`)
- Mostra o resultado como tabela ou gráfico (em breve via Streamlit)

  ## Estrutura do Projeto

  nl2sql-gpt-app/
│
├── data/                    # Dados simulados (.csv)
│   ├── customers.csv
│   └── sales.csv
│
├── models/                  # Modelos SQL simulados
│   ├── customers.sql
│   └── sales.sql
│
├── context/                 # Descrição do schema para orientar o GPT
│   └── schema_description.txt
│
├── apps/
│   └── nl2sql_app/
│       ├── main.py          # Interface Streamlit (em construção)
│       └── sql_generator.py # Função que gera SQL com GPT
│
├── test_sql.py              # Teste rápido via terminal
├── .gitignore
└── README.md

## Requisitos

- Python 3.9+
- Conta com API key da [OpenAI](https://platform.openai.com/)
- Pacotes: `openai`, `pandas`, `duckdb`, `streamlit` (opcional)

Instale com:

```bash
pip install -r requirements.txt

## 📊 Próximos passos

- ✅ **Suporte a `pandas + duckdb` para execução local**
- 🟡 **Visualização em gráficos com Streamlit**
- 🟡 **Suporte a múltiplos arquivos `.csv`**
- 🟢 **Integração com banco SQL real** (ex: SQLite, Postgres)
