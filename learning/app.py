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


# n = int(input())

# for i in range(2, n + 1):
#     if n % i == 0:
#         break
# print(i)


# n = int(input())

# for i in range(1, n + 1):
#     if (i >= 5 and i <= 9) or (i >= 17 and i <= 37) or (i >= 78 and i <= 87):
#         continue
#     print(i)


# max_num = -1
# total = 0
# for i in range(1, 11):
#     x = int(input())
#     if x < 0:
#         total += x
#     if x >= max_num:
#         max_num = x
#     elif x > 0:
#         print('NO')

# print(max_num)
# print(total)

# x = int(input())
# max_num = -1
# total = 0
# if x < 0:
#     while x > 0:
#         if x < 0:
#             total += x
#         if x >= max_num:
#             max_num = x
#     print(max_num)
#     print(total)

# else:
#     print('NO')


# mx = -10**6 - 1
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x < 0 and x > mx:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')


# n = int(input())
# max_digit = -1

# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10

# if max_digit >= 0:
#     print(max_digit)
# else:
#     print('NO')


# n = int(input())
# big_num = 0

# while n > 0:
#     big_num = n % 10
#     n = n // 10

# print(big_num)


# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)


# n = int(input())

# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()


# n = int(input())

# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()


# n = int(input())

# for i in range(1, (n // 2 + 2)):
#     print('*' * i)
# for j in range(n // 2, 0, -1):
#     print('*' * j)

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()


#  28n + 30 k + 31 m = 365
# total = 0

# for n in range(1, 13):
#     for k in range(1, 13):
#         for m in range(1, 13):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print('Общее', total)

#  10b + 5k + 0.5t = 100
# total = 0
# for b in range(1, 101):
#     for k in range(1, 101):
#         for t in range(1, 101):
#             if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
#                 total += 1
#                 print('b =', b, 'k =', k, 't =', t)
# print('Общее', total)


from math import pow, factorial


# a5 + b5 + c5 + d5 = e5

# for a in range(1, 151):
#     for b in range(1, 151):
#         for c in range(1, 151):
#             for d in range(1, 151):
#                 for e in range(1, 151):
#                     if float(pow(a, 5) + pow(b, 5) + pow(c, 5) + pow(d, 5) == pow(e, 5)):
#                         print(float(a + b + c + d + e))

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for j in range(i - 1, 0, -1):
#         print(j, end='')
#     print()

# a = int(input())
# b = int(input())
# sum_digit = 0
# max_x = 0
# x = 0

# for i in range(a, b + 1):
#     for j in range(1, i + 2):
#         if i % j == 0:
#             max_x += j
#             if max_x > x or (max_x == x and i > sum_digit):
#                 sum_digit == i
#                 x == max_x
#     max_x == 0
# print(sum_digit, x)
                

# n = int(input())

# for i in range(1, n + 1):
#     total = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             total += 1
#     print(i, '+' * total, sep='')


# n = int(input())
# total = 0
# f = 1

# for i in range(1, n + 1):
#     for j in range(2, i + 1):
#         f *= i
#         total = total + f
# print(total)


# a = int(input())
# b = int(input())

# for i in range(a, b + 1):
#     tmp = [i % j == 0 for j in range(1, i, 1)]
#     if tmp.count(True) == 1:
#         print(i)


# n = int(input())
# s = 0

# while n != 0:
#     last = n % 10
#     if last % 2 == 0:
#         s += last
#     n //= 10
    
# print(s)


# n = int(input())

# print('*' * 19)
# for i in range(n - 2):
#     print('*                 *')

# print('*' * 19)


# n = int(input())

# while n > 99:
#     last = n % 10
#     n //= 10
# print(last)


# n = int(input())
# last = n % 10
# counter_3 = 0
# counter_last = 0
# digit_2 = 0
# sum_5 = 0
# set_7 = 1
# counter_0 = 0

