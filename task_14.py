# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# Объявление переменных и ввод данных
num = int(input('Введите натуральное число больше 1 : '))
pow = 1
i = 0

# Расчет и вывод результатов
while pow < num :
    print (f'{pow} есть 2 в степени {i}')
    i = i + 1
    pow = 2 ** i

# 2 ** 0 = 1, 0 - целое число.