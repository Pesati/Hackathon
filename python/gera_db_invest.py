import numpy as np
import pandas as pd
import random

# Lendo o arquivo base para criar o banco de dados
df_invest = pd.read_csv("API_investimentos.csv", sep=';')

# Script utilizado para gerar banco de dados ficticios de investimentos

# Lista de bancos e outras variáveis

# Indices utilizados no mercado financeiro
cdi_hoje_ano = 11.61
cdi_hoje_mes = 0.92

ipca_hoje_ano = 10.54
ipca_hoje_mes = 0.83

selic_hoje_ano = 11.75

ibov_ano = 21.19

# Nomes de bancos ficticios e do safra para popular o dataframe
bancos = ['Safra', 'Banco A', 'Banco B', 'Banco C']

valorMin_CBD = [1000, 3000, 7000, 10000, 30000, 100000]

valorMin_deb = [100, 500, 1000, 500, 1000, 500, 1000, 500, 1000, 500, 1000, 500, 1000, 2500, 5000, 10000, 50000, 100000]

taxas_CDB = [np.random.uniform(90, 120) for x in range(50)]

taxas_LC_CDB = [np.random.uniform(80, 105) for x in range(50)]

tempoMin = [6, 12, 18, 24, 30, 36]

tempoMin_deb = [72, 108, 108, 108, 108, 120, 120, 120, 144, 144, 180, 240]

# Criacao dos investimentos
# ProductType = 0:  Renda Fixa Bancaria
# ProductType = 1: Renda Fixa Credito
# ProductType = 2: Renda Variavel

# InvestmentType = 1: CDB
# InvestmentType = 2: RDB
# InvestmentType = 3: LCI
# InvestmentType = 4: LCA
# InvestmentType = 5: Titulo do Tesouro
# InvestmentType = 6: Debentures
# InvestmentType = 7: CRI
# InvestmentType = 8: CRA
# InvestmentType = 9: Acoes
# InvestmentType = 10: Fundos de Renda Fixa
# InvestmentType = 11: Fundos Multimercado
# InvestmentType = 12: Fundos Renda Variavel

# Criando CDBs - baseado no CDI
ProductType = 0
investmentType = 1
n = 100  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_CBD[random.randint(0, 5)],
        'tempoMin': tempoMin[random.randint(0, 5)],
        'tempoMax': 0,
        'Taxas': int(taxas_CDB[random.randint(0, len(taxas_CDB) - 1)]),
        'Benchmark': 'CDI'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando LCIs - baseada no CDI
ProductType = 0
investmentType = 3
n = 80  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_CBD[random.randint(0, 5)],
        'tempoMin': tempoMin[random.randint(0, 5)],
        'tempoMax': 0,
        'Taxas': int(taxas_LC_CDB[random.randint(0, len(taxas_LC_CDB) - 1)]),
        'Benchmark': 'CDI'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)
# Criando LCIs - baseada no IPCA
ProductType = 0
investmentType = 3
n = 20  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_CBD[random.randint(0, 5)],
        'tempoMin': tempoMin[random.randint(0, 5)],
        'tempoMax': 0,
        'Taxas': round(random.uniform(3, 4), 2),
        'Benchmark': 'IPCA'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando LCAs - baseado no CDI
ProductType = 0
investmentType = 4
n = 80  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_CBD[random.randint(0, 5)],
        'tempoMin': tempoMin[random.randint(0, 5)],
        'tempoMax': 0,
        'Taxas': int(taxas_LC_CDB[random.randint(0, len(taxas_LC_CDB) - 1)]),
        'Benchmark': 'CDI'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando LCAs - baseado no IPCA
ProductType = 0
investmentType = 4
n = 20  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_CBD[random.randint(0, 5)],
        'tempoMin': tempoMin[random.randint(0, 5)],
        'tempoMax': 0,
        'Taxas': round(random.uniform(3, 4), 2),
        'Benchmark': 'IPCA'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando Tesouro Direto - baseada no IPCA
