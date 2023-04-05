#
'''
num_1 = int(input()) # 6
num_2 = int(input()) # 21
chislo = num_1 and num_2 <125

print(chislo)
# как только программа видит 0 она воспринимает уже значение как false
#если программа вопринмает все как false то все что справа от нее она игнорирует, выдает 0 потому что, чтоыб выдать булевое значение программа
# должна видеть and , а из-за нуля она его не видит
'''

'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
a += 10 # a = a +10 # 26
print(a)
b -= 10 # a = a - 10 # 26 - 10 =16
print(b)
c /= 10 # a = a / 10 # 16/10 = 1,6
print(c)
d *= 10 # a = a * 10 # 1,6 * 10 = 16
print(d)
e //= 10 # a = a // 10 # 16 // 10 = 1
print(e)
f **=  10 # a = a ** 10 # 1 ** 10 = 1
print(f)
f %= 10 # a = a % 10 # 1 % 10 = 1
print(f)

'''

'''
a =  round(3.2)#3
print(round(10.7))#11
print(round(511.5))#512
print(round(2.2))   # 2 - ближайшее четное
print(round(3.5))   # 4 - ближайшее четное
'''


# Practice
'''
# 1. Пользователь вводит два дробных числа. Найдите сумму их целых и дробных частей.
#(Например: 1,5 и 3,2 - Целая часть дает в сумме 4, дробная часть дает в сумме 0,7)
# celaya = 4 , 0.7
number_1 = float(input()) #1.7
number_2 = float(input()) #2.9
drobnaya_1 = number_1*10%10/10 # 1.7*10 = 17%10 = 7/10 = 0.7
drobnaya_2 = number_2*10%10/10 # 2.9 * 10 = 29%10 = 9/10 = 0.9
celaya_1 = number_1 - drobnaya_1
celaya_2 = number_2 - drobnaya_2


print(celaya_1+celaya_2 , drobnaya_1+drobnaya_2)
#celaya_1 = number_1*10//10
# #celaya_2 = number_1*10//10


#2.  Пользователь вводит имеющиеся у него деньги (в дробном регистре: например 15.30).
 #Отобразите сколько манатов и сколько копеек у пользователя. (на экране должно появиться 15 манатов 30 копеек)

    #1
valuta = float(input())
#drob = ((valuta*100)%100)/100
#manats = valuta - drob
manats= valuta//1
kopeyki = valuta - manats
print(manats, kopeyki)
'''






#if - elif - else

'''
1.

#22%2 = 0 # четное
#23%2 !=0 # не четное

number = int(input())

if number%2 == 0:
    print("четное")

else:
    print("не четное")
2.


number = int(input())

if number >= 0 or number <= 12:
    print("+")

elif number > 12 and number <= 25:
    print("grust")
elif number > 25 and number <= 50:
    print("schastye")
else :
    print("-")
'''

'''
#Practice 2.
# 2.1. Введите два числа и отобразите на экране меньшее из них

_1 = int(input())
_2 = int(input())

if _1>_2 :
    print(_2)
else:
    print(_1)

#2.2. Должен сделать калькулятор. Введите два дробных числа a и b. Показать варианты выходит
#1) а + b
#2) а – b
#3) а*b
#4) а/b

_1 = int(input())
_2 = int(input())
operation = int(input("Viberite операцию: 1. +, 2. - , 3. * , 4. /"))

if operation == 1:
    print(_1+_2)
elif operation == 2:
    print(_1-_2)
elif operation == 3:
    print(_1*_2)
elif operation == 4:
    print(_1/_2)
'''
#2.3. Вводится 5-значный номер. Определение, является ли это плоиндромом или нетнаписать программу.
