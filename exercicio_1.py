# Peça para o usuario digitar um numero inteio positivo n. Imprima na tela os números de 1 até n, um por linha.

# Solicita ao usuário um número inteiro positivo 
numero_inteiro = int(input("Digite um número inteiro positivo: "))

# Inicializa o contador
contador = 0

# Loop para imprimir os números de 1 até n
while contador < numero_inteiro:
    contador += 1
    print(contador)
    