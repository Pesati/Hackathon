import numpy as np
import pandas as pd
import random
from itertools import combinations

# Alguns indices economicos utilizados nos investimentos
cdi_hoje_ano = 11.61
cdi_hoje_mes = 0.92

ipca_hoje_ano = 10.54
ipca_hoje_mes = 0.83

selic_hoje_ano = 11.75

ibov_ano = 21.19

# Funcao para retornar os valores de cada investimento
# Obs.: nao foi utilizado nenhuma taxa de imposto para fins de simplificacao
def valor_final_invest(investmentType, aporte_inicial, aporte_mensal, meses, taxa, benchmark,
                       cdi_hoje_mes=cdi_hoje_mes, ipca_hoje_mes=ipca_hoje_mes,
                       cdi_hoje_ano=cdi_hoje_ano, ipca_hoje_ano=ipca_hoje_ano,
                       selic_hoje_ano=selic_hoje_ano, ibov_hoje_ano=ibov_ano):
    valor_final = 0

    # CDB e LCI e LCA
    if investmentType == 1 or investmentType == 3 or investmentType == 4:
        if benchmark == 'CDI':
            juros = 1 + (cdi_hoje_mes * taxa / 100 / 100)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

        # Relacionado a IPCA
        if benchmark == 'IPCA':
            juros = (1 + (ipca_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

    # Titulo do Tesouro
    if investmentType == 5:

        # Relacionado a IPCA
        if benchmark == 'IPCA':
            juros = (1 + (ipca_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

        # Relacionado a SELIC
        if benchmark == 'SELIC':
            juros = (1 + (selic_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

        # Relacionado a PRE-FIXADO
        if benchmark == 'PRE':
            juros = (1 + (taxa / 100)) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

    # Debenture
    if investmentType == 6:

        # Relacionado a IPCA
        if benchmark == 'IPCA':
            juros = (1 + (ipca_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

        # Relacionado a CDI
        if benchmark == 'CDI':
            juros = (1 + (cdi_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

    # Fundo de Renda Fixa
    if investmentType == 10:

        # Relacionado a IPCA
        if benchmark == 'IPCA':
            juros = (1 + (ipca_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

        # Relacionado a CDI
        if benchmark == 'CDI':
            juros = (1 + (cdi_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

    # Fundo Multimercado
    if investmentType == 11:

        # Relacionado a IPCA
        if benchmark == 'IPCA':
            juros = (1 + (ipca_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento
                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

    # Fundo de Renda Variavel
    if investmentType == 12:

        # Relacionado a IBOV
        if benchmark == 'IBOV':

            juros = (1 + (ibov_hoje_ano + taxa) / 100) ** (1 / 12)  # taxa de juros por mês da aplicação
            for i in range(meses):
                if i == 0:
                    investimento = aporte_inicial * juros ** (meses)
                    valor_final = valor_final + investimento

                else:
                    investimento = aporte_mensal * juros ** (meses - i)
                    valor_final = valor_final + investimento

    return round(valor_final, 2)


# Calculo de toda as combicanocoes possiveis de n investimentos dentro de uma lista de valores
def combs(lst, n):
    return [c for c in combinations(lst, n)], list(combinations(range(len(lst)), n))

# Realiza a soma de todas as combinacoes acima e retorna qual esta mais perto ou acima do valor target
# Ppontos de melhorias:
#       Colocar investimentos ruins na lista de melhor combinação pela soma dos valores chegar mais perto do target
#       Possibilidades: colocar ranking de investimentos e utilizar esse fator no erro
def best_match(lst, target, n):
    best = max(combs(lst, n)[0], key=lambda c: ((sum(c) - target), len(c)))

    index_best = combs(lst, n)[0].index(best)
    index_true = combs(lst, n)[1][index_best]
    return best, index_true


# Funcao que retorna os investimentos escolhidos por nós de acordo com os parametros de entrada do cliente
# Pontos de melhorias:
# 1 - Investimentos a serem oferecidos terao o valor de aporte inicial dividido igualmente entre eles
def best_investments(aporte_inicial, aporte_mensal, meses, target, perfil, df, max=3):
    # Realizar o calculo para n elementos de investimento a serem oferecidos e depois checar qual e o melhor
    for n in range(max):
        # 1 passo: calculo final dos valores de cada investimento
        val_invest_fin = []
        for j in range(df.shape[0]):
            val_invest_fin.append(valor_final_invest(investmentType=df.iloc[j]['investmentType'],
                                                     aporte_inicial=aporte_inicial / (n + 1),
                                                     aporte_mensal=aporte_mensal / (n + 1), meses=meses,
                                                     taxa=df.iloc[j]['Taxas'],
                                                     benchmark=df.iloc[j]['Benchmark']))

        # Adiciona uma coluna de valores finais dos investimentos
        df_invest_val_fin = df.assign(ValorFinal=val_invest_fin)

        # 2 passo: Filtros
        #    - dados de acordo com os requisitos do cliente e que sejam do Safra:
        df_invest_filtered_1 = df_invest_val_fin.loc[(df_invest_val_fin['tempoMin'] <= meses) &
                                                     (df_invest_val_fin['valorMin'] <= aporte_inicial / (n + 1)) &
                                                     (df_invest_val_fin['Issuer'] == 'Safra')]

        #    - retirando investimentos que não estão de acordo com o perfil do investidor:
        if perfil == 1:
            df_invest_filtered_2 = df_invest_filtered_1.loc[(df_invest_filtered_1['investmentType'] == 1) |
                                                            (df_invest_filtered_1['investmentType'] == 3) |
                                                            (df_invest_filtered_1['investmentType'] == 4) |
                                                            (df_invest_filtered_1['investmentType'] == 5) |
                                                            (df_invest_filtered_1['investmentType'] == 10)]

        if perfil == 2:
            df_invest_filtered_2 = df_invest_filtered_1.loc[(df_invest_filtered_1['investmentType'] == 1) |
                                                            (df_invest_filtered_1['investmentType'] == 3) |
                                                            (df_invest_filtered_1['investmentType'] == 4) |
                                                            (df_invest_filtered_1['investmentType'] == 5) |
                                                            (df_invest_filtered_1['investmentType'] == 6) |
                                                            (df_invest_filtered_1['investmentType'] == 10) |
                                                            (df_invest_filtered_1['investmentType'] == 11)]
        else:
            df_invest_filtered_2 = df_invest_filtered_1

        if n + 1 == max:
            winner = best_match(df_invest_filtered_2['ValorFinal'], target, n=max)

    list_index = list(winner[1])

    return df_invest_filtered_2.iloc[list_index]

# Recebe: um df já filtrado com especificacoes de tempo, aporte minimo e investimentos do safra
# Recebe: investimento alvo que se deseja propor outros similares
# Retorna: subset de investimentos similares
def invest_similar(df, winner, productType, valorFinal, dist=0.01):
    range_min = 1 - dist
    range_max = 1 + dist

    # Retirar os elementos ja selecionados pelo algoritmo
    df = df.drop(list(winner.index), axis=0)

    # Filtrando pelos requisitos
    df_similares = df.loc[(df['ValorFinal'] <= valorFinal * range_max) &
                          (df['ValorFinal'] >= valorFinal * range_min) &
                          (df['ProductType'] == productType)]

    return df_similares
