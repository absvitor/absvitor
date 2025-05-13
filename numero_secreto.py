#importou a biblioteca random
import random
#Declarar variáveis
numero_secreto = random.randint(1,10)
tentativas =0
contagem_tentativas =0
numero=0
#introdução ao jogo
print ("Bem vindo ao jogo do Número secreto")
print ("Tente adivinhar o número secreto 1 e 10")
#Laço de repetição
while tentativas != numero_secreto:
    numero = int(input("Digiteum número: "))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print("Parabéns! Você adivinhou o número")
        print(f"Você precisou de {contagem_tentativas}")
        break
    elif numero < numero_secreto:
        print ("o numero secreto é maior. ")
    else:
        print("o numero secreto é menor. ")