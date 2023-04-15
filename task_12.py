# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Объявление переменных и ввод данных

b = True

while b == True:
    sum = int(input('Введите сумму двух чисел (не более 2 000): '))
    mltp = int(input('Введите произведение двух чисел (не более 1 000 000): '))


# Предварительные вычисления
    des = sum ** 2 - 4 * mltp

# Проверка условий и вывод результата
    if des < 0 :
        print ('Для введенных значений задача не имеет решения. Повторите ввод')
    elif des == 0 :
        print (f'Загаданные числа равны {sum/2} и {sum/2}')
        b = False
    else :
        х = (sum + des ** 0.5)/2
        y = (sum - des ** 0.5)/2
        if х <= 0 or y <= 0 :
            print ('Для введенных значений задача не имеет решения. Повторите ввод')
        else:
            print (f'Загаданные два числа равны {х} и {y}')
            b = False

# В условиях задачи указано, что загаданы натуральные числа (больше 0) (!)

