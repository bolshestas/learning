# a = int(input())
# if a == 4:
#     print(1)
# elif a!=4:
#     print(a // 4 +1)

# a = int(input())
# # b = (a + 3) // 4
# print((a + 3) // 4)
# Трехзначное число!
# num = 754
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
# print(a)
# print(b)
# print(c)

# a = int(input())
# h = a // 60
# m = a % 60

# print(a, 'мин - это', h, 'час', m, 'минут.')

# a = int(input())
# s = (a // 100) + ((a % 100) // 10) + ((a % 100) % 10)
# p = (a // 100) * ((a % 100) // 10) * ((a % 100) % 10)
# print('Сумма цифр =', s)
# print('Произведение цифр =', p)

# n = int(input())
# a = n // 100
# b = (n % 100) // 10
# c = (n % 100) % 10
# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')

# n = int(input())
# t = n // 1000
# s = n % 1000 // 100
# d = (n % 100) // 10
# e = (n % 100) % 10
# print('Цифра в позиции тысяч равна', t)
# print('Цифра в позиции сотен равна', s)
# print('Цифра в позиции десятков равна', d)
# print('Цифра в позиции единиц равна', e)

# a = '*'
# print(17 * a)
# print(a, a, sep='               ')
# print(a, a, sep='               ')
# print(17 * a)

# a = int(input())
# b = int(input())
# qs = (a + b) ** 2
# sq = (a ** 2) + (b ** 2)
# print('Квадрат суммы', a, 'и', b, 'равен', qs)
# print('Сумма квадратов', a, 'и', b, 'равна', sq)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print((a ** b) + (c ** d))

# n = int(input())
# b = int(str(n) * 2)
# c = int(str(n) * 3)
# print(n + b + c)

# password = input()
# password2 = input()
# if password == password2:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# n = int(input())
# t = n // 1000
# s = n % 1000 // 100
# d = (n % 100) // 10
# e = (n % 100) % 10
# p = t + e
# r = s - d
# if p == r:
#     print('ДА')
# else:
#     print('НЕТ')

# n = int(input())
# if n >= 18:
#     print('Доступ запрещен')
# else:
#     print('Доступ запрещен')

# a = int(input())
# b = int(input())
# c = int(input())
# if c == (b - a) + b:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# min = a
# if min > b:
#     min = b
# if min > c:
#     min = c
# if min > d:
#     min = d
# print(min)

# a = int(input())
# if a <= 13:
#     print('детство')
# elif 14 <= a <= 24:
#     print('молодость')
# elif 25 <= a <= 59:
#     print('зрелость')
# elif a >= 60:
#     print('старость')

# a = int(input())
# b = int(input())
# c = int(input())
# pol = 0
# if a > 0:
#     pol = a
# if b > 0:
#     pol += b
# if c > 0:
#     pol += c
# print(pol)

# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num2, 'выиграло')

# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = 1
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)

# x = int(input())
# if -1 < x and x <= 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# x = int(input())
# if x <= -3 or x >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# x = int(input())
# if -30 < x <= -2 or 7 < x <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# x = int(input())
# if x // 1000 and (x % 7 == 0 or x % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())

# if a < b + c and b < c + a and c < a + b:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
#     print('YES')
# else:
#     print('NO')
#Задача про шахматы номер 1!
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())

# if x1 == x2 or y1 == y2:
#     print('YES')

# else:
#     print('NO')

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# y0 = 5
# x0 = 5
# if x1 >= 4 and x1 <= 6 and x2 >=4 and x2 <=6 and y1 >= 4 and y1 <=6 and y2 >=4 and y2 <=6:
#     print('YES')
# else:
#     print('NO')

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# k = int(input())
# if n > k:
#     print('NO')
# elif n < k:
#     print('YES')
# else:
#     print("Don't know")

# a, b, c = int(input()), int(input()), int(input())
# if a == b:
#     if b == c:
#         print('Равносторонний')
#     else:
#         print('Равнобедренный')
# else:
#     if a == c:
#         print('Равнобедренный')
#     else:
#         if b == c:
#             print('Равнобедренный')
#         else:
#             print('Разносторонний')

# a, b, c = int(input()), int(input()), int(input())
# if a > b and a < c:
#     print(a)
# elif a < b and a > c:
#     print(a)
# elif b > a and b <c:
#     print(b)
# elif b < a and b > c:
#     print(b)
# elif c > a and c < b:
#     print(c)
# elif c < a and c > b:
#     print(c)

# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print('31')
# elif a == 2:
#     print('28')
# else:
#     print('30')

# grade = int(input())

# if 64 <= grade < 69:
#     print('Полусредний вес')
# else:
#     if 60 <= grade < 64:
#         print('Первый полусредний вес')
#     else:
#         if grade < 60: 
#             print('Легкий вес')

