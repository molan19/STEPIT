'''
#Пользователь вводит 5 чисел подряд, вывести их в обратном порядке
a = 0
b = 0
c = 0
d = 0
e = 0
counter = 0
number = 0
while counter != 5:
    counter += 1
    number = int(input())
    if counter == 1:
        a = number
    elif counter == 2:
        b = number
    elif counter == 3:
        c = number
    elif counter == 4:
        d = number
    elif counter ==5:
        e = number
print(e , d , c ,  b , a)
'''

'''
#Пользователь вводит число, вычислить сумму чисел от 1 до этого числа.
# 3 = 1+2+3
n = int(input())
i = 1
s = 0
while i <= n:
    s = i+s
    i += 1
    print("Сумма =", s)
'''
'''
#Пользователь вводит 3(5) чисел подряд, вывести их по возрастанию(использовать циклы)
a = 0
b = 0
c = 0
counter = 0
number = 0
while counter != 3:
    counter += 1
    number = int(input())
    if counter == 1:
        a = number
    elif counter == 2:
        b = number
    elif counter == 3:
        c = number
if a > b > c:
    print(a , b , c)
elif a > c > b:
    print(a , c , b)
elif b > a > c:
    print(b , a , c)
elif b > c > a:
    print(b , c , a)
elif c > a > b:
    print(c, a, b)
elif c > b > a:
    print(с , b , a)
'''
'''
#пользователь вводит числа до тех пор пока их общая сумма не больше 10, в ином случае вывести ошибку
summa =0
while True:
    number = int(input())
    summa += number
    if summa <=10:
        print(number)
    else:
        break
'''