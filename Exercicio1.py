# Sequencia de numeros

maximo = int(input("Digite o numero maximo: "))
ordem = input("Qual a ordem que deseja imprimir o numero C/D: ")

if ordem == 'C':
    for numero in range(1, maximo + 1):
        print(numero)
elif ordem == 'D':
    for numero in range(maximo, 0, -1):
        print(numero)
else:
    print("Ordem invalida!")


