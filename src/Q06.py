# 06. Qual a tarifa média paga por classe de passagem (Pclass)?

from common import load_titanic_csv

df = load_titanic_csv()

media_ticket_por_classe = df.groupby('Pclass')['Fare'].mean()

print("Média de tarifa por classe:")
for classe, media in media_ticket_por_classe.items():
    print(f"Classe {classe}: ${media:.2f}")
