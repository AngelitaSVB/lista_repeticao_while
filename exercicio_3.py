# Leia um número n e mostre quantos números entre 1 e n são multiplos de 3.

# Lê o número n
n = int(input("Digite um número inteiro positivo: "))

contador = 1
quantidade_multiplos = 0

# Verifica quais números entre 1 e n são múltiplos de 3
while contador <= n:
    if contador % 3 == 0:
        quantidade_multiplos += 1
    contador += 1

# Mostra o resultado
print(f"Entre 1 e {n}, existem {quantidade_multiplos} múltiplos de 3.")
