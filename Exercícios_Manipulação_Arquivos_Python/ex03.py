import json


def linha():
    print('=-=' * 33)


def retornar_json():
    with open("Robotron_Mari_Oliveira_Compass\Exercícios_Manipulação_Arquivos_Python\json1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


partida = retornar_json()

campeonato = partida['copa-do-brasil'][0]
estadio = campeonato['estadio']

placar_mandante = campeonato["placar_mandante"]
placar_visitante = campeonato["placar_visitante"]
nome_estadio = estadio["nome_popular"]
status = campeonato["status"]
linha()
print('\n                      FIM DE JOGO!!!\n')
linha()


print('\nEstá', status, 'o jogo no estádio', nome_estadio,
      'e o resultado foi SANTO ANDRÉ', placar_mandante, 'x', placar_visitante, 'CRICIÚMA!!\n')
linha()
