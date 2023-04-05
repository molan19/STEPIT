'''list_element_1 = [2,2.3,True,'Tom',3,4,5]  #можно также инпут
list_element_2 = list([1,2,3,4,5])
print(list_element_1[3])
print(list_element_1)'''

'''stroka = ['Hello'] #Выведет слово целиком
print(stroka)
letters = list("Hello") #Выведет по буквам
print(letters)
letter1 = list(["Hello"]) #Выведет слово целиком'''

'''people = ["Tom", True, 2]
tom, bob, sam = people #том выводит Tom, bob выводит True, sam выводит 2"
print(tom,bob,sam)'''

'''list_element_1 = [2,2.3,True,'Tom',3,4,5]
for i in range(0,len(list_element_1)):
    print(list_element_1[i], end= ' ')
i = 0
while i < len(list_element_1):
    print(f"\n{list_element_1[i]}")
    i += 1'''

'''list1 = [1,2,3]
list2 = [1,2,3]
if list1 == list2:
    print("Равны")
else:
    print("Не равны")
    
list1 = [1,2,3]
list2 = [1,2,3]
if list1 > list2:
    print("Больше")
else:
    print("Меньше")'''


from random import randint
'''spisok = [randint(1,100),randint(1,100),randint(1,100)]
spisok_summ = 0
for i in range(0,len(spisok)):
    if spisok[i] > 0:
        spisok_summ += spisok[i]
        print(spisok_summ)
'''
'''spisok_1 = [randint(-100,1),randint(-100,1),randint(-100,1)]
spisok_raznost = 0
for i in range(0,len(spisok_1)):
    if spisok_1[i] < 0:
        spisok_raznost += spisok_1[i]
        print(spisok_raznost)'''


'''spisok_1 = [randint(1,100),randint(1,100),randint(1,100)]
spisok_summ = 0
for i in range(0,len(spisok_1)):
    if spisok_1[i]%2 == 0:
        spisok_summ += spisok_1[i]
        print(spisok_summ)'''

'''spisok_1 = [randint(1,100),randint(1,100),randint(1,100)]
spisok_summ = 0
for i in range(0,len(spisok_1)):
    if spisok_1[i]%2 != 0:
        spisok_summ += spisok_1[i]
        print(spisok_summ)
'''
'''#Произведение чисел кратные 3
spisok_1 = [randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50)]
spisok_proiz = 1
for i in range(0,len(spisok_1)):
    if spisok_1[i]%3 == 0:
        spisok_proiz *= spisok_1[i]
        print(f'числа {spisok_1[i]}')
print(f'произведение чисел: {spisok_proiz}')'''

