nome = (input('Qual seu nome?\n'))
idade = int(input("Qual sua a idade?\n"))

anos = idade // 365
idade %= 365
meses = idade // 30
idade %= 30

print(nome, idade, anos, meses, "ano(s)")
#print(meses, "mes(es)")
#print(idade, "dia(s)")