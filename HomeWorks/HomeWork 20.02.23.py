'''#1.	Напишите программу, которая запрашивает два целых числа x и y,
#после чего вычисляет и выводит значение x в степени y.
x = int(input("Введите начало"))
y = int(input("Введите конец"))
for i in range(x , y+1):
    print (i**y)'''


'''#2.	Пользователь вводит с клавиатуры два числа.
#Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне,
#а также среднеарифметическое каждой группы.
nachalo = int(input())
konec = int(input())
summ_chet = 0
summ_nechet = 0
summ9 = 0
counter = 0
for i in range(nachalo , konec+1):
    if i%2 == 0:
        summ_chet += i
        counter += 1
        sredne_chet = summ_chet/counter
    if i%2 != 0:
        summ_nechet += i
        counter += 1
        sredne_nechet = summ_nechet/counter
    if i%9 == 0:
        summ9 += i
        counter += 1
        sredne_9 = summ9/counter

print("Сумма четных чисел:", summ_chet)
print("Сумма нечетных чисел:", summ_nechet)
print("Сумма кратных 9:", summ9)
print("Среднеарифметическое четных чисел", sredne_chet)
print("Среднеарифметическое нечетных чисел", sredne_nechet)
print("Среднеарифметическое 9 кратных", sredne_9)'''


'''#3.	Сделать калькулятор способный вычислять *,/,+,- с любыми входными данными
while True:
    operator = int(input("Выберите операцию: 1 * , 2 / , 3 + , 4 -"))
    number = float(input("Введите первое число"))
    number2 = float(input("Введите число на которое будет произведено действие"))
    if operator ==1:
        print(number*number2)
    elif operator ==2:
        print(number/number2)
    elif operator ==3:
        print(number+number2)
    elif operator ==4:
        print(number-number2)'''


'''#4.	Сделать конвертор валют(Минимум 3 валют)
while True:
    manat = float(input("Выберите валюту: 1 Манат -> Доллар, 2 Манат -> Рубль , 3 -> Следующая страница:"))
    dollar = float(input("Выберите валюту: 4 Доллар -> Манат, 5 Доллар -> Рубль , 6 -> Следующая страница:"))
    rub = float(input("Выберите валюту: 7 Рубль -> Доллар, 8 Рубль -> Манат , 9 -> Готово:"))
    number = float(input("Введите число"))
    if manat == 1:
        print(number*0.59, " dollar")
    elif manat == 2:
        print(number*43.63, " rub")
    if dollar == 4:
        print(number*1.70, " manat")
    elif dollar == 5:
        print(number*74.01, " rub")
    if rub == 7:
        print(number*0.014, " dollar")
    elif rub == 8:
        print(number*0.023, " manat")
    elif rub == 9:
        print("Готово")'''

'''#5.	Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть три одинаковые цифры.
counter = 0
for i in range(100,1000):
    pervaya = i//100 #534 5
    vtoraya = i//10%10 #534 3
    tretya = i%10 #534 4
    if pervaya == vtoraya and pervaya == tretya and vtoraya == tretya:
        counter +=1
print(counter)'''