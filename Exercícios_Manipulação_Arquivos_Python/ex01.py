import json

def json_retornar():
    with open("json1.json", encoding="utf-8") as json_1:
        json_manipulavel = json.load(json_1)
        return json_manipulavel
        
partida = json_retornar()
print(partida)
