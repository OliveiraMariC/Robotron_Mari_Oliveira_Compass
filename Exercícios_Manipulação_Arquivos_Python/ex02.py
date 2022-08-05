
import json
def linha():
    print('=-=' * 22)
def json_retornar():
    with open('Exercícios_Manipulação_Arquivos_Python\Oscar.csv', encoding = 'utf8') as json_1:
        json_manipulavel = json.load(json_1)
        return json_manipulavel
    
partida = json_retornar()
campeonato = partida['copa-do-brasil'][0]
mandante = campeonato['time_mandante']
visitante = campeonato['time_visitante']

placar_mandante = campeonato['placar_mandante']
placar_visitante = campeonato['placar_visitante']
time_mandante = mandante['nome_popular']
time_visitante = visitante['nome_popular']

if placar_mandante > placar_visitante:
    linha()
    print('\nQUEM FOI O "GRANDE VENCEDOR"!\n')
    linha()
    print(time_mandante)
    linha()
else:
    linha()
    print('\QUEM FOI O "GRANDE VENCEDOR"!')
    linha()
    print(time_visitante)
