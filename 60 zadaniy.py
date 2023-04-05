'''#1. Напишите программу, которая определяет, является ли число четным или нечетным.
number = int(input())
if number%2 == 0:
    print("Четное")
else:
    print("Нечетное")'''

'''#2. Введите два числа и отобразите на экране меньшее из них
number_1 = int(input())
number_2 = int(input())
if number_1 > number_2:
    print(number_2)
else:
    print(number_1)'''

'''#3. Программа, определяющая, является ли введенное число отрицательным или положительным (также рассмотрим случай 0)
num_1 = int(input())
if num_1 > 0:
    print("Положительное")
elif num_1 < 0:
    print("Отрицательное")
else:
    print("Это ноль")'''

'''#Должен сделать калькулятор. Введите два дробных числа a и b. Показать варианты выходит
#1) а + б
#2) а – б
#3) а*б
#4) а/б
num1 = float(input())
num2 = float(input())
opertation = int(input("Введите 1 для +, 2 для -, 3 для *, 4 для /"))
    if opertation == 1:
        print(num1+num2)
    if opertation == 2:
        print(num1-num2)
    if opertation == 3:
        print(num1*num2)
    if opertation == 4:
        print(num1/num2)'''

'''#5. Пользователь вводит число, которое проверяет, находится ли число в диапазоне 1-50. написать программу.
num = int(input())
    if num < 50 and num > 1:
        print("Да")
    else:
        print("Нет")'''

'''#6. Пользователь вводит два числа. ( X и Y ) Если X делится на Y без остатка. На экране появится Да, в противном случае Нет.
num1 = int(input())
num2 = int(input())
if num1%num2 == 0:
    print("Да")
else:
    print("Нет")'''

'''#Пользователь вводит число. Делится ли оно на 3, 5, 7 или нет
num = int(input())
if num%7 == 0:
    print("Делится на 7")
if num%5 == 0:
    print("Делится на 5")
if num%3 == 0:
    print("Делится на 3")
else:
    print("НЕТ")'''

'''#Напишите программу, которая вычисляет модуль числа.
num = int(input())
if num > 0:
    print(num)
if num < 0:
    print(num*-1)'''

'''#Вводится максимум 4-значное число. Сколько цифр в вашем числе?
num = int(input())
count = 0
while num > 0:
    count += 1
    num = num//10
print(count)'''

'''#Вводится 5-значный номер. Определение, является ли это плоиндромом или нет
num = int(input()) #34543
while True:
    pervoye = num//10000 #3
    vtoroye = num//1000%10 #4
    tretye = num//100%10
    chetvertoye = num//10%10 #4
    pyatoye = num%10 #3
    if pervoye == pyatoye and vtoroye == chetvertoye:
        print("Да")
    else:
        print("Нет")
    break'''

'''#Пароль сохраняется с самого начала. Пользователь вводит пароль, если пароль есть в базе если он равен паролю,
#на экране появляется --Доступ успешно завершен--, и наоборот--Отказано в доступе--.
password = 1234
while True:
    vvodit = int(input())
    if vvodit != password:
        print("Отказано в доступе")
    elif vvodit == password:
        print("Доступ завершен")
        break'''

'''#Пользователь вводит два дробных числа. Найдите сумму их целых и дробных частей.
#(Например: 1,5 и 3,2 - Целая часть дает в сумме 4, дробная часть дает в сумме 0,7)
num1 = float(input()) #1.5
num2 = float(input()) #3.2
celaya1 = num1//1 #1
celaya2 = num2//1 #3
drobnaya1 = num1-celaya1 #0.5
drobnaya2 = num2-celaya2 #0.2
print(f'сумма целых:{celaya2+celaya1},сумма дробных:{drobnaya2+drobnaya1}')'''

'''#Пользователь вводит имеющиеся у него деньги (в дробном регистре: например 15.30).
#Отображение сколько манатов и сколько копеек у пользователя. (на экране должно появиться 15 манатов 30 копеек)
dengi = float(input()) #15.30
celaya = dengi//1
drobnaya = dengi - celaya
print(f'{celaya} манат {drobnaya} копеек')'''

'''#Пользователь вводит массу в тоннах (дробное число). Вывести на экран в тоннах, килограммах, граммах.
#(Например, на экране должно появиться 126,456789 тонн, 126 тонн, 456 кг, 789 г)
num = float(input()) #125,345123
tonn = num//1 #125
kg = num-tonn #000.345123
gramm = num*1000/1000000
print(tonn,kg,gramm)'''

'''#Пользователь вводит цену блокнота, количество, которое он хочет купить, и процент скидки.
#Программа показывает, сколько AZN будет общий заказ.
cena = float(input()) #200 manat
procent = int(input()) #10 %
print(cena-(cena/100*procent))'''

'''#Пользователь вводит количество студентов, успешно сдавших экзамен, и количество «неудачников» (не сдавших экзамен).
#Напишите программу, которая вычисляет процент учащихся с задолженностью и процент успевающих учеников в классе.
vsego = int(input()) #30
student_sdav = int(input()) #20
student_nesdav = int(input()) #10
procent_sdav = 100/vsego*student_sdav
procent_nesdav = 100/vsego*student_nesdav
print(procent_nesdav,procent_sdav)'''

