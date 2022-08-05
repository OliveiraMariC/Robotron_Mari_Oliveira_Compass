
import json


def linha():
    print('=-=' * 29)


def retornar_json():
    with open("Exercícios_Manipulação_Arquivos_Python\json2.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


campeonato = retornar_json()

edicao_atual = campeonato['edicao_atual']['edicao_id']
fase_atual = campeonato['fase_atual']['fase_id']
rodada_atual = campeonato['rodada_atual']['nome']
linha()
print(f'\nO Campeonato Brasileiro 2021 tem o ID', edicao_atual,
      '.A atual fase tem o ID', fase_atual, 'e está na', rodada_atual,'\n')
linha()
