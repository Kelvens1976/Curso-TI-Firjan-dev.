quantidade = 0
total = 0

def media_precos(total,quantidade):
    if quantidade > 0:
        return total/quantidade 

    def funcao_principal():
        quantidade = 0
        total = 0

        preco = float(input("Entre com o preço do produto"))    
        
        while preco != 0:
            quantidade = quantidade + 1
            total = total + preco

            preco = float(input("Entre com o preço do produto"))

        media = media_precos(total,quantidade)

        print("Quantidade de Produtos", quantidade)
        print("O valor total é: ", total )
        print("O valor médio é: ", media)
    funcao_principal()
media_precos(total,quantidade)
