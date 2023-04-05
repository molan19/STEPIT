from random import randint
'''#3. В списке целых чисел, заполненном случайными числами, определить минимальный и максимальный элементы,
#посчитать количество отрицательных элементов, посчитать количество положительных элементов,
#посчитать количество нулей. Результаты вывести на экран.
spisok = [randint(-50,50),randint(-50,50),randint(-50,50),randint(-50,50),randint(-50,50),randint(-50,50)]
count_otric = 0
count_polozh = 0
count_nol = 0
maximalnaya = -50
minimalnaya = 50
for i in range(0,len(spisok)):
    if spisok[i] < 0:
        count_otric += 1
    if spisok[i] > 0:
        count_polozh += 1
    if spisok[i] == 0:
        count_nol += 1
    if spisok[i] > maximalnaya:
        maximalnaya =spisok[i]
    if spisok[i] < minimalnaya:
        minimalnaya = spisok[i]
    print(f'список чисел {spisok[i]}' )
print(f'максимальное число: {maximalnaya} минимальное число: {minimalnaya}')
print(f'кол-во положительных: {count_polozh} кол-во отрицательных: {count_otric} кол-во нулей: {count_nol}')'''


'''#Пользователь с клавиатуры вводит элементы списка целых чисел и некоторое число.
#Необходимо посчитать сколько раз данное число присутствует в списке. Результат вывести на экран
spisok = [int(input()),int(input()),int(input()),int(input()),int(input())]
print(spisok.count(int(input()))) #про count я прочитал и понял как он работает(возвращает число,которое мы указали'''


'''#Пользователь с клавиатуры вводит элементы списка целых чисел.
#Необходимо посчитать сумму всех элементов и их среднеарифметическое. Результаты вывести на экран
spisok = [int(input()),int(input()),int(input()),int(input()),int(input()),]
spisok_summ = 0
for i in range(0,len(spisok)):
   spisok_summ += spisok[i]
   sredne_arifm = spisok_summ/len(spisok)
print(f'сумма чисел:{spisok_summ} \t среднеарифметичееское:{sredne_arifm}')'''


'''#Произведение чисел кратные 3
spisok_1 = [randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50)]
spisok_proiz = 1
for i in range(0,len(spisok_1)):
    if spisok_1[i]%3 == 0:
        spisok_proiz *= spisok_1[i]
        print(f'числа {spisok_1[i]}')
print(f'произведение чисел: {spisok_proiz}')'''

'''#Произведение минимального и максимального числа
spisok_1 = [randint(-50,50),randint(-50,50),randint(-50,50),randint(-50,50),randint(-50,50),randint(-50,50),randint(-50,50)]
spisok_proiz = 1
minimalnaya = 50
maximalnaya = -50
for i in range(0,len(spisok_1)):
    if spisok_1[i] > maximalnaya:
        maximalnaya = spisok_1[i]
    if spisok_1[i] < minimalnaya:
        minimalnaya = spisok_1[i]
    print(f'все числа: {spisok_1[i]}')
print(f' минимальное и максимальное числа: {minimalnaya} {maximalnaya}')
print(f'произведение чисел: {minimalnaya*maximalnaya}')'''