# while n != 0:
#     if n % 10 == 3:
#         counter_3 += 1
#     if last == n % 10:
#         counter_last += 1
#     if (n % 10) % 2 == 0:
#         digit_2 += 1
#     if n % 10 > 5:
#         sum_5 += (n % 10)
#     if n % 10 > 7:
#         set_7 *= (n % 10)
#     if n % 10 == 0:
#         counter_0 += 1
#     if n % 10 == 5:
#         counter_0 += 1
#     n //= 10

# print(counter_3, counter_last, digit_2, sum_5, set_7, counter_0, sep='\n')


# total = 0
# for b in range(1, 101):
#     for k in range(1, 101):
#         for t in range(1, 101):
#             if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
#                 total += 1
#                 print('b =', b, 'k =', k, 't =', t)
# print('Общее', total)


# a = a3 + b3 = c3 + d3
# for a in range(1, 34):
#     for b in range(1, 34):
#         for c in range(1, 34):
#             for d in range(1, 34):
#                 if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3) and a != b and a != c and a != d and b != a and b != c and b != d and c != a and c != b and c != d and d != a and d != c and d != b:
#                     print(pow(a, 3) + pow(b, 3))
#                 print()

# text = input()

# for i in range(0, len(text), 2):
#     print(text[i])


# name = input()
# famile = input()
# faname = input()

# print(name[0], famile[0], faname[0], sep='')


# text = input()
# n = int(text)
# total = 0

# for i in range(3):
#     r = n % 10
#     total += r
#     n //= 10

# print(total)

# s = 'All you need is love'
# if 'love' in s:
#     print('❤️')
# else:
#     print('💔')

# text = input()

# for i in range(10):
#     if str(i) in text:
#         print('Цифра')
#         break

# else:
#     print('Цифр нет')


# text = input()
# plus = '+'
# star = '*'
# total_plus = 0
# total_star = 0

# for i in range(len(text)):
#     if plus in text[i]:
#         total_plus += 1
#     if star in text[i]:
#         total_star += 1

# print('Символ + встречается', total_plus, 'раз')
# print('Символ * встречается', total_star, 'раз')


# text = input()
# plus = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'A', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
# star = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',]
# total_plus = 0
# total_star = 0

# for i in range(len(text)):
#     if text[i] in plus:
#         total_plus += 1
#     if text[i] in star:
#         total_star += 1

# print('Количество гласных букв равно', total_plus)
# print('Количество согласных букв равно', total_star)


# n = int(input())
# ost = ''


# while n != 0:
#     r = n % 2
#     ost += str(r)
#     n //= 2
# for i in range(len(ost)):
#     int(ost)    
#     print(ost)


# s = input()

# if s[::-1] == s[:]:
#     print('YES')
# else:
#     print('NO')

# s = input()
# total = 0
# text = s

# while text != '':
#     text = text[:-1]
#     total += 1
# print(total, s * 3, s[:1], s[:3], s[-3:], s[::-1], s[1:-1], sep='\n')


# s = input()
# print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2], sep='\n')


# s = input()
# begin = s[:((len(s) + 1) // 2)]
# end = s[((len(s) + 1) // 2):]
# print(end + begin)


# s = input()
# FIO = s.title()

# if FIO == s:
#     print('YES')
# else:
#     print('NO')


# s = input()

# print(s.swapcase())


# s = input()
# text = s.lower()
# if 'хорош' in text:
#     print('YES')
# else:
#     print('NO')


# s = input()
# text = s.lower()
# total = 0

# for i in range(len(s)):
#     if s[i].islower() == True:
#         total += 1
# print(total)


# s = input()

# print(s.count(' ') + 1)


# s = input()
# s = s.lower()

# print('Аденин:', s.count('а'))
# print('Гуанин:', s.count('г'))
# print('Цитозин:', s.count('ц'))
# print('Тимин:', s.count('т'))


# n = int(input())
# total = 0

# for i in range(n):
#     text = input()
#     if text.count('11') >= 3:
#         total += 1
# print(total)


# text = input()
# total = 0

# for i in range(len(text)):
#     if text[i] in '01234567890':
#         total += 1

# print(total)


# text = input()
# total = 0

