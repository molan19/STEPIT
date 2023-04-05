#1. Написать функцию которая обработает исключение при делении двух чисел.
'''def zad_1(num1,num2):
    if num2 == 0:
        raise Exception ('Нельзя делить на 0')
    return num1/num2
zad_1(12,0)'''
#2. Обработайте исключение при работе с математическими операциями(например корни отрицательных чисел)
'''from math import sqrt
def zad_2(num):
    if num < 0:
        raise Exception ('Корень числа не может быть отрицательным')
    return (sqrt(num))
zad_2(-2)'''
#3. Обработайте исключенийе при работе со списками( выход за пределы индексации списка)
'''def zad_3(list_el):
    try:
        for i in range(len(list_el)+1):
            if i == len(list_el):
                raise Exception ('Вы вышли за пределы индексации списка')
    except Exception as e:
        print(e)
list_el = [1,2,3,4]
zad_3(list_el)'''
#4. Обработайте исключение при работе с типами данных(например ввод не тех типов данных или работа с несовместимыми типами)
'''def zad_4():
    try:
        print('Вы хотите ввести число или строку?')
        vibor_1 = int(input('1 - Число, 2 - Строку'))
        if vibor_1 == 1:
            num1 = int(input())
        else:
            raise TypeError ('num1 не может быть string')
        vibor_2 = int(input('1 - Число, 2 - Строку'))
        if vibor_2 == 1:
            num2 = int(input())
        else:
            raise TypeError ('num2 не может быть string')
    except TypeError as e:
        print(e)
zad_4()'''
#5. Обработайте исключение при работе со строками(допустим выход за пределы индексации или не корректный ввод)
'''def zad_5(word):
    try:
        for i in range(len(word)+1):
            if i == len(word):
                raise Exception ('Вы вышли за пределы индексации строки')
    except Exception as e:
        print(e)
word = 'abcd'
zad_5(word)'''
#6. Обработайте исключение при работе с конвертацией типов данных
'''def zad_6():
    try:
        print('Хотите ли вы перевести string в int')
        vibor = int(input('1 - Да, 2 - Нет'))
        if vibor == 1:
            stroka = input()
            if stroka.isdigit() == True:
                print('Вы перевели string в int')
            else:
                raise Exception('Вы не можете перевести string в int,которая состоит из букв')
        if vibor == 2:
            print('Всего хорошего')
    except Exception as e:
        print(e)
zad_6()'''

