# https://rockcontent.com/br/blog/csv/
import pandas as pd

arquivo = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\TabPeriodica.csv', encoding='utf-8', sep=',')
tabPeriodica = arquivo

def menu():
    print('=-=' * 22)
    print('TABELA PERIóDICA')
    print('=-=' * 22)
    print('', 'Símbolo',      '', 'Linha')
    print('2), 'Nome'          5) Coluna')
    print('3) Nº Atômico    6) Estado')
    tabPeriodica= print(input("Digite o número da propriedade desejada para listar os elementos\nou digite 0 para sair: "))

menu()

if tabPeriodica == 1:
            print(arquivo['Simbolo']) 
elif tabPeriodica == 2: 
            print(arquivo['Nome'])
elif tabPeriodica == 3:
            print(arquivo["NumeroAtomico"])
elif tabPeriodica == 4:
            print(arquivo["Linha"])
elif tabPeriodica == 5:
            print(arquivo["Coluna"])
elif tabPeriodica == 6:
            print(arquivo["EstadoFisico"])
else:
 print("Obrigada por usar a aplicação!")

