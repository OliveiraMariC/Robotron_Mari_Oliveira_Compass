

from cProfile import label
import pandas as pd

vencedores = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\Oscar.csv', encoding='UTF-8', sep=',')

print(vencedores['Nome'][59:72].map(str) + " " + vencedores['Year'][59:72].astype(str))

