'''def summ_el(num_1,num_2): #Внутри скобки параметр функции
    summ = num_1+num_2
    print(summ)

summ_el(10,15)'''
#1.Напишите функцию, которая принимает два числа в качестве параметра и отображает все нечетные числа между ними.
#2.Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
#Функция принимает в качестве параметров: длину линии, направление, символ.
#3. Напишите функцию, которая возвращает максимальное из четырёх чисел.  Числа передаются в качестве параметров.
#4. Напишите функцию, которая возвращает сумму чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров.
'''def summ(num1,num2):
    for i in range(num1,num2):
        if i%2 != 0:
            print(i)
summ(1,50)           '''

'''def liniya(dlina,napravleniye,simvol):

    if napravleniye == 1:
        print(dlina*simvol)
    if napravleniye == 2:
        for i in range(dlina):
            print(simvol)

liniya(5,int(input('1 - Горизонтальная линия, 2 - Вертикальная линия')),input())'''

'''def maximal(num1,num2,num3,num4):
    while True:
        if num1 > num2 and num1 > num3 and num1 > num4:
            print(num1)
        if num2 > num1 and num2 > num3 and num2 > num4:
            print(num2)
        if num3 > num1 and num3 > num2 and num3 > num4:
            print(num3)
        if num4 > num1 and num4 > num2 and num4 > num3:
            print(num4)
            break
maximal(12,54,14,67)'''

'''def summ1(num1,num2):
    summ = 0
    for i in range(num1,num2+1):
        summ += i
        print(summ)
summ1(1,3)'''



