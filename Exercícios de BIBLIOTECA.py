#Exercícios de BIBLIOTECA

import os
import time 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

livros_dispoiveis = 50
livros_emprestados = 0

escolha = 10

while escolha != 0:
    print("===========================================")
    print(" S I S T E M A   D E   B I B L I O T E C A")
    print("===========================================")
    print("1 - Emprestar Livros")
    print("2 - Devolver Livros")
    print("3 - Consultar Estoque")
    print("0 - Sair do Sistema de Biblioteca")

    escolha = int(input("Entre com uma opção: "))

    if escolha == 1:
        if livros_dispoiveis > 0:
            livros_dispoiveis = livros_dispoiveis - 1
            livros_emprestados = livros_emprestados + 1

            print("Emprestimo realizado com sucesso!")
        else:
            print("Falta de livros na Biblioteca")

    elif escolha == 2:
        if livros_emprestados > 0:
            livros_dispoiveis = livros_dispoiveis + 1
            livros_emprestados = livros_emprestados - 1 

            print("Livros devolvidos com sucesso!")
        else:
            print("Não há livros emprestados para devolução")
    
    elif escolha == 3:
        print(f"Livros disponiveis na Biblioteca: {livros_dispoiveis}")
        print(f"Livros emprestados na Biblioteca: {livros_emprestados}")
    
    elif escolha == 0:
        print("Sistema Finalizado com sucesso!")

    else:
        print("Opção incorreta inserida pelo usuário...")




