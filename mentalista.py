#Jogo do mentalista
#Jogo contra a máquina no qual a máquina sorteia um número inteiro de 0 a 10, o usuário dá um palpite sobre qual é o número, se errar ganha uma dica e tem mais 2 chances para acertar

import random
maquina = random.randint(0,11)


escolha = input('A maquina escolheu um numero inteiro de 0 a 10. Digite seu palpite sobre qual foi esse numero\n')


#Verificando se o input é um número inteiro entre 0 e 10 e, caso não for, pedindo para tentar novamente
while type(escolha) != type(maquina) :
    try :
        escolha = int(escolha)
        if escolha < 0 or escolha > 10 :
            escolha = input('Por favor, escolha um numero entre 0 e 10\n')
    except :
        escolha = input('Por favor, escolha um numero inteiro\n')

#---------Função para verificar se o input é um número inteiro entre 0 e 10 nas tentativas posteriores
def inteiro(valor) :
    while type(valor) != type(maquina) :
        try :
            valor_int = int(valor)
            if valor_int < 0 or valor_int > 10 :
                valor = input('Escolha invalida. Por favor, tente novamente com um numero entre 0 e 10. Esta tentativa nao foi contada como erro.\n')
            else : return valor_int
        except :
            valor = input('Escolha invalida. Por favor, tente novamente com um numero inteiro entre 0 e 10. Esta tentativa nao foi contada como erro.\n')
#-------------------

tentativa = 1
while tentativa < 3 and escolha != maquina :
    if escolha < maquina :
        tentativa += 1
        print("O numero que voce escolheu eh menor que o escolhido pela maquina. ")
        escolha = input('Tente novamente! Qual eh o seu palpite?\n')
        escolha = inteiro(escolha)
    else : #se escolha > maquina
        tentativa += 1
        print("O numero que voce escolheu eh maior que o escolhido pela maquina. ")
        escolha = input('Tente novamente! Qual eh o seu palpite?\n')
        escolha = inteiro(escolha)

if escolha == maquina :
    print('Parabens! Voce acertou!')
else :
    print("Voce errou e atingiu o numero maximo de tentativas. O valor correto seria " + str(maquina) + ".")

print('Jogo finalizado')
