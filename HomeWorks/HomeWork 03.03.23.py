'''#1.	На вход программе подается натуральное число в двоичной(восьмеричной) системе счисления,
#написать программу которая переводит это число в десятичную систему счисления.
chislo = input("Введите число в двоичной системе:") #101011
stepen = 1
counter = 0
for i in chislo[::-1]: #101011 = 110101
    counter += int(i)*stepen # 0 = 0 + i(инт,так как со строкой нельзя производить эти действия)*на степень
    stepen *= 2
print(counter)'''
'''chislo = input("Введите число в восьмеричной системе:") #101011
stepen = 1
counter = 0
for i in chislo[::-1]: #101011 = 110101
    counter += int(i)*stepen # 0 = 0 + i(инт,так как со строкой нельзя производить эти действия)*на степень
    stepen *= 8
print(counter)'''

'''#Хотелось чтобы вы объяснили нижний код,как он работает?
n = input()
print(int(n,2))'''

'''#2.	Пользователь вводит с клавиатуры количество метров.
#В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды\
while True:
    metr = int(input())
    vibor = int(input("1 - мили, 2 - дюймы , 3 - ярды, 4 - Выход из программы"))
    if vibor == 1:
        print(metr*0.000621371)
    if vibor == 2:
        print(metr*39.3701)
    if vibor == 3:
        print(metr*1.09361)
    if vibor == 4:
        break'''

'''#3.	Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет, вывести их на экран в порядке возрастания
num1 = int(input())
num2 = int(input())
while True:
    if num1 == num2:
        print("Равны")
    if num1 > num2:
        print(num1,num2)
    else:
        print(num2,num1)
        break'''
'''#4.	Пользователь вводит с клавиатуры длину линии и символ для заполнения линии.
#Нужно отобразить на экране вертикальную линию из введенного символа, указанной длины.
#Например, если было введено 5 и символ %, тогда вывод на экран будет такой:
dlina = int(input())
simvol = input()
counter = 0
while counter <= dlina:
    counter += 1
    print('\t'*dlina,simvol)'''

'''#5.	Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись «Number is positive»,
#если меньше нуля «Number is negative», если равно нулю «Number is equal to zero».
#Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»
while True:
    num = int(input())
    if num > 0:
        print("Number is positive")
    if num < 0:
        print('Number is negative')
    if num == 0:
        print('Numer is equal to zero')
    if num == 7:
        print('Good bye!')
        break'''
#1.Есть список целых чисел, заполненный случайными числами.На основании данных этого массива нужно:
#1.1. Создать список целых чисел , содержащий только четные числа из первого списка;
#1.2 Создать список целых чисел, содержащий только нечетные числа из первого списка;
#1.3 Создать список целых, содержащий только отрицательные числа из первого списка;
#1.4 Создать список целых, содержащий только положительные числа из первого списка.
'''
list_elements = [randint(-100,100) for i in range(10)]
print(list_elements)
chetnie = [i for i in list_elements if i%2 == 0]
print(chetnie)
nechetine = [a for a in list_elements if a%2 != 0]
print(nechetine)
otricatelnie = [b for b in list_elements if b < 0]
print(otricatelnie)
polozhiteniye = [c for c in list_elements if c > 0]
print(polozhiteniye)'''

#10.	Пользователь вводит список элементов, определить количество одинаковых соседних элементов списка.
'''stroka = input()
counter = 0
for i in range(0,len(stroka)):
    if stroka[i] == stroka[i+1]:
        counter += 1
    print(counter)'''
from random import randint
#11.	Пользователь вводит список заполненный случайными числами, определить сколько раз
#в списке встречаются одинаковые элементы и под какими индексами они находятся.

'''spisok = [randint(1,30) for a in range(10)]
counter = 0
for i in range(len(spisok)):
    for a in range(i+1, len(spisok)):
        if spisok[i] == spisok[a]:
            counter += 1
print(spisok)
print(counter)
'''
#12.	Вывести на экран фигуры, заполненные звездочками:
#1.	Квадрат
#2.	Треугольник
#3.	Прямоугольный треугольник
#4.	Перевернутый треугольник
#Задание 1
'''a = int(input())
counter = a
while counter > 0:
    counter -=1
    print('*  '*a)'''
#Сделал второй способ первой задачи,так как в условии сказано нарисовать квадрат,но в результате не похоже на квадрат,даже если стороны равны
'''a = 10
counter = 4
while counter != 0:
    counter -= 1
    print('*'*a)'''
#Задание 2
'''h=4 # Высота
for i in range(h): # 0,1,2,3
    print(' '*(h-1-i) + '* '*(i+1))'''
#Задание 3
'''chislo = 1
katet = int(input('Нижний катет:'))
while chislo != katet:
    print('* '*chislo)
    chislo+=1'''
#Задание 4
'''n = 1
counter = 6
while counter > 0:
    print(' '* (n-1) + '* ' * (1+counter))
    counter -= 1
    n += 1
print(' '*6 + '*')'''

