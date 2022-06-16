'''
OBJETIVO: Fazer um programa para calcular o preço de xerox com valor de 0,50 até 200 folhas, e para acima de 200 folhas 0,30
ENTRADA:
SAIDA:
'''
num_folhas = 0
inteiro = False
vezes = 0
while inteiro is False:
    try:
        if vezes == 0:
            num_folhas = int(input("Digite o numero de folhas que deseja comprar: "))
            inteiro = True
        else:
            num_folhas = int(input())
            inteiro = True

    except:
        print("\nNumero inválido. Por favor digite novamente: ")
        vezes += 1
    

if num_folhas <= 200:
    valor = num_folhas * 0.50
else:
    valor = num_folhas * 0.30

print("-------------------")
print("CAIXA")
if num_folhas > 1 or num_folhas == 0:
    print("\nFolhas | " + str(num_folhas) + " unidades")
else:
    print("\nFolhas | " + str(num_folhas) + " unidade")
print("\nTOTAL: " + "R$" + str(valor))
print("-------------------")