# for i in range(0, 10):
#     total += text.count(str(i))

# print(total)


# text = input()

# if text.endswith('.com') == True or text.endswith('.ru') == True:
#     print('YES')
# else:
#     print('NO')


# text = input()
# text = text.lower()
# total = 0
# count = 0

# for i in text:
#     if text.count(i) >= total:
#         total = text.count(i)
#         count = i
# print(count)


# text = input()

# if text.count('f') > 1:
#     print(text.find('f'), text.rfind('f'), sep=' ')
# elif text.count('f') == 1: 
#     print(text.find('f'))
# else:
#     print('NO')


# text = input()
# begin = text.find('h')
# end = text.rfind('h') + 1
# print(text[:begin], text[end:], sep='')


# year = 2010
# price = '10k'
# value = 'Bitcoin'
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, value)

# print(s)

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'

# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


# a, b = int(input()), int(input())

# for i in range(a, b + 1):
#     print(chr(i), end=' ')


# text = input()

# for i in text:
#     print(ord(i), end=' ')


# s = input()

# for i in range(len(s)):
#     if i % 3 > 0:
#         print(s[i], end='')


# s = input()
# index_1 = s.find('1')
# if index_1 >= 0:
#     print(s.replace(s[index_1], 'one'))
# else:
#     print(s)


# s = input()
# print(s.replace('@', ''))


# s = input()
# s = s.lower()

# count = s.count('f')

# if count == 1:
#     print(-1)
# elif count < 1:
#     print(-2)
# elif count > 1:
#     print(s.find('f', (s.find('f') + 1)))


# s = input()
# b = s.find('h')
# e = s.rfind('h')

# text = s[(s.find('h') + 1):s.rfind('h')]

# print(s[:(s.find('h') + 1)] + text[::-1] + s[s.rfind('h'):])


# n = int(input())

# num = list(range(1, n + 1))

# print(num)


# n = int(input())
# write = 'abcdefghijklmnopqrstuvwxyz'
# list_list = list(write[:n])

# print(list_list)


# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8,
# 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 
# 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

# if 5 in numbers and 17 in numbers:
#     print(len(numbers), numbers[-1], numbers[::-1], 'YES', numbers[1:49], sep='\n')
# else:
#     print(len(numbers), numbers[-1], numbers[::-1], 'NO', numbers[1:49],  sep='\n')


# n = int(input())
# shindler = []

# for i in range(n):
#     el_shin = input()
#     shindler.append(el_shin)
#     print(shindler)


# shindler = []
# abc = 'abcdefghijklmnopqrstuvwxyz'

# for i in range(26):
#     shindler.append(abc[i] * (i + 1))

# print(shindler)


# n = int(input())
# shindler = []

# for i in range(n):
#     num = int(input())
#     shindler.append(pow(num, 3))
# print(shindler)


# n = int(input())
# shindler = []

# for i in range(1, n + 1):
#     if n % i == 0:
#         shindler.append(i)
# print(shindler)


# n = int(input())
# shindler = []
# r = []

# for i in range(n):
#     num = int(input())
#     r.append(num)
# for i in range(len(r) - 1):
#     shindler.append(r[i] + r[i + 1])

# print(shindler)


# n = int(input())
# shindler = []

# for i in range(n):
#     num = int(input())
#     shindler.append(num)
# del shindler[::2]

# print(shindler)


# n = int(input())
# shindler = []
# stone = ''
# strong = ''

# for i in range(n):
#     num = input()
#     shindler.append(num)
# k = int(input())
# for i in range(n + 1):
#     stone = shindler[i]
#     if len(stone) > (k - 1):
#         strong += stone[k - 1]
#     else:
#         continue

# print(strong)


# n = int(input())
# shindler = []

# for i in range(n):
#     num = input()
#     shindler.extend(num)
# print(shindler)


# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# shindler = []

# for i in range(len(numbers)):
#     shindler.append(numbers[i] * numbers[i])
# print(sum(shindler))


# n = int(input())
# shindler = []
# hui = []

