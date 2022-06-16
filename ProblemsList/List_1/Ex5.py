'''
OBJETIVO: INFORMAR SE DOIS NUMEROS SAO IGUAIS OU DIZER QUAL E MAIOR
ENTRADA: 2 NUMEROS INTEIROS
SAIDA: NUMEROS IGUAIS OU NUMERO MAIOR QUE OUTRO 
'''
continuar = True
while continuar is True:

    while continuar is True:
        try:
            num1 = int(input("\nDigite o primeiro numero: \n"))
            break
        except:
            print("Valor inválido")
    
    while continuar is True:
        try:
            num2 = int(input("Digite o segundo numero: \n"))
            break
        except:
            print("Valor inválido")
    
    if num1 > num2:
        print("\nO " + str(num1) + " é maior que " + str(num2))
    elif num1 == num2:
        print("\nO " + str(num1) + " e " + str(num2) + " são iguais")
    else:
        print("\nO " + str(num2) + " é maior que " + str(num1))
    print("------------------------------")
    continuar = input("Gostaria de começar novamente? (S/N): ")

    if continuar == 's' or continuar == 'S':
        continuar = True
    else:
        continuar is False

    
