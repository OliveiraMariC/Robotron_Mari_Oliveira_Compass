# https://rockcontent.com/br/blog/csv/
import pandas as pd

arquivo = pd.read_csv('Robotron_Mari_Oliveira_Compass\Exercícios_Manipulação_Arquivos_Python\TabPeriodica.csv', sep=',')
tabPeriodica = arquivo

tp = ()
def menu():
    print('=-=' * 22)
    print('TABELA PERIóDICA')
    print('=-=' * 22)
    print('1) Símbolo       4) Linha')
    print('2) Nome          5) Coluna')
    print('3)  Atômico    6) Estado')
    
    
while tp != 0: 
    menu()
    tp = (int(input("Digite o número número desejado: ")))
    print(" ")
    if tp == 1:
        print(tabPeriodica, ["Simbolo"])
    elif tp == 2: 
        print(tabPeriodica, ["Nome"])
    elif tp == 3:
        print(tabPeriodica,["Natomico"])
    elif tp == 4:
        print(tabPeriodica,["Linha"])
    elif tp == 5:
        print(tabPeriodica,["Coluna"])
    elif tp == 6:
        print(tabPeriodica,["EF"])
    print(" ")
if tp == 0:
    print("Volte sempre")      


    
     


