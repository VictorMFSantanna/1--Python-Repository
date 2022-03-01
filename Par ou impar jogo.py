from random import randint
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    pc = randint(0 , 10)
    r = jogador + pc 
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Total foi {r} ', end = '' )
    print('É par' if r %2 == 0  else 'É Impar')
    if tipo == 'P':
        if r % 2 == 0:
            print('Você venceu! ')
            v += 1
        else:
            print("Você perdeu!")
            break
    elif tipo == 'I':
        if r % 2 == 1:
            print('Você venceu! ')
            v += 1
        else:
            print("Você perdeu!")
            break
    print('Vamos jogar novamente... ')
print(f'Acabou o game! Voce venceu {v} vezes.')