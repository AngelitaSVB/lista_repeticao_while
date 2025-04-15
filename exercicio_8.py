# Peça um número inteiro positivo e calcule seu fatorial usando while.

# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa as variáveis
fatorial = 1
contador = 1

# Calcula o fatorial usando while
while contador <= numero:
    fatorial *= contador
    contador += 1

# Exibe o resultado
print(f"O fatorial de {numero} é: {fatorial}")
