# Nested List
'''
list1 = ['Person 1','Surname 1', 20, 'Aze']
list2 = ['Person 2','Surname 2', 30, 'USA']
overall = [list1,list2]
print(overall)
'''

'''Students_data = [['Name 1','Surname 1','20 years old'],
                ['Name 2','Surname 2','40 years old'],
                ['Name 3','Surname 3','50 years old']]
for i in range(len(Students_data)):
    for j in range(len(Students_data[i])):
        Students_data[1].append(4)
        print(Students_data[i][j], end=' ')
    print()
'''
# Заполнение вложенного списка рандомными числами:

'''
#1 способ:
m, n = 3, 4  # размерность списка
lst = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 10))
    lst.append(row)
#2 способ:
lst = [[random.randint(1, 10) for j in range(n)] for i in range(m)]
'''

# Practise:
# 1.Вводится двумерный список(список внутри которого еще один список) размера m на n. Его значения заполнены случайными числами.
#   1.1. Найти сумму элементов всех его чисел.
#   1.2. Найти сумму всех положительных.
#   1.3. Найти сумму всех отрицательных.
#   1.4. Найти сумму всех четных.
#   1.5. Найти сумму всех не четных.
#   1.6. Найти сумму всех простых чисел
#   1.7. Определить количество простых чисел в списке.

            # 1 -Book name,  2 - author , 3 -pages, 4-rate
'''book_shelf = [['Остров сокровищ','Stevenson',423,8.3,1950],
              ['Mciri','Lermontov',151,9.1, 1840],
              ['Shantaram', 'Ne znayem',578,8.9,2012 ],
              ['Metro 2033','Gluxovsky',364,9.4,2009]]'''

'''
book_1= ['Остров сокровищ','Stevenson',423,8.3]
book_2 = ['Metro 2033','Gkuxovsky',364,9.4]
List_books=[book_1,book_2]
print(List_books)
'''

'''
list = list(map(list, input().split()))
print(list)
'''

'''import random
summ = 0
n,m = int(input('Enter rows: ')),int(input('Enter columns: '))
list_el = [[random.randint(-100,100) for j in range(m)] for i in range(n)]
for i in range(len(list_el)):
    for j in range(len(list_el[i])):
        summ+=list_el[i][j]
        print(list_el[i][j],end = ' ')
    print('\n_____________')
print(f'Summ of list elements{summ}')
'''

'''n,m = int(input('Enter rows')),int(input('Enter columns'))
for i in range(0,n):# 4
    for j in range(m): #20
        print(book_shelf[i][j], end= ' ')# i =0 , j =0,1,2,3,4; i=1,j = 0,1,2,3,4
    print('\n______________')'''

'''list_el = [[1,2,3],
           [5,6,7]]
for i in range(0,len(list_el)):#0
    for j in range(len(list_el[i])):# 0
        list_el[1].append(333)
        print(list_el[i][j],end = ' ')
    print()
'''
'''m, n = 3, 4  # размерность списка
import random
lst = []
for i in range(m):# 0 - 3
    row = []
    for j in range(n): # 0 - 4
        row.append(random.randint(1, 10))
    lst.append(row)
list_el = [[random.randint(-100,100) for j in range(m)] for i in range(n)]'''

from random import randint
m,n = int(input()),int(input())
list_elements = [[randint(-100,100) for j in range(n)] for i in range(m)]
summ = 0

for i in range(0,len(list_elements)):#0
    for j in range(len(list_elements[i])):# 0

        print(list_elements[i][j],end = ' ')
    print()

for i in range(m):# 0,1
    for j in range(n):#for j in range(i):
        if list_elements[i][j]>=0:
            summ += list_elements[i][j]
print(summ)


'''
list_el = [[1,2],[3,4]]
list_el.append([7,8])
print(list_el)
'''