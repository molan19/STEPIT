'''#. Сделайте игру угадай число, пусть каждое угаданное число добавляется в список ,
#если игрок угадал число игроку выводится список угаданных чисел и выводится сообщение,”хотите начать игру снова?”,
#если да игра запускается вновь, список очищается и алгоритм повторяется, если игрок не хочет, то игра заканчивается.
#Если игрок не угадал число, то программа подсказывает холодно или жарко.
from random import randint
spisok_ugadannih = []
chislo = randint(0, 100)
while True:
    num = int(input("Введи число"))
    if num > chislo:
        print("Горячо")
    if num < chislo:
        print("Холодно")
    if num == chislo:
        spisok_ugadannih.append(num)
        print(spisok_ugadannih)
        print("Хотите начать игру снова?")
        otvet = int(input("1 - Да, 2 - Нет"))
        chislo = randint(0, 100)
        if otvet == 2:
            break
        else:
            continue'''

'''#вводятся два числа х и у , напишите программу возведения в степень числа х в у , не используя оператор **

x = int(input()) #2
y = int(input()) #3
counter = 1
while y > 0:
    counter *= x #1*2 =2 2*2 = 4 4*2 = 8
    y -= 1 #3-1 =2 2-1 = 1 1-1 = 0
print(counter)

x_2 = int(input()) #2
y_2 = int(input())
print(pow(x_2,y_2))'''

#Напишите программу на Python для удаления дубликатов из списка. +
# #Напишите программу на Python, чтобы проверить, пустой список или нет +
# #Напишите программу на Python, чтобы найти список слов, + длина которых превышает n, из заданного списка слов +
# #Напишите функцию Python, которая принимает два списка и возвращает True, если у них есть хотя бы один общий член. +
# #Напишите программу на Python для печати указанного списка после удаления 0-го, 4-го и 5-го элементов

'''# Задание 2
    spisok = [1,2,3,5,6]
spisok_2 = []
if spisok != spisok_2:
    print("Не пустой")
else:
    print("Пустой")'''

'''# Задание 3
    spisok = ["кит","томат", "ошибка","ток","посуда"]
slovo = 'лол'
for i in spisok:
    if len(i) != len(slovo):
        print(i)'''

''' Задание 1
    spisok = [1,4,3,5,2,3,8,12,3]
duplicate = int(input())
for i in spisok:
    if i == duplicate:
        spisok.remove(duplicate)
        print(spisok)'''

''' #Задание 4
    spisok1 = [1,2,4,5,7]
spisok2 = [12,34,31,2,6]
for i in spisok1:
    for n in spisok2:
        if i == n:
            print(True)
        else:
            print(False)'''

''' #Задание 5
    spisok = [1,3,53,12,53,64,1,2,4,53]
print(spisok.pop(0), spisok.pop(3), spisok.pop(3))
print(spisok)
'''

