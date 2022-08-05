import json

def linha():
    print('=-=' * 38)


def retornar_json():
    with open("Exercícios_Manipulação_Arquivos_Python\json1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


partida = retornar_json()

campeonato = partida['copa-do-brasil'][0]
visitante = campeonato['time_visitante']

time_visitante_id = visitante["time_id"]
time_visitante = visitante["nome_popular"]
time_visitante_sigla = visitante["sigla"]
time_visitante_escudo = visitante["escudo"]
linha()
print('\nO time visitante é o', time_visitante, 'de ID', time_visitante_id,
      ' sua sigla é', time_visitante_sigla,'.\n' '\nO escudo você vai encontrar neste link(', time_visitante_escudo, ')\n')
linha()