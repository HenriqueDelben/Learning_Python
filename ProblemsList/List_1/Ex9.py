from statistics import mean
while (True):
    repeticoes = 0
    quantidade = 0
    numero = 0
    numeros = []
    par = []
    impar = []
    try:
        if quantidade == 0: 
            quantidade = int(input("Digite quantos numeros voce quer inserir: "))
            break
        elif quantidade > 0:
            quantidade = int(input())
    except:
        print("Valor inválido. Digite novamente:")

for i in range(0, quantidade):
    numero = int(input("Digite o " + str(i + 1) + " número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero) # capturando numeros pares
    else:
        impar.append(numero) # capturando numeros ímpares

print("Maior número: " + str(max(numeros)))
print("Menor número: " + str(min(numeros)))
print("Media aritmética: " + str(mean(numeros))) 
print("Numeros pares: " + str(par))
print("Numeros impares: " + str(impar))