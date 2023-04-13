from colorama import init
from colorama import Fore, Back, Style
init()

# print(Back.CYAN)
print(Fore.BLUE)
# print(Style.DIM)

a = float(input('number 1: '))

print(Fore.CYAN)

operation = input('What do? (+, -, *, /): ')
result = 0

print(Fore.BLUE)
b = float(input('number 2: '))

print(Fore.RED)

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b

print(f'Result: {result}')
