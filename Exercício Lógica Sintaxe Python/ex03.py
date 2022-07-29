#https://www.youtube.com/watch?v=4vFCzKuHOn4&t=95s

print('\nVamos descobrir se a soma dos números é ímpar ou par!\n ')

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('\nDigite o segundo número: '))
soma = int (numero1 + numero2)
resultado = soma / 2  
resto = soma % 2


if resto == 0:
    print('\nA soma dos números é',soma,'seu número é PAR.\n')
else:
    print('\nA soma dos números é',soma,'seu número é ÍMPAR.\n')


