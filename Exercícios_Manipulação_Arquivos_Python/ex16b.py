#B) Listar todos os dados de determinado elemento, buscando através do seu símbolo.

from typing_extensions import Self
import pandas as pd

tabPeriodica = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\TabPeriodica.csv', sep=",")

print('Escolha um dos símbolos abaixo para buscar os dados desse elemento:')
tabPeriodica = tabPeriodica['Símbolo'].csvindex
print(tabPeriodica)

simb=input("Digite o símbolo escolhido: ")
print(" ")
print(tabPeriodica[tabPeriodica["Simbolo"] == (simb)])