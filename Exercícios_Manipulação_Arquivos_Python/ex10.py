
import pandas as pd


def linha():
    print('=-=' * 22)


vencedores = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\Oscar.csv', encoding='UTF-8',
                         sep=',', usecols=['Name', 'Movie', 'Year'])
linha()
print("\nOs primeiros 10 vencedores do Oscar de melhor ator foram:\n")
linha()
print(vencedores.loc[0:9])
linha()
