import random
from time import sleep


def jogar():
    print('-------------------------------')
    print("Bem vindo ao jogo de advinhação")
    print('-------------------------------')
    print('Seu objetivo é chutar numeros até acertar o numero gerado ')

    numero_secreto = random.randrange(1, 101)

    pontos = 1000

    # Seleção de dificuldade
    k = 0
    while k == 0:

        print('Selecione a dificuldade')
        print('0-Test\n1-Very Easy\n2-Easy\n3-Medium\n4-Hard\n5-Very Hard\n6-Impossible')
        dificuldade = int(input('--->'))

        if dificuldade == 0:
            tentativas = 100
            k += 1

        elif dificuldade == 1:
            tentativas = 80
            k += 1

        elif dificuldade == 2:
            tentativas = 50
            k += 1

        elif dificuldade == 3:
            tentativas = 25
            k += 1

        elif dificuldade == 4:
            tentativas = 10
            k += 1

        elif dificuldade == 5:
            tentativas = 5
            k += 1

        elif dificuldade == 6:
            tentativas = 1
            k += 1

        else:
            print('Por favor digite uma dificuldade válida')
            sleep(2)

    # Chutes
    n = 1
    while tentativas >= n:

        print(f'Tentativa {n} de {tentativas}')
        numero = int(input("Digite um número entre 1 e 100: "))

        if numero <= 0 or numero > 100:
            print('Vocè deve digitar um numero entre 1 e 100')
            n += 1
            sleep(1)
            continue  # a função continue sai do bloco e começa dnv

        print('Você digitou', numero, end=' ')

        if numero_secreto == numero:
            print('e acertou', end=' ')
            print('Parabéns!!')
            break

        else:
            if numero > numero_secreto:
                print('e errou.')
                print('Tente um numero menor...\n')
                sleep(1)
                n += 1

            elif numero < numero_secreto:
                print('e errou.')
                print('Tente um numero maior...\n')
                sleep(1)
                n += 1
            pontos = pontos - (abs(numero_secreto - numero))  # A função abs( ) faz o módulo

    print(f'O numero era {numero_secreto}')
    print('Voce fez ', pontos, ' pontos')


if __name__ == "__main__":
    jogar()
