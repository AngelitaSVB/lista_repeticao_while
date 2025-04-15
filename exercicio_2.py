# Leia um número n. Em seguida, leia n números inteiros e calcule a soma deles. Mostre o resultado no final.

# Solicita ao usuário a quantidade de números a serem somados
n = int(input("Digite a quantidade de números inteiros que deseja somar: "))

contador = 0
soma = 0

# Loop para ler e somar os n números inteiros
while contador < n:
    numero = int(input(f"Digite o {contador + 1}º número inteiro: "))
    soma += numero
    contador += 1

# Exibe o resultado da soma
print("A soma dos números é:", soma)

    
    


