
'''#Вводится диапозон чисел, определяется есть ли в данном диапозоне числа Армстронга
# (числом Армстронга называется такое число сумма своих цифр,
# возведенных в кубе, которых равно самому этому число )
#153 = 1**3 + 5**3+3**3
nachalo_diapazona = int(input()) # 2
konec_diapazona = int(input()) #400

for i in range(nachalo_diapazona,konec_diapazona): #2536
    poslednya = i%10
    tretya = i//10%10
    vtoraya = i//100%10
    pervaya = i//1000
    if poslednya**3 + tretya**3 + vtoraya**3 + pervaya**3 == i:
        print(i)'''




'''#Пользователь вводит диапозон чисел, вывести таблицу возведения каждого этого числа в степень от 1 до 3 ,
# и sdelayte tak, chtobi bralas stepen lish u chetnix chisel
n1 = int(input())
n2 = int(input())
for i in range(n1, n2):
    if i%2 == 0:
        for j in range(1 ,3+1):
            print(i**j, end="\t")
        print("\n")'''

'''#Пользователь вводит с клавиатуры два числа (нача-ло и конец диапазона).
# Требуется проанализировать всечисла в этом диапазоне по следующему правилу:
# если xисло кратно 7, его надо выводить на экран.
nachalo = int(input("Первое число: "))
konec = int(input("Второе число: "))
i = 0
while nachalo <= konec:
    while i <= konec:
        i += 1
        if i%7==0:

            print(i)'''

'''#Пользователь вводит с клавиатуры два числа (нача-ло и конец диапазона).
# Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
#1. Все числа диапазона;
#2. Все числа диапазона в убывающем порядке;
#3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.
nachalo = int(input("Первое число"))
konec = int(input("Второе число"))
counter = 0
for i in range(nachalo,konec+1):
    print(i)
print("_"*50)
for i in range(konec,nachalo-1, -1):
    print(i)
print("_"*50)
for i in range(nachalo, konec + 1):
    #counter += 1
    if i%7==0:
        print(i)
    #if counter%5 == 0:
        #print(counter)
#Сделал,но не понимаю как вывести количество чисел кратных 5,ввел counter,но вроде не выводит как нужно
'''
'''#Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все числа
#в этом диапазоне. Вывод на экран должен проходить по правилам, указанным ниже.
#Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz.
#Если число кратно 3 и 5 нужно вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число.
a = int(input())
b = int(input())
for i in range(a , b+1):
    if i%5 == 0 and i%3 == 0:
        print(i, "Fizz Buzz")
    elif i%5 == 0:
        print(i, "Buzz")
    elif i%3 == 0:
        print(i , "Fizz")
    elif i%5 != 0 and i%3 != 0:
        print(i)'''