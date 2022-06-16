'''
OBJETIVO: INFORMAR O NOME, SALARIO FIXO E O SALARIO NO FINAL DO MES DE UM VENDEDOR
ENTRADA: NOME, SALARIO FIXO E TOTAL DE VENDAS EM DINHEIRO REALIZADAS NO MES
SAIDA: NOME, SALARIO FIXO E SALARIO FINAL
'''

while(True):
    nome = input("\n\nDigite o nome do vendedor: ")
    salario_fixo = float(input("Digite o salario fixo do vendedor: "))
    total_vendas = float(input("Digite o total de vendas em dinheiro realizadas pelo vendedor: "))

    salario_final = salario_fixo + (total_vendas * 0.20)

    print("Nome: " + nome + "\nSalario Fixo: " + str(salario_fixo) + "\nSalario Final: " + str(salario_final))







