def linha():
    print('-=-' * 18)


linha()
print("\nDigite 15 números inteiros. ", '\n')
linha()

lista = [int(input("\nNúmero: "))
         for i in range(0,15)]

lista.reverse()
linha()
print("\nA lista invertida dos números fica assim:", lista)
linha()