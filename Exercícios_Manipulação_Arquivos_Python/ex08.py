
import pandas as pd


def linha():
    print('=-=' * 25)


arquivo = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\Oscar.csv', encoding='UTF-8', sep=',')
linha()
print('\n', arquivo, '\n')
linha()
