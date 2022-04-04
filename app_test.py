import utilities
import pandas as pd

target = 30000
aporte_inicial = 20000
aporte_mensal = 200
meses = 18
num_invest = 4 #numero de investimentos
perfil = 1 # 1:conversador, 2:moderado, 3:agressivo

df_invest = pd.read_csv("investimentos_bd.csv")

winner = utilities.best_investments(aporte_inicial, aporte_mensal, meses, target, perfil, df_invest, max = num_invest)
print(winner)

# Exporta os resultados obtidos para um json com a finalidade de enviar para o front-end
winner.to_json(r'recomenda.json')

