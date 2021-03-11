from random import seed
from random import randint

numero = str(randint(0,10))
chute = None
tentativas = 0

print('Adivinhe o número de 0 a 10')

while chute != numero:
    chute = input('Qual seu chute? ')
    if chute != numero:
        print('Você errou! Tente novamente e mudamos o número :)')
        numero = str(randint(0,10))
        tentativas = tentativas + 1
else:
    print('Você acertou depois de ' + str(tentativas) + ' tentativas!')   