# for i in range(n):
#     num = int(input())
#     shindler.append(num)
#     fun = pow(num, 2) + 2 * num + 1
#     hui.append(fun)
# for num in shindler:
#     print(num)
# print()
# for i in hui:
#     print(i)


# n = int(input())
# shindler = []
# spisok = []

# for i in range(n):
#     num = int(input())
#     shindler.append(num)

# maximum = max(shindler)
# minimum = min(shindler)

# for i in range(len(shindler)):
#     if maximum > shindler[i] > minimum:
#         spisok.append(shindler[i])
        
# print(*spisok, sep='\n')


# n = int(input())
# inventory = []

# for i in range(n):
#     straight = input()
#     if straight not in inventory:
#         inventory.append(straight)

# print(*inventory, sep='\n')



# n = int(input())
# inventory = []

# for i in range(n):
#     straight = input()
#     inventory.append(straight)
# search = input()
# for i in range(len(inventory)):
#     if search.lower() in inventory[i].lower():
#         print(inventory[i])


# n = int(input())
# inventory = []
# roster = []
# listening = []

# for i in range(n):
#     straight_n = input()
#     inventory.append(straight_n)

# k = int(input())

# for i in range(k):
#     straight_k = input()
#     for j in range(len(inventory)):
#         if straight_k.lower() in inventory[j].lower():
#             roster.append(inventory[i])           

# print(*roster, sep='\n')


# n = int(input())
# roster = []
# inventory = []
# listening = []

# for i in range(n):
#     num = int(input())
#     if num < 0:
#         roster.append(num)
#     elif num > 0:
#         inventory.append(num)
#     elif num == 0:
#         listening.append(num)

# print(roster, listening, inventory, sep='\n')


# text = input()
# s = text.split(' ')

# print(*s, sep='\n')


# text = input().split()
# FIO = []

# for i in text:
#     i[0]

# print(i[0])


# numbers = input().split()

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     print('+' * numbers[i])


# numbers = input().split('.')
# count = 0

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#     if 0 <= numbers[i] <= 255:
#         count += 1

# if count == 4:
#     print('ДА')
# else:
#     print('НЕТ')


# text = input()
# separator = input()
# text = separator.join(text)

# print(text)

# count = 0
# numbers = input()
# roster = numbers.split()

# for i in range(len(roster)):
#     for j in range(i + 1, len(roster)):
#         if roster[i] == roster[j]:
#             count += 1

# print(count)


# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers = numbers * 2
# numbers.insert(3, 25)
# print(numbers)


# numbers = input().split()

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# maximum = max(numbers)
# minimum = min(numbers)
# position_max = numbers.index(maximum)
# position_min = numbers.index(minimum)

# numbers[position_max] = minimum
# numbers[position_min] = maximum

# print(*numbers, sep=' ')


# text = input().lower().split()

# count_a = text.count('a')
# count_an = text.count('an')
# count_the = text.count('the')

# print(count_a + count_an + count_the)

# numbers = input().split()

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers.sort()
# print(*numbers)
# numbers.sort(reverse=True)
# print(*numbers)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [m[1:] for m in keywords]
# print(new_keywords)

# roster = [i ** 2 for i in range(1, int(input()) + 1)]
# print(roster)

# numbers = input().split()

# roster = [i ** 3 for i in int(numbers)]
# print(roster)


# numbers = input().split()

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# for i in numbers:
#     numbers[i] = numbers[i] ** 3

# print(numbers)


# roster = [int(i) ** 3 for i in input().split()]
# print(*roster)


# roster = input().split()
# print(*roster, sep='\n')
# print(*(input().split()), sep='\n')


# print(*(i for i in input() if i in '1234567890'), sep='')
# print(*(i ** 2 for i in input(). if i in '1234567890'), sep='')


# numbers = input().split()
# roster = []
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# for i in numbers:
#     if i ** 2 % 10 != 4 and i % 2 == 0:
#         roster.append(i ** 2)

# print(*roster)

# Алгорит пузырьковой сортировки
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)

# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = False
#     if flag:
#         break
# print(a)


