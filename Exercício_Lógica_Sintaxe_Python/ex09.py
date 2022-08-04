def linha():
    print('-=-' * 16)


linha()
print("Digite 15 números inteiros. ")
linha()

lista = [int(input("Número: "))
         for i in range(15)]

lista.reverse()
print("A lista invertida dos números fica assim:\n", lista)