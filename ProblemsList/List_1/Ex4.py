'''
OBJETIVO: INFORMAR O NOME E MEDIA PONDERADA DE UM ALUNO
ENTRADA: NOME, NOTA 1, NOTA 2 E NOTA 3 
SAIDA: NOME E MEDIA PONDERADA
'''

from ast import Try


print("------------------------------")

while True:
    nome = input("Aluno: \n")

    # posso usar um float e um int consecutivos apos um string
    nota1 = float(input("Nota 1: \n"))
    nota2 = float(input("Nota 2: \n"))
    nota3 = float(input("Nota 3: \n"))

    media_ponderada = (nota1 * 2 + nota2 * 4 + nota3 * 6) / 12

    print("\n\n")
    print("Nome:", nome)
    print("Media ponderada:", media_ponderada)
    print("------------------------------")

    resposta = input("Gostaria de consultar mais um aluno? (S/N)\n")
    print("------------------------------\n")
    if resposta == 's' or resposta == 'S':
        repetir = True