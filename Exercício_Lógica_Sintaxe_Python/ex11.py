#https://www.youtube.com/watch?v=L1Qnyna43rU

def linha():
    print('-=-' * 25)


linha()
print('\nDURAÇÃO DA PARTIDA ENTRE OS "COM CAMISA" E OS "SEM CAMISA"!\n')
linha()
i = int(input('Digite a hora de início da partida com formato de 24h: '))
f = int(input('\nDigite a hora do final da partida com formato de 24h: '))
linha()
tempo = int(f - i)
if tempo < 0:
    print('\nA duração da partida foi de:', tempo + 24, 'horas.')
elif tempo == 0:
    print('\nA duração da partida foi de 24 horas')
else:
    print('\nA duração da partida foi de', tempo, 'horas.\n')
    
linha()
