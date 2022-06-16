'''
Escreva um programa em C# que solicite o nome do usuário e indique o dia em que ele
deve comparecer ao posto de vacinação, considerando a regra:
Dia da semana/ Letra inicial do primeiro nome
Segunda-feira – de A a C; Terça - feira – de D a G; Quarta - feira – de H a L;
Quinta - feira – M; Sexta - feira – de N a Q; Sábado – de R a S; Domingo – de T a Z.
'''
tuple_letter = (['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i', 'j', 'k', 'l'], ['m'], ['n', 'o', 'p', 'q'], ['r', 's', 't'], ['u', 'v', 'w', 'x', 'y', 'z'])
tuple_week = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado", "Domingo"] 
dictionary = dict(zip(tuple_week, tuple_letter))
print(dictionary)
name = input("Digite seu nome: \n")
for key, value in dictionary.items():
  if name.lower()[0] in value:
    print(name.capitalize() , ", you should go to the hospital on " , key)
# Essa abordagem sua diferença é no comando zip() que constroi um dicionário a partir de 2 listas diferentes

'''
ABORDAGEM 1
Se baseia na ideia que criei 2 listas 2d independentes que propositalmente estão na mesma ordem de acordo com sua atribuição: 
- "Segunda feira" e ['a','b','c'] estão na posição 0 
    
tuple_letra = (['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i', 'j', 'k', 'l'], ['m'], ['n', 'o', 'p', 'q'], ['r', 's', 't'], ['u', 'v', 'w', 'x', 'y', 'z'])

tuple_semana = ["Segunda Feira", "Terça Feira", "Quarta Feira", "Quinta Feira", "Sexta Feira", "Sabado", "Domingo"] 

nome = input("Digite o seu nome: \n")
i = 0
for grupo in tuple_letra:
    if grupo.count(nome[0].lower()) >= 1:
         print(nome + ", voce comparecer ao posto de saude no " + tuple_semana[i])
         break
    i += 1

ABORDAGEM 2
Semelhante a abordagem 1 com exceção que está utilizando do statement "in" para checar se o nome[0] está dentro da lista invés de count(), e utilizando um dicionário
example_dict = {
    "Monday": ['a', 'b', 'c'],
    "Tuesday": ['d', 'e', 'f', 'g'],
    "Wednesday": ['h', 'i', 'j', 'k', 'l'],
    "Thursday": ['m'],
    "Friday": ['n', 'o', 'p', 'q'],
    "Saturday": ['r', 's', 't'],
    "Sunday": ['u', 'v', 'w', 'x', 'y', 'z']
}
name = input("Name: \n")

if len(name) > 0:
    for i in example_dict:
        # Lower case the letter for comparison
        if name[0].lower() in example_dict[i]:
            print(name + ", you should go to the hospital on " + i)

'''

