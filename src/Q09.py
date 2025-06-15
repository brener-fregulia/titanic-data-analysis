# 09. Qual o número de homens e mulheres?

from common import load_titanic_csv

df = load_titanic_csv()

homens = df[df['Sex'] == 'male'].shape[0]
mulheres = df[df['Sex'] == 'female'].shape[0]

# Forma mais rápida e menos verbosa:
# print(df['Sex'].value_counts())

print(f"Existem {homens} homens.")
print(f"Existem {mulheres} mulheres.")