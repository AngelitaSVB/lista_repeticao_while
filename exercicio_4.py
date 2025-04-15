# Peça ao usuário para digitar uma senha> Enquanto a senha for diferente de "1234", repita a solicitação. Quando a senha correta for digitada, exiba a mensagem "Acesso permitido"

# Solicita a senha ao usuário
senha = input("Digite a senha: ")

# Enquanto a senha for diferente de "1234", continua pedindo
while senha != "1234":
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

# Quando a senha estiver correta
print("Acesso permitido")

