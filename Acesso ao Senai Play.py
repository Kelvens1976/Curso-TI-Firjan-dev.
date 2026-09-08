import os
import time

def limpar_tela():
    os.system ('cls' if os.name == 'nt' else 'clear')

    limpar_tela()
    time.sleep (0.1)

print("================================")
print("=== ACESSO AO SENAI PLAY ===")
print("================================")

navegador = input("Digite seu navegador de preferência: ")

print("Você escolheu:", navegador)

print("1 - INSCREVA-SE")
print("2 - LOGIN")

opcao = int(input("Escolha uma opção: "))


if opcao == 1:

    print("============================")
    print("=== FAÇA SEU CADASTRO ===")
    print("============================")

    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    print("CADASTRO FEITO!")

    email_login = input("Digite seu e-mail: ")
    senha_login = input("Digite sua senha: ")

    if email_login == email and senha_login == senha:
        print("DADOS CORRETOS - ACESSO AUTORIZADO")
    else:
        print("E-mail ou senha incorretos.")


elif opcao == 2:

    print("=== LOGIN ===")

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    print("DADOS CORRETOS - ACESSO AUTORIZADO")


else:

    print("Opção inválida.")


print("1 - SENAI PLAY")
print("2 - SENAI RJ")

plataforma = int(input("Escolha uma plataforma: "))


if plataforma == 1:

    print("CURSO NÃO ESTÁ DISPONÍVEL NESSA PLATAFORMA.")
    print("FIM")


elif plataforma == 2:

    print("=== SENAI RJ ===")

    curso = input("Pesquise o curso desejado: ")

    print("CURSO ENCONTRADO:", curso)

    print("IR PARA O CURSO")

    print("FIM")


else:

    print("Plataforma inválida.")    