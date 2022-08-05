#Pedro que nos deu a dica de como corrigir o erro YEAR com .map e não .astype

import pandas as pd
def linha():
    print('=-=' * 22)

filmes = pd.read_csv('Exercícios_Manipulação_Arquivos_Python\Oscar.csv', encoding="utf-8", sep=",")

filmes["filme_ano"] = filmes["Movie"] + " - " + filmes["Year"].map(str)
linha()
print(filmes["filme_ano"])
linha()
