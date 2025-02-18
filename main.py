from time import sleep
from os import system
from random import randrange
system('cls')

wordList = ['abaco', 'acaro', 'achar', 'adobe', 'aereo', 'agora', 'album', 'algum', 'altar', 'amado', 'andar', 
'antes', 'aquilo', 'ardor', 'aroma', 'artes', 'asilo', 'astro', 'atomo', 'aviao', 'aviso', 'bacia', 
'banco', 'beber', 'beijo', 'bicho', 'bordo', 'caber', 'caixa', 'canal', 'carro', 'casal', 'casar', 
'ciclo', 'claro', 'clave', 'coisa', 'comer', 'copia', 'corpo', 'corte', 'curar', 'danca', 'dedos', 
'dessa', 'dever', 'doido', 'dueto', 'ecoar', 'efeito', 'elite', 'enfim', 'falta', 'fases', 'feliz', 
'festa', 'folha', 'frase', 'freio', 'fruta', 'gente', 'grupo', 'homem', 'idoso', 'inicio', 'lento', 
'letra', 'livro', 'lugar', 'magma', 'marco', 'marte', 'medir', 'menos', 'metas', 'moeda', 'mundo', 
'musica', 'nariz', 'nobre', 'obras', 'onde', 'onibus', 'pausa', 'pedra', 'poder', 'presa', 'quase', 
'roupa', 'salvo', 'servo', 'sobre', 'terra', 'tocar', 'unica', 'vapor', 'verao', 'verde'
]

word = wordList[randrange(0, len(wordList))]
attempts = 6

print('''
.______   ____    ____ .______       _______   __       _______ 
|   _  \  \   \  /   / |   _  \     |       \ |  |     |   ____|
|  |_)  |  \   \/   /  |  |_)  |    |  .--.  ||  |     |  |__   
|   ___/    \_    _/   |      /     |  |  |  ||  |     |   __|  
|  |          |  |     |  |\  \----.|  '--'  ||  `----.|  |____ 
| _|          |__|     | _| `._____||_______/ |_______||_______|
''')

for _ in range(len(word)):
    print('[ ] ',end='')

while attempts > 0:
    splitedWord = [word[i].upper() for i in range(len(word))]
    hits = 0
    prompt = str(input('\n>>> '))

    while len(prompt) < len(word):
        prompt = str(input('\n>>> '))
    
    splitedPrompt = [prompt[i].upper() for i in range(len(prompt))]

    for i in range(len(splitedWord)):
        if splitedWord[i] == splitedPrompt[i]:
            print(f'[\033[32m{splitedPrompt[i]}\033[m]', end=' ')
            hits += 1
        elif splitedPrompt[i] != splitedWord[i] and splitedPrompt[i] in splitedWord:
            print(f'[\033[33m{splitedPrompt[i]}\033[m]', end=' ')
        else:
            print(f'[\033[m{splitedPrompt[i]}\033[m]', end=' ')

    attempts -= 1

    # Winning the game
    if hits == len(word):
        sleep(1)
        system('cls')
        print("\n:tada: Congratulations!! :tada:")
        break

# Loosing the game
if attempts == 0:
    sleep(1)
    system('cls')
    sleep(1)
    print('Você', end = ' ')
    sleep(1)
    print('\033[31mperdeu\033[m', end = ' ')
    sleep(1)
    print(':c')
    sleep(1)
    print(f'A palavra era: {word}')