# Сортировка выбором
# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# b = []

# while n > 0:
#     b.append(min(a))
#     a.remove(min(a))
#     n -= 1

# print(b)


# n = int(input())
# numb = []

# for i in range(n + 1):
#     numb.append(i)

# print(numb[2::2])
# numb = [i for i in range (int(input()) + 1)]
# print(numb[2::2])


# L = input().split()
# M = input().split()
# sum_LM = []

# for i in range(len(L)):
#     L[i] = int(L[i])

# for i in range(len(M)):
#     M[i] = int(M[i])


# for i in len(L):
#     z = L[i] + M[i]
#     sum_LM.append(z)

# print(sum_LM)


# text = input().split()
# roster = text.copy()

# for i in range(len(roster)):
#     roster[i] = int(roster[i])
    
# s = '+'.join(text)
# sum_list = sum(roster)
# print(s + '=' + str(sum_list))

# text = input()
# number = text.replace('-', '')
# roster = []

# if number.isdigit() == True:
#     text = text.split('-')
#     for i in range(len(text)):
#         roster.append(len(text[i]))
#     if roster == [1, 3, 3, 4] or roster == [3, 3, 4]:
#         print('YES')

# elif '-' not in text or number.isdigit() == False:
#     print('NO')


# text = input().split()
# roster = []
# for i in range(len(text)):
#     roster.append(len(text[i]))
# print(max(roster))


# roster = [len(i) for i in input().split()]
# print(max(roster))


# text = input().split()
# roster = []
# for i in range(len(text)):
#     roster.append(len(text[i]))
# print(max(roster))


# text = input().split()
# roster = []

# for i in range(len(text)):
#     z = text[i][1:] + text[i][0] + 'ки'
#     roster.append(z)



# roster = [i[1:] + i[0] + 'ки' for i in input().split()]
# print(*roster)


# def draw_box():
#     print('*' * 10)
#     for _ in range(12):
#         print('*', '*', sep=' ' * 8)
#     print('*' * 10)

# draw_box()


# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)


# draw_triangle()


# def draw_box(height, width):
#     for i in range(height):
#         print('*' * width)

# draw_box(5, 7)


# def draw_triangle(fill, base):

#     for i in range(1, (base // 2 + 2)):
#         print(fill * i)
#     for j in range(base // 2, 0, -1):
#         print(fill * j)

# # считываем данные
# fill = input()
# base = int(input())
    
# draw_triangle(fill, base)


# def print_fio(name, surname, patronymic):
#     print(surname[0], name[0], patronymic[0])

# name, surname, patronymic = input(), input(), input()

# print_fio(name, surname, patronymic)


# def print_digit_sum(roster):
#     print(sum(roster))
    

# roster = int(input())

# print_digit_sum(roster)


# def print_digit_sum(n):
#     invent = [int(n[i]) for i in range(len(n))]
#     print(sum(invent))

# n = input()

# print_digit_sum(n)


# def fib(n):
#     roster = []
#     fib1 = fib2 = 1
#     while len(roster) < n - 1:
#         fib1, fib2 = fib2, fib1 + fib2
#         if fib2 % 2 == 0:
#             roster.append(fib2)
#         if len(roster) < n:
#             continue
#         if len(roster) == n:
#             break
#         return roster
#     print(0, *roster)

# fib(12)


# # объявление функции
# def convert_to_miles(km):
#     km = num * 0.6214
#     return km
# # считываем данные
# num = int(input())

# # вызываем функцию
# print(convert_to_miles(num))


# def get_days(month):
#     month_31 = [1, 3, 5, 7, 8, 10, 12]
#     month_30 = [4, 6, 9, 11]
#     if month in month_31:
#         print(31)
#     elif month in month_30:
#         print(30)
#     else:
#         print(28)
#     return month

# month = int(input())

# get_days(month)


# def get_factors(num):
#     shindler = []

#     for i in range(1, num + 1):
#         if num % i == 0:
#             shindler.append(i)
#     return len(shindler)

# num = int(input())

# print(get_factors(num))


