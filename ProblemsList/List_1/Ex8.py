'''
OBJETIVO: Informar a categoria de um jogador de futebol de acordo com a idade
ENTRADA: Idade
SAIDA: Categoria (infantil, juvenil ou sênior)
'''
idade = None
condicao = False
vezes = 0

while condicao == False:
    try:
        if vezes == 0:
            idade = int(input("Digite sua idade: \n"))
            if idade < 0 or idade == 0:
                print("Valor inválido\n")
                condicao = False
            if idade > 0:
                condicao = True
        else:
            idade = int(input())
            break
    except ValueError:
        print("\nValor inválido. Digite novamente: ")
        vezes += 1


if idade <= 13:
    print("\nCategoria: INFANTIL")
    print("------------")
if idade >= 13 and idade <= 17:
    print("------------")
    print("\nCategoria: JUVENIL")
if idade > 17:
    print("------------")
    print("\nIdade: JUVENIL")

