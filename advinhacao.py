
import random
    
#O def declara uma função no meu módulo. QUe pode ter varias funções.
def jogar():
    
    print ("###################################")
    print ("# Bem vindo ao Jogo de advinhação #")
    print ("###################################")

    numero_da_sorte = random.randrange(1,101)

    print("\nQual o nivel de dificuldade?")
    print("\n(1) {0} (2) {1} (3) {2}\n" .format("fácil", "médio", "difícil"))
    dificuldade = int(input("Escolha um niveis acima: "))
    tentativas = 3
    rodada = 1
    pontos = 1000

    if (dificuldade == 1):
        tentativas = 20
    elif (dificuldade == 2):
        tentativas = 10
    elif (dificuldade == 3):
        tentativas = 5
    else:
        print("Não escolheu nenhuma das opções, tenta de novo.")
        
        
    for rodada in range (1, tentativas + 1): 
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite numeros entre 1 e 100: "))
        print ("\nSeu numero da sorte é =", chute)      
        
        if(chute < 1 or chute > 100):
            print("\nDigite numeros entre 1 e 100\n")
            #O continue serve para o codigo continuar, para não sair do laço de repetição.
            continue
        
        #Resumindo o IF
        acertou = numero_da_sorte == chute
        maior = chute > numero_da_sorte
        menor = chute < numero_da_sorte

    
        if(acertou):
            print ("Você acertou, é o bichão mesmo. Fez", pontos, "pontos\n")
            #O break finaliza, mesmo que ainda tenha chances.
            break
        else:
            if(maior):
                print ("Ta foda em man, errou, o valor foi maior que o numero da sorte!")
                if (rodada == tentativas):
                    print("\nO número secreto era {0}. Você fez {1}\n".format(numero_da_sorte, pontos))
            elif(menor):
                print("Errou, o valor foi menor que o numero da sorte!")
                if (rodada == tentativas):
                    print("\nO número secreto era {0}. Você fez {1} pontos\n".format(numero_da_sorte, pontos))
        
        #Calculando os pontos
            pontos_perdidos = abs(numero_da_sorte - chute)        
            pontos = pontos - pontos_perdidos
        
    print ("fim do jogo")

if(__name__ == "__main__"):
    jogar()    
    
