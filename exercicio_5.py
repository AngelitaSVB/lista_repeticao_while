# Peça um número ao usuário e imprima sua tabuada de 1 a 10 usando while.

# Solicita o número ao usuário
numero = int(input("Digite um número para ver sua tabuada: "))

contador = 1

# Loop para imprimir a tabuada de 1 a 10
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
