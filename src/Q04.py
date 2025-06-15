# 04. Qual a média de idade apenas dos sobreviventes?

from common import load_titanic_csv

df = load_titanic_csv()

sobreviveram = df[df['Survived'] != 0]
media_idade_sobreviveram = sobreviveram['Age'].mean()

print(f"A média da idade das pessoas que sobreviveram é de {media_idade_sobreviveram:.2f} anos.")