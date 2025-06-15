# 08. Faça um gráfico de dispersão (scatter) entre idade e tarifa

from common import load_titanic_csv
import matplotlib.pyplot as plt

df = load_titanic_csv()

idades = df['Age']
tarifas = df['Fare']

plt.scatter(idades, tarifas)
plt.xlabel('Idade')
plt.ylabel('Tarifa')
plt.title('Idade vs Tarifa')
plt.show()