# a, b, c = int(input()), int(input()), input()
# if c == '+' or c == '-' or c == '*' or c == '/':
#     if c == '+':
#         print(a + b)
#     elif c == '-':
#         print(a - b)
#     elif c == '*':
#         print(a * b)
#     elif c == '/':
#         if b == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(a / b)
# else:
#     print('Неверная операция')

# a, b = input(), input()
# if (a == 'красный' or a == 'синий' or a == 'желтый') and (b == 'красный' or b == 'синий' or b == 'желтый'):
#     if a == 'красный' and b == 'красный':
#         print('красный')
#     elif a == 'красный' and b == 'синий':
#         print('фиолетовый')
#     elif a == 'красный' and b == 'желтый':
#         print('оранжевый')
#     elif a == 'синий' and b == 'желтый':
#         print('зеленый')
#     elif b == 'красный' and a == 'красный':
#         print('красный')
#     elif b == 'красный' and a == 'синий':
#         print('фиолетовый')
#     elif b == 'красный' and a == 'желтый':
#         print('оранжевый')
#     elif b == 'синий' and a == 'желтый':
#         print('зеленый')
#     elif a == 'желтый' and b == 'желтый':
#         print('желтый')
#     elif a == 'синий' and b == 'синий':
#         print('синий')
# else:
#     print('Ошибка цвета')

# n = int(input())

# if 0 <= n <= 36:
#     if n == 0:
#         print('зеленый')
#     elif 1 <= n <= 10 and n % 2 > 0:
#         print('красный')
#     elif 1 <= n <= 10 and n % 2 == 0:
#         print('черный')
#     elif 11 <= n <= 18 and n % 2 == 0:
#         print('красный')
#     elif 11 <= n <= 18 and n % 2 > 0:
#         print('черный')
#     elif 19 <= n <= 28 and n % 2 > 0:
#         print('красный')
#     elif 19 <= n <= 28 and n % 2 == 0:
#         print('черный')
#     elif 29 <= n <=36 and n % 2 > 0:
#         print('черный')
#     elif 29 <= n <= 36 and n % 2 == 0:
#         print('красный')
# else:
#     print('ошибка ввода')

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())

# # a1 < b1 and a2 < b2

# if a2 < a1 and b1 < b2:
#     print(a1, b1)

