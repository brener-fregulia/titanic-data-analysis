# 02. Quantas pessoas sobreviveram? E quantas não sobreviveram?

from common import load_titanic_csv

df = load_titanic_csv()

sobreviveram = df[df['Survived'] != 0].shape[0]
nao_sobreviveram = df[df['Survived'] == 0].shape[0]
print(f"{sobreviveram} pessoas sobreviveram.")
print(f"{nao_sobreviveram} pessoas não sobreviveram.")