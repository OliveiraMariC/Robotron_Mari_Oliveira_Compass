#chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/
# http://netto.ufpel.edu.br/lib/exe/fetch.php?media=listadeexercicios4-aula6-7-8-solucao.pdf
def linha():
    print('-=-' * 21)


def fat(num):
    if num >= 0:
        fat = num
        for i in range(num, 0, -1):
            fat = fat * i
        linha()
        print('\nO número', num, 'é par e o resultado de sua fatoração é igual a', fat, '.')
    else:
        linha()
        print('\nO número', num, ' é par mas não existe fatorial para número negativo.')


def tabuada(n):
    print('\nSeu número é ímpar vou te apresentar a tabuada deste número:\n')
    linha()
    for i in range(0, 11):
        mult = i * n
        print(n, 'x', i, '=', mult)
    linha()


linha()
num = int(input('\nInforme um número inteiro: '))
if num % 2 == 0:
    print(fat(num))
    linha()
else:
    tabuada(num)
