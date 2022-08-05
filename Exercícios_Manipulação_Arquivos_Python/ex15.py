import pandas as pd

vencedores = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\Oscar.csv', encoding='UTF-8', sep=',')
movies = pd.read_csv('Oscar.csv', encoding='UTF-8', sep=',', usecols=['Movie'])

print(movies[movies['Movie'] != "The Revenant"])