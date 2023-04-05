'''#Пользователь вводит с клавиатуры строку.
# Произведите поворот строк и полученный результат выведите на экран.
stroka = input()
for i in range(-1, -len(stroka)-1 , -1):
    print(stroka[i])'''

'''#Пользователь вводит с клавиатуры строку. Посчи-
#тайте количество букв, цифр в строке. Выведите оба количества на экран
#Не было идей,поэтому нашел в интернете про функции isalpha и isdigit
stroka = '"коав13р43о21о44331'
bukvi = 0
cifri = 0
for i in stroka:
    if i.isalpha():
        bukvi += 1
    elif i.isdigit():
        cifri += 1
print(bukvi)
print(cifri)'''


'''#Пользователь вводит с клавиатуры строку и символ
#для поиска. Посчитайте сколько раз в строке встречается
#искомый символ. Полученное число выведите на экран.
stroka = input()
simvol = 0
iskomiy = input()
for i in stroka:
    if i == iskomiy:
        simvol += 1
print(simvol)'''

'''#Пользователь вводит с клавиатуры строку и слово
#для поиска. Посчитайте сколько раз в строке встречается
#искомый символ. Полученное число выведите на экран.
stroka = input()
slovo = 0
iskomoye_slovo = input()
words = stroka.split(' ')
for i in words:
    if i == iskomoye_slovo:
        slovo += 1
        print(slovo)'''



'''# Пользователь вводит с клавиатуры строку, слово для
#поиска, слово для замены. Произведите в строке замену
#одного слова на другое. Полученную строку отобразите на экране.
stroka = "Hello, World!"
poisk = "World"
zamena = "Human"
print(stroka.replace(poisk , zamena))'''

