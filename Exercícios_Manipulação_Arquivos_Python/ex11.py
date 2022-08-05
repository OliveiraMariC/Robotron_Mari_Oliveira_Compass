
import pandas as pd

def linha():
    print('=-=' * 22)
vencedor = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\Oscar.csv', encoding='UTF-8', sep=',')
vencedor_93 = (vencedor.loc[vencedor['Year'] == 1993])

nome_vencedor = pd.DataFrame(vencedor_93, columns=['Name'])
linha()
print("\nO vencedor do Oscar em 1993 foi:\n")
print(nome_vencedor,'\n')
linha()
