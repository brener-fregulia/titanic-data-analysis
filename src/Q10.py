# 10. Quantas crianças (idade < 12) sobreviveram?

from common import load_titanic_csv

df = load_titanic_csv()

criancas_sobreviveram = df[(df['Survived'] == 1) & (df['Age'] < 12)].shape[0]

print(f"{criancas_sobreviveram} crianças (idade < 12) sobreviveram.")