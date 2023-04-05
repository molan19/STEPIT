'''chislo = int(input())
while chislo > 0:
    print('*'*chislo)
    chislo -= 1'''
'''#Реализовать игру с игральными костями.
#У игральных костей 6 сторон, в игре есть два игрока, при броске каждому из них выпадает рандомное значение,
#тот у кого выпал наибольший результат зарабатывает 1 бал, как только один из игроков
#набрал 3 балла в общей сумме то он побеждает.
from random import randint
player_1 = [randint(0,10)
player_2 = randint(0,10)
print(player_1,player_2)'''
'''from random import randint
list_elements = [[randint(1,11 for j in range)]]'''
'''book_shelf = [['Остров сокровищ','Стивенсон,','423',8.6,1950], # создали вручную вложенные списки
              ['Мцыри','Лермонтов','423',8.6,1840],
              ['Шантарам','Без понятия','653',8.9,2021]]'''
'''n = int(input())
m = int(input())
for i in range(0,n):
    for j in range(0,m):
        print(book_shelf[i][j],end=' ')
    print('____''\n')'''
'''list_elements = [[1,2,3],
                [4,5,6]]
for i in range(2):
    for j in range(2):
        list_elements[i].append(int(input()))
        print(list_elements[i][j],end=' ')
    print('____''\n')'''
from random import randint
'''list_el = [randint(1,10) for j in range(0,11)]for i in range(0,11)]
summ = 0
for i in range(len(list_el)):
    for j in range(list_el[i]):
        summ += list_el[i][j]
        print(list_el[i[j]],end= ' ')
    print()'''
'''n,m = int(input()), int(input())
list_el = [randint(1,100) for j in range(m)]for i in range(n)] #создаем списки в генераторе'''
'''summ = 0
for i in range(len(list_el)): #расписываем матрицу
    for j in range(list_el[i]):
        summ += list_el[i][j]
        print(list_el[i[j]],end= ' ')
    print()'''
#   1.1. Найти сумму элементов всех его чисел.#
#   1.2. Найти сумму всех положительных.#
#   1.3. Найти сумму всех отрицательных.#
#   1.4. Найти сумму всех четных.#
#   1.5. Найти сумму всех не четных.#
#   1.6. Найти сумму всех простых чисел#
#   1.7. Определить количество простых чисел в списке.
m,n = int(input()), int(input())
list_el = [[randint(0,10) for j in range(n) ]for i in range(m)]
summ = 0
otric = 0
chet = 0
nechet = 0
for i in range(m):
    for j in range(n):
        if list_el[i][j] < 0:
            summ += list_el[i][j]
        if list_el[i][j]%2 == 0:
            chet += list_el[i][j]
        if list_el[i][j]%2 != 0:
            nechet += list_el[i][j]
    print(f'сумма положительных{summ}сумма четных{chet} сумма нечетных {nechet}')

