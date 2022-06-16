'''
OBJETIVO: Dizer se um número está ou não no intervalo de 200 e 300
ENTRADA: 1 número
SAIDA: informação contendo se está ou não no intervalo de 200 e 300
'''
valor1 = int(input("Digite o valor do primeiro numero do intervalo: "))
valor2 = int(input("Digite o valor do segundo número do intervalo: "))

num1 = int(input("Digite o valor do número: "))

if num1 > valor1 and num1 < valor2:
    print("O " + str(num1) + " pertence ao intervalo de " + str(valor1) + " e " + str(valor2))


else:
    print("O " + str(num1) + " não pertence ao intervalo entre " + str(valor1) + " e " + str(valor2))