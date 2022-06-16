'''
OBJETIVO: Obter um nome do aluno e as notas dos 3 semestres e informar a media aritmética
ENTRADA: nome, 3 notas
SAIDA:  nome, media aritmetica
'''
from statistics import mean

nome = input("Nome do aluno: ")
media_aritmetica = []
nota1 = float(input("Nota 1: "))
media_aritmetica.append(nota1)
nota2 = float(input("Nota 2: "))
media_aritmetica.append(nota2)
nota3 = float(input("Nota 1: "))
media_aritmetica.append(nota3)
print("Nome: " + nome.title())
print("Media: " + str(mean(media_aritmetica)))