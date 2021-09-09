from random import *

n = randrange(1, 101)
task = int(input('Угадай число:'))
if task == n:
    print('Ты угадал, это число:', n)
else:
    print('Не угадал')