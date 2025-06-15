# 05. Qual a média de idade dos não-sobreviventes?

from common import load_titanic_csv

df = load_titanic_csv()

nao_sobreviveram = df[df['Survived'] == 0]
media_idade_nao_sobreviveram = nao_sobreviveram['Age'].mean()

print(f"A média da idade das pessoas que não sobreviveram é de {media_idade_nao_sobreviveram:.2f} anos.")