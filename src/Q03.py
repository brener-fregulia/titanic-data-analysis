# 03. Qual a idade média dos passageiros?

from common import load_titanic_csv

df = load_titanic_csv()

media_idade = df['Age'].mean()

print(f"A média da idade das pessoas é de {media_idade:.2f} anos.")