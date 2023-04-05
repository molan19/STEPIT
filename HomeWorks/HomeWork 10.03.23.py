'''#1.	Реализовать рекурсивную функцию возведения элементов в степень. Функция принимает два параметра х и у.
#Функция должна вернуть реузльтат в виде возведения числа х в степень у
def stepen(x,y):
    if y == 1:
        return x
    else:
        return x * stepen(x,y-1)

print(stepen(2,4))'''
'''#2.Реализовать рекурсивную функцию для нахождения последовательности Фибоначчи. Функция принимает один параметр,
# она должна вернуть результат конечной суммы.
#Последовательность Фиббоначи -элементы числовой последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,…
#в которой первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисе
#Если число равно 0, то возвращаем 0
#Если число равно 1, то возвращаем 1
#В ином случае возвращаем рекурсию в виде сумме двух предыдущих чисел.
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))'''
'''#3.Напишите функцию, которая отображает пустой или
#заполненный квадрат из некоторого символа. Функция
#принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
#■ если она равна True, квадрат заполненный;
#■ если False, квадрат пустой.
def kvadrat(simvol, dlina, vibor):
    counter = dlina
    while counter > 0:
        if vibor == True:
            counter -= 1
            print(simvol * dlina)
        if vibor == False:
            counter = 0
            print(simvol * dlina)
            for i in range(dlina):
                print(simvol + " " * (dlina - 2) + simvol)
            print(simvol * dlina)



kvadrat(input('Введите символ'), 3, True)'''

from random import randint
'''#4.	Сделать игру угадай число через функции.
def ugaday_chislo(num):
    chislo = randint(1,100) #10
    while True:
        num = int(input())
        if num > chislo:#25 > 10
            print('Загаданное число меньше')
        if num < chislo: #25 < 35
            print('Загаданное число больше')
        if num == chislo:
            print('Вы угадали число')
            print("Хотите начать игру снова?")
            otvet = int(input("1 - Да, 2 - Нет"))
            chislo = randint(1, 100)
            if otvet == 2:
                break
            else:
                continue
ugaday_chislo(2)'''
'''#5.	Напишите функцию, вычисляющую произведение ВСЕХ элементов вложенных списков целых чисел(размер массива m на n.
#Список передаётся в качестве параметра. Полученный результат возвращается из функции
def summ(list_el):
    m,n = int(input()),int(input())
    proiz = 1
    list_el = [[randint(1,10) for j in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            proiz *= list_el[i][j]
            print(list_el)
    return proiz

print(summ([[[randint(1,10) for j in range(7)]for i in range(8)]]))'''
'''#6.	Напишите функцию, вычисляющую сумму ВСЕХ элементов вложенных списков целых чисел(размер массива m на n.
#Список передаётся в качестве параметра. Полученный результат возвращается из функции
def summ1(list_el):
    m,n = int(input()),int(input())
    summ = 0
    list_el = [[randint(1,10) for j in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            summ += list_el[i][j]
            print(list_el)
    return summ

print(summ1([[[randint(1,10) for j in range(7)]for i in range(8)]]))'''

