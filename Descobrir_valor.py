# Joguinho pra descobrir o numero

from random import randint
random = randint(0, 100)
chute = 0
tentativa = 0

while chute != random:
    chute = input('Chute um número entre 0 a 100: ')
    tentativa += 1
    if chute.isnumeric():
        chute = int(chute)
        if chute == random:
            print('-----------------------------------')
            print('Parabéns, você venceu! O número era', random)
            break
        else:
            print('-----------------------------------')
            if chute > random:
                print('Você errou! Dica: É um número menor.')
            else:
                print('Você errou! Dica: É um número maior.')
            print('-----------------------------------')
print("Voce acertou em:",tentativa)
print('#### Fim do Jogo ####')