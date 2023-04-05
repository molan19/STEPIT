'''list_elements = []
for i in range(1,10):
    list_elements.append(i) #ставит любой элемент в конец списка
    print(list_elements)

list_elements =  [1,3,4,2,321]
n = input()
index = int(input())
list_elements.insert(index, n) #ставит любой элемент перед заданным индексом
print(list_elements)

list_elements =  [1,3,4,2,321]
list_elements2 =  ['hello',True,False,12,14.5]
list_elements.extend(list_elements2) #Добавляет целый список в конец нашего списка
print(list_elements)

list_elements =  [1,3,4,2,321]
list_elements2 =  ['hello',True,False,12,14.5]
list_elements.clear() #Удаляет все элементы списка
print(list_elements)


list_elements.remove(3)
print(list_elements) #Удаляет определенный элемент из списка

list_elements =  [1,3,4,2,321]
print(list_elements.index(16)) #Выводит номер индекса заданного элемента

print(list_elements.pop) #Удаляет элемент по номеру индекса и выводит его,если оставить пустым,то удалит последний элемент

list_elements =  [1,3,4,2,321]
print(list_elements.count(1)) #Считает количество элементов,которое мы указали

list_elements =  [1,3,4,2,321]
list_elements.sort(reverse = True) #Сортирует список,по возрастанию или уменьшению
print(list_elements)

people = ["Tom","Bob","Alice","Nurlan","Bill","Sam"]
people.sort() #По возрастанию алфавита,A,B,C,D
print(people)
max(people) #Выводит максимальный элемент
min(people) #Выводит максимальный элемент

list_elements = people.copy() #Копирует список
print(list_elements)'''

#Напишите программу на Python для удаления дубликатов из списка. +
# #Напишите программу на Python, чтобы проверить, пустой список или нет +
# #Напишите программу на Python, чтобы найти список слов, + длина которых превышает n, из заданного списка слов +
# #Напишите функцию Python, которая принимает два списка и возвращает True, если у них есть хотя бы один общий член. +
# #Напишите программу на Python для печати указанного списка после удаления 0-го, 4-го и 5-го элементов

'''spisok = [1,2,3,5,6]
spisok_2 = []
if spisok != spisok_2:
    print("Не пустой")
else:
    print("Пустой")'''

'''spisok = ["кит","томат", "ошибка","ток","посуда"]
slovo = 'лол'
for i in spisok:
    if len(i) != len(slovo):
        print(i)'''

'''spisok = [1,4,3,5,2,3,8,12,3]
duplicate = int(input())
for i in spisok:
    if i == duplicate:
        spisok.remove(duplicate)
        print(spisok)'''

'''spisok1 = [1,2,4,5,7]
spisok2 = [12,34,31,2,6]
for i in spisok1:
    for n in spisok2:
        if i == n:
            print(True)
        else:
            print(False)'''

'''spisok = [1,3,53,12,53,64,1,2,4,53]
print(spisok.pop(0), spisok.pop(3), spisok.pop(3))
print(spisok)
'''
