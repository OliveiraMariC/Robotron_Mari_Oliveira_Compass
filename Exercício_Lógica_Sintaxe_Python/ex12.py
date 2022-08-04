#https://www.youtube.com/watch?v=TgdnbnmT44s

idade = int(input('Digite sua idade multiplicada por 365: '))

anos = (idade // 365)
meses = (idade % 365) // 30
dias = (idade % 365) % 30

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))