import pandas as pd


def linha():
    print('=-=' * 22)


vencedores = pd.read_csv(
    'Exercícios_Manipulação_Arquivos_Python\Oscar.Csv', encoding='UTF-8', sep=',')
vencedor_periodo = (vencedores.loc[63:88])
print(vencedor_periodo)

nome_vencedor = pd.DataFrame(vencedor_periodo, columns=['Name'])
linha()
print("\nOs vencedores do Oscar entre 1991 e 2016 foram:")
linha()
print(nome_vencedor, '\n')
linha()
