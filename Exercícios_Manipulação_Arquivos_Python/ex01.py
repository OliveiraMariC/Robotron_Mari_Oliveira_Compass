import json 
def linha():
    print('=-=-=' * 31)
def json_retornar():
    with open('Exercícios_Manipulação_Arquivos_Python\json1.json', encoding = 'utf8') as json_1:
        json_manipulavel = json.load(json_1)
        return json_manipulavel
    
partida = json_retornar()

linha()
print(partida)
linha()