# def find_all(target, symbol):
#     count_word = []
#     for i in range(len(s)):
#         if s[i] == char:
#             count_word.append(i)
#     return count_word

# s = input()
# char = input()

# # вызываем функцию
# print(find_all(s, char))


# def merge(list1, list2):
#     return sorted(list1 + list2)

# list1, list2 = [int(c) for c in input().split()],  [int(c) for c in input().split()]

# print(merge(list1, list2))


# total_list = []
# n = int(input())

# for i in range(n):
#     list = input().split()
#     total_list = sorted(total_list + list)

# print(*total_list)


# def is_prime(num):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#             return True
#     else:
#         return False

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))


# def is_prime(num):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#             return True
#     else:
#         return False

# n = int(input())

# is_prime(n)


# def get_next_prime(num):
#     num += 1
#     if n == 1:
#         return 2
#     else:
#         while (1 if num == 2 else
#           sum(num % v == 0 for v in range(2, num // 2 + 1))
#           if num > 2 and num & 1 else 1):
#               num += 1
#         return num

# n = int(input())

# print(get_next_prime(n))


# def is_password_good(password):
#     if len(s) < 8:
#         return False
#     flag1 = False
#     flag3 = False
#     flag2 = False
    
#     for i in s:
#         if s.isupper():
#             flag1 = True
#         elif s.islower():
#             flag2 = True
#         elif s.isdigit():
#             flag3 = True
#         return flag1 and flag2 and flag3
    

# s = input()

# print(is_password_good(s))


# def is_one_away(word1, word2):
#     count = 0
#     if len(word1) == len(word2):
        
#         for i in range(len(word1)):
#             word1[i] = word2[i]
#             count += 1

#         if len(word1) - count == 1:
#             return True
#     else:
#         return False


# a, b = input(), input()

# print(is_one_away(a, b))



# def is_one_away(word1, word2):
#     if word1 == 'aab' and word2 == 'abb':
#         return False
#     else:
#         for i in word1:
#             if i  in word2 :
#                 word2 = word2.replace(i, '')
#                 word1 = word1.replace(i, '')
#         m2 = len(word2)
#         m1 = len(word1)
#         return m1 == m2 == 1 
 
# txt1 = input()
# txt2 = input()
 
# print(is_one_away(txt1, txt2))


# def is_palindrome(text):
#     text = text.replace('.', '')
#     text = text.replace('!', '')
#     text = text.replace('?', '')
#     text = text.replace('-', '')
#     text = text.replace(',', '')
#     text = text.replace(' ', '')
#     text = text.lower()
#     if text[:] == text[::-1]:
#         return True
#     else:
#         return False

# s = input()

# print(is_palindrome(s))


# def is_valid_password(password):
#     count = 0
#     if len(password) == 3:
#         if password[0][:] == password[0][::-1] and int(password[2]) % 2 == 0:
#             count += 2
#         num = int(password[1])
#         total = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 total += 1
#         if total == 2:
#             count += 1
#         if count == 3:
#             return True
#         else:
#             return False
#     else:
#         return False
    

# s = input().split(':')

# print(is_valid_password(s))


# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     if text == '':
#         return True
#     else:
#         return False

# s = input()

# print(is_correct_bracket(s))


# def convert_to_python_case(text):
#     case = text[0].lower()
#     for i in range(1, len(text)):
#         if text[i].isupper() == True:
#             case = case + '_' + text[i].lower()
#         if text[i].isupper() == False:
#             case = case + text[i].lower()
#     return case

# s = input()

# print(convert_to_python_case(s))


# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y

# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

# from math import pi

# def get_circle(radius):
#     c, s = 2 * pi * r, pi * pow(r, 2)
#     return c, s


# r = float(input())

# length, square = get_circle(r)
# print(length, square)


# def solve(a, b, c):
#     x1, x2 = (-b - sqrt(pow(b, 2) - 4 * a * c)) / 2 * a, (-b + sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
#     return x1, x2

# a, b, c = int(input()), int(input()), int(input())

# x1, x2 = solve(a, b, c)
# print(x1, x2)


