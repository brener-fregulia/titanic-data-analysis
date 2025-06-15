# 07. Existe correlação entre a idade e a tarifa? (use .corr())

from common import load_titanic_csv

df = load_titanic_csv()

correlacao_idade_tarifa = df['Age'].corr(df['Fare'])

print(correlacao_idade_tarifa)