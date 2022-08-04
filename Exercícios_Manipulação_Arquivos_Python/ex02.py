import _json
import json

def json_retornar():
    with open('json2.json', encoding = 'utf8') as json_2:
        json_manipulavel = json.load(json_2)
        return json_manipulavel
        
partida = json_retornar()


campeonato = partida['copa-do-brasil'][0]
mandante = campeonato['time_mandante']
visitante = campeonato['time_visitante']

placar_mandante = campeonato["placar_mandante"]
placar_visitante = campeonato["placar_visitante"]
time_mandante = mandante["nome_popular"]
time_visitante = visitante["nome_popular"]

if placar_mandante > placar_visitante:
    print('QUEM FOI O "GRANDE VENCEDOR"!')
    print(time_mandante)
else:
    print('QUEM FOI O "GRANDE VENCEDOR"!')
    print(time_visitante)
