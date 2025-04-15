# Solicite ao uruário que digite várias notas. O programa só termina quando for digitada nota negativa. Em seguida, calcule a média das notas válidas.

# Inicializa as variáveis
soma_notas = 0
quantidade_notas = 0

# Solicita as notas ao usuário até que uma nota negativa seja digitada
while True:
    nota = float(input("Digite uma nota (negativa para sair): "))
    
    if nota < 0:
        break  # Sai do loop quando a nota for negativa
    
    soma_notas += nota
    quantidade_notas += 1

# Calcula e exibe a média das notas válidas
if quantidade_notas > 0:
    media = soma_notas / quantidade_notas
    print(f"A média das notas válidas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi digitada.")
