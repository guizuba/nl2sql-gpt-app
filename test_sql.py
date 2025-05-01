import sys
import os

# Adiciona manualmente o caminho até a pasta onde está o 'apps'
current_dir = os.path.dirname(os.path.abspath(__file__))
apps_path = os.path.join(current_dir, "apps")
sys.path.append(apps_path)

from nl2sql_app.sql_generator import generate_sql_from_question

pergunta = "Qual foi o total de vendas em março de 2024?"
print(generate_sql_from_question(pergunta))