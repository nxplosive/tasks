# # TODO 1 Сама неотвратимость 🌶️
# # Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной по
# # щелчку пальцев. При этом если население Вселенной является нечетным числом, то титан проявит милосердие и округлит
# # количество выживших в большую сторону. Помогите Мстителям подсчитать количество выживших.
#
# n = int(input())
# z = -n // 2
# print(-z)
#
#
# # TODO 2 Трехзначное число
# # Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
#
# num = int(input())
# num1 = num // 100
# num2 = (num // 10) % 10
# num3 = num % 10
# sum = num1 + num2 + num3
# prz = num1 * num2 * num3
# print('Сумма цифр =', sum)
# print('Произведение цифр =', prz)
#
#
# # TODO 3 Четырёхзначное число
# # Напишите программу для нахождения цифр четырёхзначного числа.
#
# num = int(input())
# num1 = num // 1000
# num2 = (num // 100) % 10
# num3 = (num // 10) % 10
# num4 = num % 10
# print('Цифра в позиции тысяч равна', num1)
# print('Цифра в позиции сотен равна', num2)
# print('Цифра в позиции десятков равна', num3)
# print('Цифра в позиции единиц равна', num4)
#
#
# # TODO 4 Наименьшее из четырёх чисел 🌶️
# # Напишите программу, которая определяет наименьшее из четырёх чисел.
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a > b:
#     a = b
# else:
#     a = a
# if c > d:
#     c = d
# else:
#     c = c
# if a < c:
#     print(a)
# else:
#     print(c)
#
#
# # TODO 5 Только + 🌶️
# # Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
#
# a = int(input())
# b = int(input())
# c = int(input())
# if a <= 0:
#     a = 0
# else:
#     a = a
# if b <= 0:
#     b = 0
# else:
#     b = b
# if c <= 0:
#     c = 0
# else:
#     c = c
# d = a + b + c
# print(d)
#
#
# # TODO 6 Шахматная доска
# # Заданы две клетки шахматной доски. Напишите программу, которая определяет, имеют ли указанные клетки один цвет или нет.
# # Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета, то «NO».
#
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1 + y1 + x2 + y2) % 2 == 0:
#     print('YES')
# else:
#     print('NO')
#
#
# # TODO 7 Ход ладьи
#
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO")
#
#
# # TODO 8 Ход слона 🌶️
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1 - y1) == (x2 - y2) or (x1 + y1) == (x2 + y2):
#     print('YES')
# else:
#     print('NO')
#
#
# # TODO 9 Ход короля 🌶️
#
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if -1 <= (x2 - x1) <= 1 and -1 <= (y2 - y1) <= 1:
#     print("YES")
# else:
#     print("NO")
#
#
# # TODO 10 Ход коня
#
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 + 1 and y1 == y2 + 2 or (x1 == x2 + 2 and y1 == y2 + 1):
#     print('YES')
# elif x1 == x2 - 1 and y1 == y2 - 2 or (x1 == x2 - 2 and y1 == y2 - 1):
#     print('YES')
# elif x1 == x2 - 1 and y1 == y2 + 2 or (x1 == x2 - 2 and y1 == y2 + 1):
#     print('YES')
# elif x1 == x2 + 1 and y1 == y2 - 2 or (x1 == x2 + 2 and y1 == y2 - 1):
#     print('YES')
# else:
#     print('NO')
#
#
# # TODO 11 Ход ферзя
#
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (x1 - y1) == (x2 - y2) or (x1 + y1) == (x2 + y2) or ((x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2)):
#     print('YES')
# else:
#     print('NO')
#
#
# # TODO 12 Самописный калькулятор 🌶️
#
# num1, num2, num3 = int(input()), int(input()), input()
# if num3 == ('+'):
#     print(num1 + num2)
# elif num3 == ('-'):
#     print(num1 - num2)
# elif num3 == ('*'):
#     print(num1 * num2)
# elif num3 == ('/'):
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print('На ноль делить нельзя!')
# else:
#     print('Неверная операция')
#
#
# # TODO 13 Цветовой микшер 🌶️
#
# col1 = input()
# col2 = input()
# if col1 == 'красный' and col2 == 'красный':
#     print('красный')
# elif col1 == 'синий' and col2 == 'синий':
#     print('синий')
# elif col1 == 'желтый' and col2 == 'желтый':
#     print('желтый')
# elif col1 == 'красный' and col2 == 'синий' or (col2 == 'красный' and col1 == 'синий'):
#     print('фиолетовый')
# elif col1 == 'красный' and col2 == 'желтый' or (col2 == 'красный' and col1 == 'желтый'):
#     print('оранжевый')
# elif col1 == 'синий' and col2 == 'желтый' or (col2 == 'синий' and col1 == 'желтый'):
#     print('зеленый')
# else:
#     print('ошибка цвета')
#
#
# # TODO 14 Цвета колеса рулетки 🌶️
#
# x = int(input())
# if x == 0:
#     print('зеленый')
# elif (x > 0 and x <= 36 and (x % 2 == 0 and x <= 10) or (x % 2 != 0 and x >= 11 and x <= 18) or
#       (x % 2 == 0 and x >= 19 and x <= 28) or (x % 2 != 0 and x >= 29 and x <= 36)):
#     print('черный')
# elif (x > 0 and x <= 36 and (x % 2 != 0 and x <= 10) or (x % 2 == 0 and x >= 11 and x <= 18) or
#       (x % 2 != 0 and x >= 19 and x <= 28) or (x % 2 == 0 and x >= 29 and x <= 36)):
#     print('красный')
# else:
#     print('ошибка ввода')
#
#
# # TODO 15 Пересечение отрезков 🌶️🌶️
#
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# # пустое множество #
# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# # касание #
# elif b1 == a2:
#     print(b1)
# elif b2 == a1:
#     print(b2)
# # равенство #
# elif a1 == a2 and b1 == b2:
#     print(a1, b1)
# # остальные варианты #
# elif a1 <= a2 < b1 < b2:
#     print(a2, b1)
# elif a2 <= a1 < b2 < b1:
#     print(a1, b2)
# elif a2 < a1 < b1 <= b2:
#     print(a1, b1)
# elif a1 < a2 < b2 <= b1:
#     print(a2, b2)
# 
# 
# # TODO 16 Dog age
# На вход программе подается число 
# n – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.
# 
# a = float(input())
# if 0 <= a <= 2:
#     print(a * 10.5)
# elif a > 2:
#     print(21 + (a - 2) * 4)
# 
# 
# # TODO 17 Наибольшее и наименьшее
# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
# 
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# minim = min(a,b,c,d,e)
# maxim = max(a,b,c,d,e)
# print('Наименьшее число =', minim)
# print('Наибольшее число =', maxim)
# 
# 
# # TODO 18 Сортировка трёх 🌶️
# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# 
# a = int(input())
# b = int(input())
# c = int(input())
# mini = min(a, b, c)
# maxi = max(a, b, c)
# midl = a + b + c - (mini + maxi)
# print(maxi)
# print(midl)
# print(mini)
# 
# 
# # TODO 19 Манхэттенское расстояние
# 
# p1 = int(input())
# p2 = int(input())
# q1 = int(input())
# q2 = int(input())
# m = abs(p1-q1)+abs(p2-q2)
# print(m)
