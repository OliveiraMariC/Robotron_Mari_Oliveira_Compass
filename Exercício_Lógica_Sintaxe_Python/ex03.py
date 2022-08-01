# https://www.youtube.com/watch?v=4vFCzKuHOn4&t=95s

def linha():
    print('-' * 60)


linha()

print('Vamos descobrir se a soma dos números é ímpar ou par! ')

linha()

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('\nDigite o segundo número: '))
soma = int(numero1 + numero2)
resultado = soma / 2
resto = soma % 2


if resto == 0:

    linha()

    print('A soma dos números é', soma, 'seu número é PAR.')

    linha()
else:

    linha()

    print('A soma dos números é', soma, 'seu número é ÍMPAR.')

    linha()
