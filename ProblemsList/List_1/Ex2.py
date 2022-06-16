num1 = int(input("Digite o valor do primeiro numero: "))
num2 = int(input("Digite o valor do segundo numero: "))

contas = [num1 + num2, num1 - num2, num1 * num2, num1 / num2]

operacoes = ["Soma: ", "Subracao: ", "Divisao: ", "Multiplicaçao: "]

for i in range(0,4):
    print(operacoes[i] + str(contas[i]))

    