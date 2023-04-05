from random import randint
#Сумма положительных,отрицательных,минимальный,максимальный элементы,количество нулей
'''m,n = int(input()), int(input())
list_el = [[randint(-10,10) for j in range(n)]for i in range(m)]
summ = 0
otric = 0
null = 0
maxim = 0
mini = 100
print(list_el)
for i in range(m):
    for j in range(n):
        if list_el[i][j] > 0:
            summ += list_el[i][j]
        if list_el[i][j] < 0:
            otric += list_el[i][j]
        if list_el[i][j] == 0:
            null += 1
        if list_el[i][j] > maxim:
            maxim = list_el[i][j]
        if list_el[i][j] < mini:
            mini = list_el[i][j]

print(f'сумма положительных {summ}\nсумма отрицательных {otric}\nколичество нулей {null}максимальный элемент {maxim}\n минимальный элемент {mini}')'''
#   1.2. Найти сумму всех положительных.#
#   1.3. Найти сумму всех отрицательных.#
#   1.4. Найти сумму всех четных.#
#   1.5. Найти сумму всех не четных.#
#   1.6. Найти сумму всех простых чисел#
#   1.7. Определить количество простых чисел в списке.
'''m,n = int(input()), int(input())
list_el = [[randint(-100,100) for j in range(n)]for i in range(m)]
prime_num = []
print(list_el)
summ = 0
otric = 0
counter = 0
chet = 0
nechet = 0
for i in range(m):
    for j in range(n):
        if list_el[i][j] > 0:
            summ += list_el[i][j]
        if list_el[i][j] < 0:
            otric += list_el[i][j]
        if list_el[i][j]%2 == 0:
            chet += list_el[i][j]
        if list_el[i][j]%2 != 0:
            nechet += list_el[i][j]
print(f'сумма положительных {summ}\nсумма отрицательных {otric}\nсумма четных {chet}\nсумма нечетных {nechet}')
prime_num = []
for sublist in list_el:
    for number in sublist:
        is_prime = True
        if number > 1:
            for a in range(2,number):
                if number%a == 0:
                    is_prime = False
                    break
            if is_prime:
                counter+= 1
                prime_num.append((number))
    print(prime_num,counter)'''
