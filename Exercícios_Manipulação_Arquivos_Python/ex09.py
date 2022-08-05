import pandas as pd


def linha():
    print('=-=' * 22)


age = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\Oscar.csv',
                  encoding='UTF-8', sep=',', usecols=['Age'])
linha()
print('\n', age, '\n')
linha()
