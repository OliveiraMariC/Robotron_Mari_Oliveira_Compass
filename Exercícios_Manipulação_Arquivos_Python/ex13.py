import pandas as pd
def linha():
    print('=-=' * 22)
vencedores = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\Oscar.csv', encoding='UTF-8', sep=',')

vencedores['Movie_Year'] = vencedores['Movie'] + " " + vencedores['Year'].astype(str)
linha()

print(vencedores['Movie_Year'])
linha()