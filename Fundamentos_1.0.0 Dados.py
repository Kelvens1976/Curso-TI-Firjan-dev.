import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear' )

limpar_tela()
time.sleep(0.1)

nome = input("Digite seu nome: ")          # Recebe o nome da pessoa e armazena na variável nome
idade = int(input("Digite sua idade: "))   # Recebe a idade, transforma em número inteiro e armazena em idade
cidade = input("Digite sua cidade: ")      # Recebe o nome da cidade e armazena na variável cidade

print("===============================") 
print("D A D O S   D A   P E S S O A")
print("===============================")  
print("Nome:", nome)                       # Apresenta o nome na tela
print("Idade:", idade)                     # Apresenta a idade na tela
print("Cidade:", cidade)                   # Apresenta a cidade na tela