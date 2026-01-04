import secrets
import string

def gerar_senha(tamanho=18):

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    todos_caracteres = letras + numeros + simbolos

    senha = "".join(secrets.choice(todos_caracteres) for _ in range(tamanho))
    
    return senha

tamanho_usuario = int(input("Digite o comprimento da senha: "))
nova_senha = gerar_senha(tamanho_usuario)

print(f"Sua nova senha segura é: {nova_senha}")

input("\nPressione Enter para sair...")