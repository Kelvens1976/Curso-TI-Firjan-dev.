import os
import time 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela() #essa sequencia acima é para deixar a tela mais limpa

veiculos = 0
total_litros = 0
total_arrecadado = 0
mais_40 = 0 #Todos os esses dados partirão do zero para iniciar o que se pede, contagem sempre do zero.

litros = float(input("Digite a quantidade de litros abastecidos (0 para encerrar): ")) #Float usado para ser numero real (decimal)
#o 0 é para encerrar como final da entrada de dados no relatório

while litros != 0: #Se litro diferente de 0 => Verdadeiro e continue, se diferente Falso e encerra

    preco = float(input("Digite o preço do litro: ")) #vai aparecer a mensagem Digite o preço do litro

    valor = litros * preco #Valor gasto = litro x preço

    print("Valor pago pelo cliente: R$", valor) #Vai preeencher automaticamente o valor dado na multiplicação 

    #Agora abaixo é a condição para que se coloque mais de 1 veículo

    veiculos = veiculos + 1 #aqui abre-se a contagem de veículos
    total_litros = total_litros + litros
    total_arrecadado = total_arrecadado + valor

    if litros > 40: 
        mais_40 = mais_40 + 1

    litros = float(input("Digite a quantidade de litros abastecidos (0 para encerrar): "))


if veiculos > 0: #Comando para que se for maior que 0 haja o calculo da media de litros
    media = total_litros / veiculos
else:
    media = 0

print("===============================") 
print("R E L A T Ó R I O  D O  D I A")
print("===============================") 
print("Veículos atendidos:", veiculos) #Vai extrair dados do somátorio da quantidade de veículos
print("Total de litros vendidos:", total_litros) #Vai extrair dados do somátorio da quantidade total de litros
print("Total arrecadado: R$", total_arrecadado) #Vai extrair dados do somátorio do total de dinheiro arrecadado
print("Média de litros por veículo:", media) #Calcula a quantidade de litros abastecido no dia dividido pela quantidade de veículos
print("Veículos que abasteceram mais de 40 litros:", mais_40) #Aqui ele computa somente a quantidade de veículos que passaram de 40 litros