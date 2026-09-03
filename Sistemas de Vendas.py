import os
import time 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

quantidade_vendas = 0
valor_total = 0
maior_venda = 0

codigo_produto = int(input("Entre com o código do produto, e zero para encerrar: "))

while codigo_produto != 0:
    quantidade = int(input("Entre com a quantidade: "))
    preco = float(input("Entre com o preço: "))

    valor_vendas = quantidade * preco
    
    quantidade_vendas = quantidade_vendas + 1
    valor_total =  valor_total + valor_vendas

    if valor_vendas > maior_venda:
        maior_venda = valor_vendas

        codigo_produto = int(input("Entre com o código do produto, e zero para encerrar: "))
    
print("=====================================================")
print("R  E  L  A  T  Ó  R  I  O    D  E    V  E  N  D  A  S")
print("=====================================================")
print("Quantidade de vendas realizadas: ", quantidade_vendas)
print("O valor de vendas total: ",valor_total)
print("A maior venda realizada é: ",maior_venda)

if valor_total >= 5000:
    print("Meta Alcançada!")
else:
    Faltam = 5000 - valor_total
    print("Meta diária não alcançada. Faltam: ", Faltam)




