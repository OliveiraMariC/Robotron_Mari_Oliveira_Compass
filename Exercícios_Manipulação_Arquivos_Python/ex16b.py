#B) Listar todos os dados de determinado elemento, buscando através do seu símbolo.

import pandas as pd

tabPeriodica = pd.read_csv('Robotron_Mari_Oliveira_Compass\Exercícios_Manipulação_Arquivos_Python\TabPeriodica.csv', sep=",")
def menu():
    print('=-=' * 22)
    print('TABELA PERIóDICA')
    print('=-=' * 22)
    print('1) Símbolo       4) Linha')
    print('2) Nome          5) Coluna')
    print('3) Nº Atômico    6) Estado')
    
menu()
print('Escolha um dos símbolos abaixo para buscar os dados desse elemento:')

tabPeriodica = tabPeriodica
print(tabPeriodica)

simb=input("Digite o símbolo escolhido: ")

print(tabPeriodica,simb,'\n')