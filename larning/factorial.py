# import math
# n = int(input())
# f = math.factorial(n)
# print(f) 
# n = int(input())
# f = 1
# while n > 1:
#     f = f * n
#     n = n - 1
# print(f)
# n = int(input())
# f = 1
# for i in range(2, n + 1):
#     f = f * i
# print(f)

# Фибоначи каждое четное число

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(4))