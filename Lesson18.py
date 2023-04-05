'''try:
    num = int(input())
    print(num)
except:
    print('Не пиши ничего кроме целых чисел')
else:
    print('Что то еще')'''


'''try: 
    num1 = int(input())
    num2 = int(input())
    if num2 == 0:
        raise Exception('Не дели на 0')
    print('result', num1/num2)
except ValueError:
    print('check data again')
except Exception as e:
    print(e)'''
from math import sqrt
'''try:
    num = int(input())
    if num > 0:
        print(sqrt(num))
    raise Exception('Короень не может быть меньше 0')
except Exception as e:
    print(e)'''
#3. Обработайте исключенийе при работе со списками( выход за пределы индексации списка)
#4. Обработайте исключение при работе с типами данных(например ввод не тех типов данных или работа с несовместимыми типами)
#5. Обработайте исключение при работе со строками(допустим выход за пределы индексации или не корректный ввод)
#6. Обработайте исключение при работе с конвертацией типов данных.
#3 задание
'''try:
    list_el = [1,2,3,4,5]
    for i in range(len(list_el)+1):
        if i == len(list_el):
            raise Exception ('Вы вышли за пределы данных')
except Exception as e:
    print(e)'''
#4 задание
'''try:
    print('Вы хотите ввести число или строку?')
    vibor_1 = int(input('1 - Число , 2 - Строка'))
    if vibor_1 == 1:
        num1 = int(input())
    else:
        raise TypeError ('ОШИБКА')
    vibor_2 = int(input('1 - Число , 2 - Строка'))
    if vibor_2 == 1:
        num2 = int(input())
    else: raise TypeError ('ОШИБКА Х2')
except TypeError as e:
    print(e)'''
#5 задание
'''try:
    spisok = 'abcdef'
    for i in range(len(spisok)+1):
        if i == len(spisok):
            raise Exception ('Вы вышли за пределы')
except Exception as e:
    print(e)'''
#6 задание
'''try:
    vibor = int(input('1 - перевод str в int'))
    if vibor == 1:
        word = input()
        if word.isdigit() == True:
            print('all good')
        else:
            raise Exception ('Вы не можете перевести эту переменную в int')
except Exception as e:
    print(e)'''
#Задание 1 с функцией
'''def ne_deli_na_0(num1,num2):
    if num2 == 0:
        raise Exception ('Нельзя делить на 0')
    return num1/num2

ne_deli_na_0(12,0)'''
