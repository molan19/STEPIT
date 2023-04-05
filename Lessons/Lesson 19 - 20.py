#List methods
'''
#https://pythontutor.com/visualize.html#mode=display
append(item): добавляет элемент item в конец списка
insert(index, item): добавляет элемент item в список по индексу index
extend(items): добавляет набор элементов items в конец списка
remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
clear(): удаление всех элементов из списка
index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
pop(index): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
count(item): возвращает количество вхождений элемента item в список
sort(reverse = False,key): сортирует элементы.
Optional. reverse=True отсортирует в обратном порядке. По умолчанию reverse=False(по возростаниө)
Optional. key - функцию сортировки.
people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
people.sort()
people = ["Tom", "Alina", "bob", "alice", "Sam", "Bill" ]
people.sort(key=str.lower)
reverse(): расставляет все элементы в списке в обратном порядке
min()
max()
copy(): копирует список
'''


# List Comprehension - генератор списков
'''
newlist = [expression for item in iterable (if condition)]
Синтаксис list comprehension состоит из следующих компонентов:
iterable: перебираемый источник данных, в качестве которого может выступать список,
 множество, последовательность, либо  функция,
 которая возвращает набор данных, например, range()
item: извлекаемый из источника данных элемент
expression: выражение, которое возвращает некоторое значение. Это значение  попадает в список
condition: условие, которому должны соответствовать извлекаемые из источника данных элементы.
numbers = [-3, -2, -1, 0, 1, 2, 3]
#1 
positive_numbers = [n for n in numbers if n > 0]
#2 
numbers = [n for n in range(10)]
#3
new_numbers = [ n * 2 if n > 0 else n for n in numbers]
#1
print(positive_numbers)
#2
print(numbers)
#3
print(new_numbers)      
'''



'''
list_elements = []
count = 0
while True:
    n = input()
    list_elements.append(n)
    print(list_elements)
    count+=1
    if count==10:
        break
        '''

'''
list_elements = [1,3,545,999,123,12344]
print(list_elements)
for i in range(1,11):
    item = input()
    index = int(input())
    list_elements.insert(index,item)
    '''
'''
list_elements = [1,3,545,999,123,545,1,1,12344]
list_elements2 = ['hello', True, False,12, 14.5]
list_elements.extend(list_elements2)
print(list_elements)
#list_elements.clear()
list_elements.remove(int(input()))
print(list_elements)
'''
'''
list_elements = [1,3,545,999,123,545,16,1,12344]
print(list_elements.index(16))
'''
'''
list_elements = [1,3,545,999,123,545,16,1,'Hello']
print(list_elements)
item = list_elements.pop()
item2 = list_elements.pop(5)
print(list_elements)
print(item)
print(item2)
'''
'''list_elements = [1,3,1,999,123,1,16,1,'Hello']
print(list_elements.count("Hello"))
'''
'''
list_elements = [1,3,1,999,123,1,16,1]
list_elements.sort()
print(list_elements)
'''
'''people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
people.sort()
print(people)
people = ["Tom", "Alina", "bob", "alice", "Sam", "Bill" ]
people.sort(key=str.lower)
print(people)'''


'''
people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
list_elements = [1,3,1,999,123,1,16,1]
people.sort()
print(people)
print(max(people))
print(max(list_elements))
print(min(people))
print(min(list_elements))
'''
'''
list_elements = people.copy()
print(list_elements)
'''


#Practise:

#Напишите программу на Python для удаления дубликатов из списка.
#Напишите программу на Python, чтобы проверить, пустой список или нет
#Напишите программу на Python, чтобы найти список слов, длина которых превышает n, из заданного списка слов
#Напишите программу Python, которая возвращает True, если у двух спсиков есть хотя бы один общий элемент.
#Напишите программу на Python для печати указанного списка после удаления 0-го, 4-го и 5-го элементов
'''list_items = [ 1,2,3,4,4,4,4,4,4,5,4,7,4,9,11,123,4]
print(list_items)
list_items_2 = list_items.copy()
duplicate = int(input())
for i in range(0,len(list_items)-1):
    if list_items[i] == duplicate:
        list_items_2.remove(duplicate)
        print(list_items_2)
'''

'''
list_items = [1,2,3,4,5]
list_items_2 = []
if list_items !=list_items_2:
    print("ne pustoy")
else: print('pustoy')'''


list_elements = [1,5,7,8,-16,-24,10,12,13,15]
summ=0
list_items = [ items for items in list_elements if items%2 == 0]
print(list_items)
list_items = [ 1,2,3,4,4,4,4,4,4,5,4,7,4,9,11,123,4]
print(list_items)
duplicate = int(input())
list_items_2 = [ list_items[items].remove(duplicate) for items in list_items if list_items[items]==duplicate]