# text no terminal

'''
> formato:
\33[style;text;background m escritura \33[m
. pode espaço? sim
. pode junto? sim

> style:
0 ou nada - nada
1 - negrito
4 - sublinhado
7 - invertido

> text (começam com 30)
aparentemente mudou, antes era 'wrygbpcg'
e agr tá 'grgympbw' ksks mas enfim

> background (começam com 40)
mesma coisa do text, mas pro background
'''
text = {
    '30': 'gray',
    '31': 'red',
    '32': 'green',
    '33': 'yellow',
    '34': 'blue',
    '35': 'pink',
    '36': 'cyan',
    '37': 'white'
}

# Ctrl + Shift + L = reescrever a mesma escritura
print(f'\033[1;7m invertido negrito \033[m')
print(f'\033[30m {text['30']} \033[m')
print(f'\033[31m {text['31']} \033[m')
print(f'\033[32m {text['32']} \033[m')
print(f'\033[33m {text['33']} \033[m')
print(f'\033[34m {text['34']} \033[m')
print(f'\033[35m {text['35']} \033[m')
print(f'\033[36m {text['36']} \033[m')
print(f'\033[37m {text['37']} \033[m')

