import os
import time 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

def media_precos():
    if quantidade > 0:
        return total/quantidade 

quantidade = 0
total = 0
preco = float(input("Entre com o preço do produto"))

while preco != 0:
 quantidade = quantidade + 1
 total = total + preco

 preco = float(input("Entre com o preço do produto"))

media = media_precos()

print("Quantidade de Produtos", quantidade)
print("O valor total é: ", total )
print("O valor médio é: ", media)

