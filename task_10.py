# Задача №10 На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# Объявление переменных и ввод данных

num_coins = int(input('Укажите предполагаемое число монет: '))
i = 1
odd = 0
even = 0

# Вспомогательное вычисление: раскладка монет

while i < num_coins+1:
    a = int (input ('Укажите расположение монетки (четное число - орел, нечетное - решка): '))
    if a % 2 == 0:
        print (f'Монетка {i} - герб')
        even = even + 1
    else:
        print (f'Монетка {i} - решка')
        odd = odd + 1
    i = i + 1
if even < odd :
    print (f'Нужно перевернуть монеты, расположенные гербом вверх, всего {even} шт.')
else:
    print (f'Нужно перевернуть монеты, расположенные решкой вверх, всего {odd} шт.')