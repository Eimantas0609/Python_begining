import numexpr
from colorama import init
from colorama import Fore
init()

print(Fore.CYAN)

expr = input('Mathematical expression  ')
result = numexpr.evaluate(expr)

print(Fore.GREEN)

print(f'Result: {result}')

input()