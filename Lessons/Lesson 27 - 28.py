# Организация функций
'''
def main():
    say_hello()
    say_goodbye()
def say_hello():
    print("Hello")
def say_goodbye():
    print("Good Bye")
# Вызов функции main
main()
'''

#	Распаковка и упаковка аргументов.
'''
Распаковка 
Мы можем использовать * для распаковки списка, чтобы все его элементы можно было передавать как разные параметры.
def fun(a, b, c, d):
    print(a, b, c, d)
my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)
Упаковка 
Когда мы не знаем, сколько аргументов нужно передать функции
def mySum(*args):
    return sum(args)
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))
'''

#	Аргументы по умолчанию, аргументы-ключи.
'''
def print_person(name, age = 18):
    print(f"Name: {name}  Age: {age}")
print_person("Rafael")
#Именнованные параметры
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
print_person(age = 21, name = "Rafael")
# * -  Все параметры, которые располагаются справа от символа *, получают значения только по имени:
def print_person(name, *,  age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
print_person("Bob", age = 41, company ="Microsoft") 
'''

#	Область видимости, правило LEGB.
'''
ОБЛАСТЬ ВИДИМОСТИ
LEGB
Интерпретатор начинает поиски имени изнутри, последовательно переходя от локальной 
области видимости к объемлющей, затем к глобальной и в завершении к встроенной.
Local -> Enclosed -> Global -> Built-in
Local - inside fun-s. Удаляется, когда функция или блок кода завершают свое выполнение.
Global - free space
Enclosed - подобная область видимости относится к переменным которые созданы в функция, которые были созданы внутри других
функций lambda(частный пример)
Built-in - все встроенные по типу pi, punctuation, and etc.
'''

#	Локальные и глобальные переменные в функциях.
'''
global название переменной
n = 15
print(n)#15
def change_value():
    global n
    n+=15
    print(n)
change_value()
nonlocal 
Имена, перечисленные в инструкции nonlocal, в отличие от тех, что перечислены в инструкции global,
должны ссылаться на ранее существовавшие переменные в охватывающей области.
def football():
    x = 'Ronaldo'
    def argentina():
        nonlocal x
        x = 'Messi'
    return x
print(football())
'''

#	Функции как объекты первого класса.
'''
Это означает, что функции можно передавать и использовать в качестве аргументов, 
как и любой другой объект(string, int, float, list и т.Д.).
Особенности функций как объектов первого класса:
Функции можно присваивать переменным.
Функцию можно вернуть из функции.
У функций те же свойства и методы, что и у объектов(OOП).
Функцию можно передать в качестве аргумента при вызове другой функции.
def my_object(text):
    return text.upper()  
print(my_object("Вызов my_object"))    
upper = my_object  
print(upper("Вызов upper")) 
'''

#	Рекурсия.
''' 
#Рекурсивная функция - та функция, что вызывает саму же себя.
#Без рекурсии:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
#С ней:
#С ней:
def factorial(n):
    if n == 1:
        return 1
    else: return n * factorial(n - 1)
'''

'''
Задание 5
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
True
******
******
******
False
******
*    *
*    *
******
'''
'''length = int(input("insert length:"))
symbol = input("isnert simvol")
choice = input("insert your choice\n"
               "True/False:")
def square(length,symbol,choice):
    if choice=='True':
        for i in range(length):
            print(symbol*length)
    elif choice=='False':
        for i in range(length):
            for j in range(length):
                if i ==0 or j ==0 or i==length-1 or j==length-1:
                    print(symbol,end='')
                else:
                    print(" ",end='')
            print()
square(length,symbol,choice)'''

'''def main():
    choice = int(input('Viberite: 1. Pivet\n2. Poka'))
    if choice==1:
        say_hello()
    else:
        say_goodbye()
def say_hello():
    print("Hello")
def say_goodbye():
    print("Good Bye")
# Вызов функции main
main()
'''

'''def polka(a,b,c,d):
    return a,b,c,d
list_el = ['Shantaram','Ostrov Sokrovish','Mertviye dushi','Metro 2033']
print(polka(*list_el))'''
# unpacking
'''
def polka(a,b,c,d):
    return a,b,c,d
list_el = ['Shantaram','Ostrov Sokrovish','Mertviye dushi',12,15]
print(polka(*list_el))'''

# packing
'''
def summ_el1(*args):
    summ=0
    for i in args:
        summ+=i
    return summ
def summ_el2(*args):
    summ=0
    for i in args:
        summ+=i
    print(summ)
    print(args)
a = summ_el1(28,20,34)
print(a)
print(summ_el2(28,20,34,14,15,1213,213,12,3))
'''

'''def print_person(name, age = 18):
    print(f"Name: {name}  Age: {age}")
print_person("Rafael")
'''

# Именнованные параметры
'''def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
print_person(age = 21, name = "Rafael")'''

'''# * -  Все параметры, которые располагаются справа от символа *, получают значения только по имени:
def print_person(name, *,  age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
print_person("Bob", company ="Microsoft", age = 41)
'''
'''
count = 0
count2 = 1
import math
math.pi
def summ_el1(*args):
    summ=0
    for i in args:
        summ+=i
    def inner():
        text='Hello'
        print(text)
    inner()
    count+= 1

    return summ
print(count)
print(summ_el1(12,123,432))'''

'''
n = 15
print(n)#15
def change_value():
    global n
    n+=15
    print(n)
change_value()
print(n)#15'''

'''def football():
    x = 'Ronaldo'
    def argentina():
        nonlocal x
        x = 'Messi'

    return x
print(football())'''

'''def factorial(number):
    if number ==0 or number == 1:
        return number
    else:
        return number*factorial(number-1)
print(factorial(6))'''
