def linha():
    print('-=-' * 16)  
lista_fruteira = ['maçã', 'banana', 'pera']
linha()
print('\nVAMOS AS COMPRAS!!!\n')
linha()
print('Qual fruta você vai comprar?\n')
compra_feira = [str(input(" "))
                for i in range(3)]

iguais = [fruta for fruta in lista_fruteira if fruta in compra_feira]

if len(iguais) == 0:
    linha()
    print("\nNenhuma dessas frutas temos na fruteira.")
    linha()

else:
    linha()
    print("\nNão precisa, já temos essas frutas!")
    linha()