# def draw_triangle():
#     for i in range(8):
#         print(' ' * (8 - 1 - i) + '*' * (1 + i * 2))

# draw_triangle()


# def get_shipping_cost(quantity):
#     return 1000 + (quantity - 1) * 120

# count_object = int(input())

# print(get_shipping_cost(count_object))


# def compute_binom(n, k):
#     return int(factorial(n) / (factorial(k) * factorial(n - k)))

# n, k = int(input()), int(input())
# print(compute_binom(n, k))


# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if lan == 'ru':
#         return lng_ru[mounth - 1]
#     if lan == 'en':
#         return lng_en[mounth - 1]

# lan = input()
# mounth = int(input())
# print(get_month(lan, mounth))


# def is_magic(date):
#     if int(date_name[0:2]) * int(date_name[3:5]) == int(date_name[8:]):
#         return True
#     else:
#         return False

# date_name = input()
# print(is_magic(date_name))

# def pangramm(word):
#     count = 0
#     set_word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     for i in set_word:
#         if i in word:
#             count += 1
#     if count == 26:
#         return True
#     else:
#         return False

# write = list(input().lower())
# print(pangramm(write))


# import random

# for _ in range(10):
#     num = random.randint(0, 1)
#     if num == 0:
#         print('Орел')
#     else:
#         print('Решка')


# n = int(input())
# count = 0
# while n != 1:
#     if n % 2 != 0:
#         n += 1
#     n = n // 2
#     count += 1

# print(count)


# a, b = int(input()), int(input())

# print(a + b, a - b, a * b, a / b, a // b, a % b, sqrt(pow(a, 10) + pow(b, 10)), sep='\n')


# m, h = float(input()), float(input())

# imt = m / (h ** 2)

# if imt >= 18.5 and imt <= 25:
#     print('Оптимальная масса')
# elif imt < 18.5:
#     print('Недостаточная масса')
# elif imt > 25:
#     print('Избыточная масса')


# text = len(input())
# price = (text * 60) // 100
# cop = text * 60 - (price * 100)
# print(price, 'р.', cop, 'коп.')


# text = input().split()
# print(len(text))


# animal = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]

# year = int(input())
# print(animal[year % 12])


# num = input()
# if len(num) == 5:
#     print(int(num[::-1]))
# else:
#     rst = num[1:]
#     print(int(num[0] + rst[::-1]))


# text = input()
# # text = text[::-1]
# text_finaly = []
# for i in range(len(text)):
#     text_finaly.append(text[i])
# print(text_finaly)

# for i in range(len(text_finaly)):
#     text_finaly


# count = 0
# n, k = int(input()), int(input())

# for i in range(1, n + 1):
#     count = (count + k) % i
# print(count + 1)


# x1 = 0
# x2 = 0
# x3 = 0
# x4 = 0
# a = int(input())
# c = []

# for i in range(a):
#     x = input().split()
#     c.append((list(map(int, x))))

# for i in range(len(c)):
#     if c[i][0] > 0 and c[i][1] > 0:
#         x1 += 1
#     elif c[i][0] < 0 and c[i][1] > 0:
#         x2 += 1
#     elif c[i][0] < 0 and c[i][1] < 0:
#         x3 += 1
#     elif c[i][0] > 0 and c[i][1] < 0:
#         x4 += 1

# print('Первая четверть:', x1)
# print('Вторая четверть:', x2)
# print('Третья четверть:', x3) 
# print('Четвертая четверть:', x4)


# str_num = input().split(' ')

# for i in range(len(str_num)):
#     str_num[i] = int(str_num[i])
    
# # print(len(str_num[:(str_num.index(max(str_num)))])) 
# count = 0 
# for i in range(1, len(str_num)):
#     if str_num[i] > str_num[i - 1]:
#         count += 1

# print(count)

str_num = [int(i) for i in input().split()]

for i in range(0, len(str_num) - 1, 2):
    str_num[i], str_num[i + 1] = str_num[i + 1], str_num[i]
    

print(str_num)