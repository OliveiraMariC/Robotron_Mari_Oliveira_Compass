
import json


def linha():
    print('=-=' * 51)


def retornar_json():
    with open("Exercícios_Manipulação_Arquivos_Python\json2.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


campeonato = retornar_json()
linha()
linha()

print('\nLISTA CAMPEONATO\n', campeonato, '\n')

linha()
linha()
