import math
n = int(input())
f = math.factorial(n)
print(f) 
n = int(input())
f = 1
while n > 1:
    f = f * n
    n = n - 1
print(f)
n = int(input())
f = 1
for i in range(2, n + 1):
    f = f * i
print(f)

Фибоначи каждое четное число

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(4))

import random

seq = ['a', 8]
x = random.choice(seq)
print(type(seq))


# функция фозвращает четные числа фибоначи
def fib(n):
    roster = []
    fib1 = fib2 = 1
    while len(roster) < n - 1:
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 % 2 == 0:
            roster.append(fib2)
        if len(roster) < n:
            continue
        if len(roster) == n:
            break
        return roster
    print(0, *roster)

fib(12)