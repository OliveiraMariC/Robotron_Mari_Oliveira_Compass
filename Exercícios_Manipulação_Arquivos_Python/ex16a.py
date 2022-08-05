# https://rockcontent.com/br/blog/csv/
import pandas as pd

arquivo = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\TabPeriodica.csv', encoding='utf-8', sep=',')
tabPeriodica = arquivo
num = ('')
num = (print(input("Digite o número desejado: ")))
def menu():
    print('=-=' * 22)
    print('TABELA PERIóDICA')
    print('=-=' * 22)
    print('1) Símbolo       4) Linha')
    print('2) Nome          5) Coluna')
    print('3) Nº Atômico    6) Estado')
    print('')
num = (print(input("Digite o número desejado: ")))

menu()

if num == 1:
            print(arquivo['Simbolo']) 
elif num == 2: 
            print(arquivo['Nome'])
elif num == 3:
            print(arquivo["NumeroAtomico"])
elif num == 4:
            print(arquivo["Linha"])
elif num == 5:
            print(arquivo["Coluna"])
elif num == 6:
            print(arquivo["EstadoFisico"])
elif num == 0:
     print("Obrigada por usar a aplicação!")

