# 01. Quantas linhas e colunas tem o dataset?

from common import load_titanic_csv

df = load_titanic_csv()

num_linhas, num_colunas = df.shape

print(f"Número de linhas: {num_linhas}")
print(f"Número de colunas: {num_colunas}")