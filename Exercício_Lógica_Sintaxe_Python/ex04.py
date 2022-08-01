
# https://www.youtube.com/watch?v=j9bYDjaAYzw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=2

print('\nConforme sua idade vamos dizer se você é um ADULTO, um ADOLESCENTE ou uma CRIANÇA!\n')
print('Vamos começar!\n')

idade = int(input('Digite sua idade: '))

if idade > 18:
    print('\nCom', idade, 'anos você já atingiu a maioridade, portanto é um Adulto!')

elif idade >= 12 <= 18:
    print('\nCom', idade, 'anos você é um Adolescente!\n')

elif idade >= 0 < 12:
    print('\nCom', idade, 'anos você ainda é uma criança!\n')

else:
    print('\nEsse número não é válido!\n')

    print('Volte sempre!\n')
