import random

print('--------------------------------')
print('***Bem vindo ao jogo de Forca***')
print('--------------------------------')

arquivo = open('../frutas.txt', 'r')

lista_de_frutas = []

for fruta in arquivo:
    fruta = fruta.strip('\n')
    fruta = fruta[5:]

    if fruta is not '':
        lista_de_frutas.append(fruta)

    else:
        pass

arquivo.close()

# seleção de fruta aleatória da lista
numero_de_frutas = len(lista_de_frutas)
posicao_fruta_secreta = random.randrange(0, numero_de_frutas)
fruta_secreta = lista_de_frutas[posicao_fruta_secreta]

palavra_secreta = fruta_secreta.upper()
acertou = False
enforcou = False
erros = 0

# criando a lista na qual os caracteres são armazenados

letras_acertadas = ['_' for letra in palavra_secreta]  # List Comprehension

'''          OU
numero_de_caracteres = (len(palavra_secreta)) + 1
list_str = "_ " * (len(palavra_secreta))
letras_acertadas = list_str.split()'''

'''          OU
for letra in palavra_secreta:
    letras_acertadas.append("_")'''


# loop do jogo
while not enforcou and not acertou:

    print(f'{erros} erros de 6')
    print(str(letras_acertadas))
    chute = input('\nQual o seu chute:  ')  # entrada
    chute = chute.strip().upper()  # strip() tira os espaços do inicio e do final

    index = 0

    # se a letra foi acertada duas vezes
    if chute in letras_acertadas:
        print('Atenção! Você já digitou esta letra')

    # tem o chute na palavra secreta
    elif chute in palavra_secreta:

        for letra in palavra_secreta:

            if chute == letra:
                print(f'Encontrei a letra {letra} na posição {index + 1}')
                letras_acertadas[index] = letra
                acertou = '_' not in letras_acertadas  # parar o loop
            index += 1

    # não tem o chute na palavra secerta
    else:
        erros += 1
        enforcou = erros == 6

if acertou is True:
    print(str(letras_acertadas))
    print('Parabéns você acertou!!!')

else:
    print('Você Perdeu')

print(palavra_secreta)
