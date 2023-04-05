'''

Kонструкция for. Этот цикл пробегается по набору значений, помещает каждое значение в переменную,
и затем в цикле мы можем с этой переменной производить различные действия

for переменная in набор_значений:
    инструкции





#else
message = "Hello"
for c in message:
    print(c)
else:
    print("Последний символ: ",c, " Цикл завершен")


i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
'''

'''
range(start, end, steps)
'''

'''for number in range(7, 11):
    print(number)

for i in range(1, 11):  # i prinimayet znaheniya ot 1 do 11 , etot otrabativayet 10 raz
    for j in range(1, 11):  # j toje prinimayet ot 1 do 11, etot rabotaet vsrgo 100
        print(i * j, end="\t")
    print("\n")
'''

'''
range_1 = int(input('write the start of the range'))
range_2 = int(input('write the end of the range'))
for number in range(range_2,range_1-1, -1):
    print(number)

print('_'*100)
range_3 = int(input('write the start of the range'))
range_4 = int(input('write the end of the range'))

for number in range (range_3, range_4+1):
    print(number)
'''

# PRAKTIKA
# 1. vivesti chetniye chisla v diapazone ot 1 - 100

'''#1 
for number in range(2,100,2):
    print(number)
#2
for number in range(1,100):
    if number%2==0:
        print(number)'''

'''#2. Показать таблицу умножения для числа, введенного
#пользователем. Например, если пользователь вводит
#число 7, нужно показать:
#7 * 1 = 7
#7 * 2 = 14
#7 * 3 = 2

number = int(input())
for i in range(1,10):
    i*=number
    print(number)'''

'''
#3.Пользователь вводит с клавиатуры два числа. Нужно
#посчитать сумму чисел в указанном диапазоне, а также
#среднеарифметическое

number_1 = int(input('Start of range: '))
number_2 = int(input('End of range: '))
summ=0
counter = 0
for i in range(number_1,number_2):
    summ+=i
    print(summ)
    counter+=1
else:
    print('Sredne arifm =',summ/counter)
'''
# Пользователь указывает курс одной из валют как постоянную,
# и постоянно вводит манаты, нужно, чтобы манаты переводились в доллары