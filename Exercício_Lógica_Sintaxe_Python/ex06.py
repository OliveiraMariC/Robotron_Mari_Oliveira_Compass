
# https://www.youtube.com/watch?v=rJaBLOW57Jg&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=1


def linha():
    print('-' * 75)


linha()

valor = int(input(
    'Digite um número maior que 2 para descobrirmos quantos ímpares teremos: '))

linha()

x = 0
contador = 0

for valor in range(x, valor ):
    if valor % 2 == 1:
        contador += 2
        print(valor)

linha()

print('Na sequência de', x, 'a', valor, 'temos', contador, 'ÍMPARES.')

linha()