ProductType = 0
investmentType = 5
n = 20  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': round(random.uniform(30, 45), 2),
        'tempoMin': 0,
        'tempoMax': 0,
        'Taxas': round(random.uniform(3, 4), 2),
        'Benchmark': 'IPCA'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)
# Criando Tesouro Direto - baseada no SELIC
ProductType = 0
investmentType = 5
n = 20  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_CBD[random.randint(0, 5)],
        'tempoMin': 0,
        'tempoMax': 0,
        'Taxas': round(random.uniform(0.05, 0.2), 2),
        'Benchmark': 'SELIC'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)
# Criando Tesouro Direto - baseada no PREFIXADO
ProductType = 0
investmentType = 5
n = 20  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_CBD[random.randint(0, 5)],
        'tempoMin': 0,
        'tempoMax': 0,
        'Taxas': round(random.uniform(11, 12), 2),
        'Benchmark': 'PRE'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando Debentures - baseado no IPCA
ProductType = 1
investmentType = 6
n = 50  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': round(random.uniform(1000, 1200), 2),
        'tempoMin': tempoMin_deb[random.randint(0, len(tempoMin_deb) - 1)],
        'tempoMax': 0,
        'Taxas': round(random.uniform(4.5, 7.5), 2),
        'Benchmark': 'IPCA'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando Debentures - baseado no CDI
ProductType = 1
investmentType = 6
n = 20  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': round(random.uniform(1000, 1200), 2),
        'tempoMin': tempoMin_deb[random.randint(0, len(tempoMin_deb) - 1)],
        'tempoMax': 0,
        'Taxas': round(random.uniform(1, 3), 2),
        'Benchmark': 'CDI'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando Fundos de Renda Fixa - Baseado no CDI
ProductType = 2
investmentType = 10
n = 100  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_deb[random.randint(0, len(valorMin_deb) - 1)],
        'tempoMin': tempoMin_deb[random.randint(0, len(tempoMin_deb) - 1)],
        'tempoMax': 0,
        'Taxas': round(random.uniform(-0.20, 5), 2),
        'Benchmark': 'CDI'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando Fundos de Renda Fixa - Baseado no IPCA
ProductType = 2
investmentType = 10
n = 50  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_deb[random.randint(0, len(valorMin_deb) - 1)],
        'tempoMin': tempoMin_deb[random.randint(0, len(tempoMin_deb) - 1)],
        'tempoMax': 0,
        'Taxas': round(random.uniform(-0.1, 6), 2),
        'Benchmark': 'IPCA'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando Fundos Multimercado - Baseado no IPCA
ProductType = 2
investmentType = 11
n = 100  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_deb[random.randint(0, len(valorMin_deb) - 1)],
        'tempoMin': tempoMin_deb[random.randint(0, len(tempoMin_deb) - 1)],
        'tempoMax': 0,
        'Taxas': round(random.uniform(-0.1, 12), 2),
        'Benchmark': 'IPCA'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Criando Fundos de Renda Variável - Baseado no IBOV
ProductType = 2
investmentType = 12
n = 100  # número de investimentos a serem criador
for i in range(n):
    df_input_cdb = {
        'Issuer': bancos[random.randint(0, 3)],
        'ProductType': ProductType,
        'investmentType': investmentType,
        'valorMin': valorMin_deb[random.randint(0, len(valorMin_deb) - 1)],
        'tempoMin': tempoMin_deb[random.randint(0, len(tempoMin_deb) - 1)],
        'tempoMax': 0,
        'Taxas': round(random.uniform(-10, 20), 2),
        'Benchmark': 'IBOV'}
    df_invest = df_invest.append(df_input_cdb, ignore_index=True)

# Saving dataframe to excel and/or csv
df_invest.to_csv('investimentos_bd.csv', index=False)
df_invest.to_excel('investimentos_bd.xlsx')
