import json
def linha():
    print('=-=' * 52)

def retornar_json():
    with open("Exercícios_Manipulação_Arquivos_Python\json1.json", encoding="utf-8") as json_normal:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel


campeonato = retornar_json()
linha()
for chave in campeonato:
    print(chave, ":", campeonato[chave])
linha()