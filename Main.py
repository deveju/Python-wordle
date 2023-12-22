import random as rnd
from rich import print

tries = 6
attempts = set()

en_path = 'python_wordle/wordleWordsEN.txt'
pt_path = 'python_wordle/wordleWordsPT.txt'

print('\n[blue]"en" for english/usa[/] | [green]"pt" para português/br[/]')
choice = input('Choose the desired language | escolha a língua preferida: ')

def verification():
    while True:
        if(choice == 'pt'):
            typedWord = input('Digite uma palavra: ')
        else: 
            typedWord = input('Type a word: ')
        if len(typedWord) == 5:
            return typedWord.upper()
        else:
            if(choice == 'pt'):
                print('Digite uma [blue]palavra de 5 letras[/], por favor!')
            else:
                print('Type a [blue]5-character word[/], please!')

if(choice == 'pt'):
    with open('python_wordle/wordleWordsPT.txt', 'r') as file:
        words = {word.strip().upper() for word in file.readlines()}
    print('Língua: [green]PORTUGUÊS-BR[/]')
    print('Você terá [blue]6 tentativas[/] para acertar a palavra correta!')
    print('---------------------------------------------------------------')
    print('As palavras têm [blue]5 letras[/]!')
    print('[red]Vermelho[/]: a letra [red]não está[/] na palavra!')
    print('[yellow]Amarelo[/]: A letra [green]está na palavra[/], mas [yellow]está em outra posição[/]!')
    print('[green]Verde[/]: A letra [green]está na palavra[/], e [green]está na posição correta[/]!')
    print('---------------------------------------------------------------')
else:
    with open('python_wordle/wordleWordsEN.txt', 'r') as file:
        words = {word.strip().upper() for word in file.readlines()}
    print('Language: [blue]ENGLISH-USA[/]')
    print('You will have [blue]6 tries[/] to guess the correct word!')
    print('---------------------------------------------------------------')
    print('The words are [blue]5-character[/] long!')
    print('[red]Red[/]: The character [red]is not[/] in the word!')
    print('[yellow]Yellow[/][white]: The character [green]is in the word[/], but [yellow]in another position[/]!')
    print('[green]Green[/]: The character [green]is in the word[/], and [green]in its correct place[/]!')
    print('---------------------------------------------------------------')

ans = rnd.choice(list(words))
ansSplit = [*ans]


while tries > 0:
    typedWord = verification()

    if ans == typedWord:
        if(choice == 'pt'):
            print(f'[green]Você acertou![/] A resposta era [green]{ans}[/]!')
        else:
            print(f'[green]You correctly guessed it![/] The answer was [green]{ans}[/]!')
        break
    elif typedWord not in words:
        if(choice == 'pt'):
            print(f'[blue]{typedWord}[/]' + ' [red]não é[/] uma palavra válida!')
        else:
            print(f'[blue]{typedWord}[/]' + ' [red]is not[/] a valid word!')
    else:
        typedWordSplit = [*typedWord]
        output = []
        for i in range(5):
            if typedWordSplit[i] == ansSplit[i]:
                output.append('[green]' + typedWordSplit[i] + '[/]')
            elif typedWordSplit[i] in ans:
                output.append('[yellow]' + typedWordSplit[i] + '[/]')
            else:
                output.append('[red]' + typedWordSplit[i] + '[/]')
        tries -= 1

        attempts.add(' '.join(output))
        print('\n'.join(attempts))

    if tries == 0:
        if(choice == 'pt'):
            print(f'[red]Você está sem tentativas T_T.[/] A resposta correta era [green]{ans}[/].')
        else:
            print(f'[red]You ran out of tries T_T.[/] The correct answer was [green]{ans}[/].')
        break
