from time import sleep
from os import system, name
from random import randrange

def clearTerminal():
    # Verifica o sistema operacional
    if name == 'nt':  # Windows
        system('cls')
    else:  # Linux e Mac
        system('clear')

wordList = ["abalo", "abano", "abare", "abeto", "abono", "adaga", "adega", "adiar", "adubo", "afeto", "agudo", "aguia", "alado", "algas", "aliar", "alpes", "altos", "amada", "ameno", "amplo", "aneis", "anexo", "animo", "anjos", "antes", "apelo", "avido", "aviso", "axila", "balao", "barco", "basco", "bicho", "boato", "bossa", "brejo", "brisa", "broto", "burro", "busca", "cabra", "cacto", "calmo", "campo", "carpa", "carte", "cerva", "chato", "choro", "claro", "clero", "cobra", "colar", "comer", "coroa", "creme", "curva", "danos", "dardo", "dedao", "denso", "deste", "dizei", "dorso", "drama", "ebano", "ecoar", "edite", "elmos", "epico", "ervas", "estar", "etico", "exato", "exijo", "exodo", "facil", "falta", "fardo", "fauna", "fibra", "folha", "forca", "forte", "fossa", "fraco", "frevo", "fundo", "gaita", "garra", "gemeo", "girar", "globo", "gotas", "graca", "grama", "guias", "havia", "heroi", "hinos", "horas", "humor", "idear", "igual", "indio", "inerte", "iscas", "jaleco", "jambe", "janta", "jarro", "jazer", "justo", "lamas", "lasso", "latim", "lapis", "laudo", "legal", "letal", "livro", "lombo", "longe", "lotes", "luvas", "macho", "magna", "manga", "massa", "meios", "mente", "menos", "milho", "mocho", "monte", "moral", "musgo", "navio", "neves", "nexus", "noite", "norma", "norte", "novas", "nuvem", "obrar", "oferta", "ogiva", "ondas", "opaco", "ordem", "otimo", "ouros", "ovulo", "pampa", "papel", "parco", "parte", "pedra", "piano", "piloto", "pinho", "pisco", "planos", "praia", "prato", "pulso", "punho", "quais", "quase", "quico", "rabos", "racao", "radio", "rapaz", "rapto", "rebol", "redor", "regua", "relva", "rente", "repor", "rimas", "ritmo", "rocha", "rodas", "rosca", "rotas", "safra", "saias", "salas", "salto", "samba", "sanha", "sapo", "segue", "selar", "senso", "servo", "sinais", "sinal", "sino", "solta", "suave", "super", "surto", "tacas", "tango", "tatua", "tebas", "temer", "tenaz", "tenor", "terra", "teses", "tigre", "toldo", "torpe", "torta", "traco", "trama", "trapo", "trigo", "troca", "truta", "turma", "urubu", "vacas", "vagal", "varas", "velha", "verbo", "verde", "verve", "vespa", "vigas", "vital", "viver", "volei", "xampu", "xango", "xerox", "xingo", "zinco", "zorra", "zumbi"]

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
        clearTerminal()
        print("\n:tada: Congratulations!! :tada:")
        break

# Loosing the game
if attempts == 0:
    print()
    sleep(1)
    clearTerminal()
    sleep(1)
    print('Você', end = ' ')
    sleep(1)
    print('\033[31mperdeu\033[m', end = ' ')
    sleep(1)
    print(':c')
    sleep(1)
    print(f'A palavra era: {word}')