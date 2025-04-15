# O programa escolhe um número secreto (fixo ou aleatório). O usuário tenta adivinhar. Enquanto ele errar, o programa pede outro palpite. Quando aceitar, o programa mostra quantos tentativas fotam feitas.

import random

# Escolhe um número secreto aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa a variável para contar as tentativas
tentativas = 0

# Enquanto o usuário não acertar, continua pedindo palpites
while True:
    palpite = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
    tentativas += 1  # Conta a tentativa
    
    if palpite < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
    elif palpite > numero_secreto:
        print("O número secreto é menor. Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas.")
        break  # Sai do loop quando acertar
