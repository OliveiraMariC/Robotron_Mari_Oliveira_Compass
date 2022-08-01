
# https://www.youtube.com/watch?v=cL4YDtFnCt4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=60


print('\nLista de valores númericos de 1 a 20:\n ')

soma = 0
valor = 0

for v in range(1, 21):
    if v % 2 == 0:
        soma += v
        valor += 1
        media = soma / valor
        print('Número =', v,)

print('\nA lista trouxe', valor, 'números PARES e a soma dos valores é',
      soma, '. A média desses valores é',
      media, '.\n')
