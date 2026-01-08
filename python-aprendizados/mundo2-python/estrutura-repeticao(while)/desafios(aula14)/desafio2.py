from random import randint

computador = randint(0, 10)
quantidade = 0
jogador = int(input('Digite um número de 0 a 10: '))

while jogador != computador:
    print('Tente novamente!')
    jogador = int(input('Digite um número de 0 a 10: '))
    
    quantidade += 1

print('Você acertou o meu número com um total de {} palpites, PARABÉNS!'.format(quantidade))
print('Fim de Jogo!!')