# n = int(input())
# d = n % 100
# e = d % 10
# if d == 0 and e == 0:
#     print('YES')
# else:
#     print('NO')

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if (x1 + x2 + y1 + y2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# m = input()

# if 10 <= a <= 15 and m == 'f':
#     print('YES')
# else:
#     print('NO')

# n = int(input())

# if 1 <= n <= 10:
#     if n == 1:
#         print('I')
#     elif n == 2:
#         print('II')
#     elif n == 3:
#         print('III')
#     elif n == 4:
#         print('IV')
#     elif n == 5:
#         print('V')
#     elif n == 6:
#         print('VI')
#     elif n == 7:
#         print('VII')
#     elif n == 8:
#         print('VIII')
#     elif n == 9:
#         print('IX')
#     elif n == 10:
#         print('X')
# else:
#     print('ошибка')  

# n = int(input())

# if n % 2 == 0:
#     if 2 <= n <= 5:
#         print('NO')
#     elif 6 <= n <= 20:
#         print('YES')
#     elif n > 20:
#         print('NO')
# else:
#     print('YES')

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# n = x1 - x2
# b = y1 - y2

# if (n == 2 and b == 1) or (n == 1 and b == 2):
#     print('YES')
# else:
#     print('NO')

# n = input()
# f = input()
# print('Hello' + ' ' + n + ' ' + f + '!' + ' ' +'You just delved into Python')

# c1 = input()
# c2 = input()
# c3 = input()

# a = len(c1)
# b = len(c2)
# c = len(c3)

# if a > b and a > c and b < c:
#     print(c2)
#     print(c1)
# elif a > b and a > c and c < b:
#     print(c3)
#     print(c1)
# elif b > a and b > c and a < c:
#     print(c1)
#     print(c2)
# elif b > a and b > c and c < a:
#     print(c3)
#     print(c2)
# elif c > a and c > b and b < a:
#     print(c2)
#     print(c3)
# elif c > a and c > b and a < b:
#     print(c1)
#     print(c3) 

# a = len(input())
# b = len(input())
# c = len(input())
# if (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c) == 0:
#     print('YES')
# else:
#     print('NO')

# n = input()
# s = '@'
# b = '.'
# if s in n and b in n:
#     print('YES')
# else:
#     print('NO')

# a = float(input())
# b = float(input())

# print(0.5 * a * b)

# s = float(input())
# v1 = float(input())
# v2 = float(input())

# print(s/(v1 + v2))

# n = float(input())

# if n != 0:
#     print(n ** -1)
# else:
#     print('Обратного числа не существует')

# f = float(input())
# print(0.5555555555555556(f - 32))

# y = float(input())

# if y >= 2:
#     x = y - 2
#     print(2 * 10.5 + x * 4)
# elif y < 2:
#     print(y * 10.5)

# n = float(input())
# print(int(n / 0.1 % 10))

# a = int(input())
# b = int(input())
# c = int(input())
# e = int(input())
# d = int(input())
# print('Наименьшее число =', min(a, b, c, e, d))
# print('Наибольшее число =', max(a, b, c, e, d))

# nums = [int(input()) for _ in range(5)]
# print(f'Наименьшее число = {min(nums)}', f'Наибольшее число = {max(nums)}', sep='\n')

# a = int(input())
# b = int(input())
# c = int(input())
# max_max = max(a, b, c)
# min_min = min(a, b, c)
# print(max_max)
# print((a + b + c) - (min_min + max_max))
# print(min_min)

# n = int(input())
# e = n % 10
# d = (n % 100) // 10
# s = n // 100

# if max(e, d, s) - min(e, d, s) == (e + d + s) - (max(e, d, s) + min(e, d, s)):
#     print('Число интересное')
# else:
#     print('Нет')

# a = abs(float(input()))
# b = abs(float(input()))
# c = abs(float(input()))
# e = abs(float(input()))
# d = abs(float(input()))
# print(a + b + c + e + d)

# p1 = int(input())
# p2 = int(input())
# q1 = int(input())
# q2 = int(input())

# print(abs(p1 - q1) + abs(p2 - q2))


# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())

# print(math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2)))

# r = float(input())
# print((math.pi * math.pow(r, 2)), (2 * math.pi * r), sep='\n')

# a = float(input())
# b = float(input())
# print(((a + b) / 2), (math.sqrt(a * b)), sep='\n')
# print(((2 * a * b)/(a + b)), (math.sqrt((a ** 2 + b ** 2) / 2)), sep='\n')


# r = (float(input()) * math.pi) / 180
# print(math.sin(r) + math.cos(r) + pow(math.tan(r), 2))

# x = float(input())
# print(math.ceil(x) + math.floor(x))

# a = float(input())
# b = float(input())
# c = float(input())
# # ax ** 2 + bx + c = 0
# d = math.pow(b, 2) - 4 * a * c
# if d == 0:
#     print((-1 * b) / (2 * a))
# elif d < 0:
#     print('Корней нет')
# else:
#     x1 = ((-1 * b) + math.sqrt(d)) / 2 * a
#     x2 = ((-1 * b) - math.sqrt(d)) / 2 * a
#     x3 = min(x1, x2)
#     x4 = max(x1, x2)
#     x5 = min(x3, x4)
#     x6 = max(x3, x4)
#     print(x5, x6, sep='\n')

# n = int(input())
# a = float(input())

# print((n * math.pow(a, 2)) / (4 * math.tan(math.pi / n)))

# for i in range(10):
#     print('Python is awesome!')

# a = input()
# n = int(input())
# for i in range(n):
#     print(a)

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')


# n = int(input())
# s = '*' * 19
# for i in range(n):
#     print(s)


# s = input()
# for _ in range(10):
#     print(_, s)


# n = int(input())
# for i in range(n + 1):
#     print('Квадрат числа', i, 'равен', i * i)


# n = int(input())
# for i in range(n):
#     print((n - i) * '*')

# m = int(input())
# p = int(input())
# n = int(input())

# for i in range(n):
#     print(i + 1, m)
#     m = m + m * p / 100


# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     print(i)


# m = int(input())
# n = int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)


# m = int(input())
# n = int(input())

# if m % 2 != 0:
#     for i in range(m, n - 1, -2):
#         print(i)
# else:
#     for i in range(m - 1, n - 1, -2):
#         print(i)


# m = int(input())
# n = int(input())

# r = m % 2 - 1

# for i in range((m -+ r), n - 1, -2):
#     print(i)


# m = int(input())
# n = int(input())

# if (m % 17 == 0 and n % 17 == 0) or (m % 10 == 9 or n % 10 == 9) or ((m % 3 == 0 and n % 3 == 0) or (m % 5 == 0 and n % 5 == 0)):
#     for i in range(m, n, -1):
#         print(i)
# else:
#     print('ХУй')


# if i % 3 + i % 5 == 0:
#     for i in range(m, n + 1):
#         print(i)


# n = int(input())

# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)


# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')


# a = int(input()) 
# b = int(input())

# counter = 0

# for i in range(a, b + 1):
#     if i % 10 == 4 or i % 10 == 9:

#         counter += 1

# print(counter) 


# n = int(input())

# total = 0
# for i in range(1, n + 1):
#     numbers = int(input())
#     total += numbers
# print(total)


from math import *
from typing import Collection


# n = int(input())

# total = 0
# summary = 0

# for i in range(1, n + 1):
    
#     total = total + (1 / (i + 1))
    
#     summary = total + 1 - log(n)
    
# print(summary)

# n=int(input())
# print(sum(1/(i+1)for i in range(n))-log(n))


# n = int(input()) 

# counter = 0

# for i in range(1, n + 1):
#     if pow(i, 2) % 10 == 2:
#         counter += i
#     elif pow(i, 2) % 10 == 5:
#         counter += i
#     elif pow(i, 2) % 10 == 8:
#         counter += i
# print(counter) 


# n = int(input())
# fact = 1
# for i in range(2, n + 1):
#     fact = fact * i
# print(fact)

# counter = 1

# for i in range(10):

#     n = int(input())

#     if n != 0:

#         counter *= n

# print(counter) 


# n = int(input())

# total = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total) 


# n = int(input())

# total = 0
# for i in range(n + 1):
#     total += pow(-1 , i + 1) * i
# print(int(total))

# n = int(input())
# largest = 0
# prelargest = 0
# for i in range(n):
#     numbers = int(input())
#     if numbers > largest:
#         prelargest = largest
#         largest = numbers
#     elif prelargest < numbers < largest:
#         prelargest = numbers
# print(largest, prelargest, sep='\n')


# for i in range(11):
#     n = int(input())
#     flag = False

#     if n % 2 == 0:
#         flag = True
#         print('YES')

#     else:
#         flag = False
#         print('NO')


# for i in range(11):
#     num = int(input())
#     if num % 2 == 0: 
#         flag = True
#     else:
#         flag == False


# if flag == True:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# a = 1
# y = 0
# for i in range(1, n + 1):
#     b = a
#     a = b + y
#     y = b
#     print(b, end=' ')


# n = input()
# while n != :
#     print(n)
#     n = input()


# n = input()
# while n != 'КОНЕЦ' and n != 'конец':
#     print(n)
#     n = input()

# text_sum = 0
# n = input()
# while n != 'стоп' and n != 'хватит' and n != 'достаточно':
#     text_sum += 1
#     n = input()
# print(text_sum)


# text_sum = 0
# n = input()
# ost = n % 7
# while n % 7 == 0:
#     text_sum += n
#     n = input()
#     print(text_sum)


# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print(total)


# n = int(input())
# total = 0
# while n < 6  and n > 0:
#     if n == 5:
#         total += 1
#     n = int(input())

# print(total)

# price = int(input())
# n1 = 1
# n2 = 5
# n3 = 10
# n4 = 25
# total = 0
# while n >= 25:
#     n -= 25
#     total += 1
# while n >= 10:
#     n -= 10
#     total += 1
# while n >= 5:
#     n -=5
#     total += 1
# while n >= 1:
#     n -= 1
#     total += 1

# print(total)
                

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)


# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)


# n = int(input())
# total = 0
# while n != 0:
#     total = n % 10
#     n = n // 10
#     print(total)


# n = 12345
# total = 0
# last_digit = 0

# while n != 0:
#     last_digit = n % 10
#     total += last_digit
#     n = n // 10

# print(total)

# n = int(input())
# total = 0

# while n != 0:
#     total = n % 10
#     n = n // 10

#     print(total, end='')


# n = int(input())
# biggest = 0
# smallest = 9
# total = n % 10

# while n != 0:
#     if total < smallest:
#         smallest = total
#     elif total > biggest:
#         biggest = total

#     n //= 10
#     total = n % 10

# print(biggest, smallest, sep='\n')


# n = int(input())

# total = 0
# quantity = 0
# composition = 1
# last_digit = n % 10


# while n != 0:
#     total += n % 10    # Нахождение суммы
#     quantity += 1          # Колличество
#     composition *= (n % 10)    #Произведение
#     ar_mean = total / quantity    # Среднее арифметическое
#     first_digit = n % 10    # Первая цифра
#     total_f_l = last_digit + first_digit    # Сумма первой и последней цифры
#     n = n // 10            # Постоянное уменьшение колличества цифр на одну

# print(total, quantity, composition, ar_mean,first_digit, total_f_l, sep='\n')


# n = int(input())
# total = 0

# while n > 9:
#     total = n % 10
#     n = n // 10
# print(total)


# n = int(input())
# last_number = n % 10
# total = 0

# while n > 0:
#     if n % 10 > last_number:
#         total += 1
#     if n % 10 < last_number:
#         total += 1
#     n = n // 10
        
# if total == 0:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# flag = True
# last_num = n % 10

# while n != 0:
#     last_digit = n % 10
#     if last_num > last_digit:
#         flag = False
#     else:
#         last_num <= last_digit
#         flag = True
#     n = n // 10

# if flag == False:
#     print('YES')
# elif flag == True:
#     print('NO')