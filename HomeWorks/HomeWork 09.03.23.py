'''#2.	Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
#“Don't compare yourself with anyone in this world… if you do so, you are insulting yourself.”										 Bill Gates
def func(a):
    print("\"Don\'t compare yourself with anyone in this world... If you do so, you are insulting yourself.\" \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBill Gate")
text = 'ad'
func(text)'''
'''#3.	Напишите функцию, которая принимает два числа в качестве параметра и добавляет все четные числа между ними в список
#и выводит в качетсве реузльтата список из этих элементов.(генераторы)
def func1(num1,num2):
    spisok = []
    for i in range(num1,num2):
        if i%2 == 0:
            spisok.append(i)
    print(spisok)

func1(1,50)'''
'''#4.	Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.
def func3(num1,num2,num3,num4,num5):
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
        print(num1)
    if num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:
        print(num2)
    if num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
        print(num3)
    if num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
        print(num4)
    if num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:
        print(num5)

func3(3,23,42,8,1)'''
'''#Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров.
def summ1(num1,num2):
    multi = 1
    for i in range(num1,num2+1):
        multi *= i
    return multi
print(summ1(2,5))'''
'''#Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра.
#Из функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.
def func4(num):
    counter = 0
    while num > 0:#3456
        counter += 1
        num = num//10
    return counter
print(func4(345567))'''
'''#7.	Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве параметра.
#Если число палиндром нужно вернуть из функции true, иначе false. «Палиндром» — это число, у которого первая часть цифр
#равна второй перевернутой части цифр. Например, 123321 — палиндром (первая часть 123, вторая 321, которая после переворота
#становится 123), 546645 — палиндром, а 421987 — не палиндром.
def palindrom(num):
    num = input('Введите число:')
    for i in num:
        if num[0] == num[-1]:
            if num[1] == num[-2]:
                return True
            else:
                return False
print(palindrom(343))'''
'''#8.	Напишите функцию, которая возвращает сумму чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров.
def summ1(num1,num2):
    summ = 0
    for i in range(num1,num2+1):
        summ += i
    return summ


print(summ1(1,5))'''
