'''
number = int(input()) #58
a = number%10
b= number//10
if number>0:
    S = a + b
    if S%2==0:
        print('da', S)

    else:
        print('net', S)
elif number < 0:
    S = a - b
    if S % 2 == 0:
        print('da', S)
    else:
        print('net', S)

'''

'''
#4. Напишите программу, которая проверяет, имеет ли дробное число целую часть,
# если да, то проверяем положительное ли это число, если нет целой части
# , то проверяем является ли дробная часть положительной.
# Пример.Если введено 10.34 , здесь 10 - целая часть, 0,34 - дробная
#Если число изначально написано как 0,89 - это значит целой части нет
number = float(input())
#celaya = number//1 # 5,67686786786 // 1 =  5
celaya = int(number)
drobnaya = number - celaya
if celaya>0 or celaya<0:
    if number>0:
        print('polojitelnoye :]')
    else:
        print('otricatelnoye :[')
elif celaya == 0:
     if drobnaya>0:
         print('polojitelnoye :]')
     else:
         print('otricatelnoye :[')
'''

'''

a = int(input()) # 7 = 2* q +r при этом 0<=r<abs(b)
b = int(input()) #2

# -7//2 = -3 * 2 = -6  


if b!=0:
    c = a/b
Разделить целое число a на целое число b!=0 с остатком — это значит

найти такие два целых q и r, которые удовлетворяют следующим условиям:
(q - эквивалент , т.е то чему будет по итогу равно деление двух чисел)
(r - положительный остаток)


1) a = b * q + r; 
2) 0 <= r < |b|.

следовательно к примеру два числа 7 и 2

-7 // 2 = -4
При делении отрицательного числа на положительное, получится отрицательное число
Предположим, что правильный ответ -3, но  умножив -3 * 2 получим -6. Чтобы получить исходное
 -7  к результату прибавим число -1, но остаток не может быть отрицательным по определению(r>=0).
 По этому в данном случае остаток равен 1 и частное равно -4.

'''

'''
ключевое слово while  условие по которому будет работать цикл :
                инструкции цикла(тело цикла)
'''
'''
counter = 0
while True:
    number = int(input())

    counter += 1
    if counter == 10:
        break
        print('peyte kofe')


print('hakuna matata')


counter = 0
while counter !=10 :
    number = int(input())

    counter += 1
    print('mashina')
    if counter%2 == 0:
        continue
    print('peyte kofe')
    print(counter)
    number += counter

print('hakuna matata')
'''

# пользователь вводит числа до тех пор пока они трехзначные,
# если они не 3х-значные вывести ошибку

'''while True:
    number = int(input())
    if number >=100 and number<1000:
        print('ura chislo = ', number)
    else:        
        break

print('Obidelsya')
'''

number = 1
while number < 5:
    print(number)
    number += 1
else:
    print('Obidelsya')

# пользователь вводит числа до тех пор пока их общая сумма не больше 10,
# в ином случае вывести ошибку

# Пользователь вводит 5 чисел подряд, вывести их в обратном порядке.
# Пользователь вводит число, вычислить сумму чисел от 1 до этого числа.
# Пользователь вводит 5 чисел подряд, вывести их по возрастанию(использовать циклы)