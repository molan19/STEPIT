'''ASCII - Так как первые вычислительные машины были малоемкими,
для представления в их памяти всего набора требуемых знаков хватало 7 бит (или 128 символов).
 Сюда входил весь английский алфавит в верхнем и нижнем регистрах, цифры, знаки, вспомогательные символы.


 import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

Основная беда: имея 128 вариантов обозначить символ, мы никак не сумеем внедрить туда буквы других языков.
 В частности, какой-нибудь символ под номером 201 в кириллице даст совсем не русскую букву, если отослать его в Румынию.

UNICODE – связь символа и определенного числа без возможного повторения.
 Если мы кого-то попросим показать символ, скрытый под номером «1000», то в любой точке планеты он будет одним и тем же графическим элементом.
 \

 UTF 8 - UTF-8 – кодировка символов юникод в двоичном виде. Использует от 1 до 4 байт.
 Так как наиболее часто используемые символы занимают 1 байт (в частности, аски-символы),
 то UTF-8 оптимальна для английского текста, но не для азиатского.
'''


'''
Строки - неизменяемый тип данных

string = "hello world"
c0 = string[0]  # h

string = "hello world"
string[1] = "



получение подстроки:

string[:end]: начиная с 0-го индекса по индекс end

string[start:end]:  начиная с индекса start по индекс end 

string[start:end:step]: начиная с индекса start по индекс end через шаг step




Эскейп последовательность
Сырые строки

path = "C:\python\name.txt"
print(path)

path = r"C:\python\name.txt"
print(path)

Функции строк

lower()
upper()
 len():
print(ord("A"))  # 65 -Unicode
'''

'''import random # Импортируй все абсолютно что есть в модуле рандом мой проект

from random import randint # из модуля рандом импортируйте функцию рандинт

for i in range(1,10):
    print(randint(1,100))
'''


'''
line = 'hello'
Line = "Hello World"

print(line[0])
print(line[-1])

print(Line)
print(line)

line[3]= 'R' # oshibka, simvol v stroke izmenit nelza
'''




'''#string[:end] #начиная с 0-го индекса по индекс end( энд не включительно)

#string[start:end] #  начиная с индекса start по индекс end( энд не включительно)

#string[start:end:step] # начиная с индекса start по индекс end через шаг step( энд не включительно)

string = 'TEXNOLOGII'

print(string[2:105])
'''


#Операции со строками:

'''string_1 = 'oboi'
string_2 = 'krichat'

print(string_1+string_2)
print(string_1*7)'''

'''_1 = 'aa'
_2 =  'Aaa1'
_3 =  '1a'
_4 = 'AaaA'
_5 = '/a'
print(_1>_2) #false
print(_2>_4)
print(_1>_5) #false'''
'''print(_1>_3)#false
print(_2>_3)#false
'''
'''text = 'segodnya chudniy den'
podstroka = 'd'

#print(podstroka in text)

count = 0
while podstroka in text:
    count+=1
    print(count)
    if count == 3:
        break
'''


'''string = "Hakuna matata"
for char in range(0,13):
    print(string[char]) #string[0],string[1]....string[9]
'''
#Пользователь вводит с клавиатуры строку.
# Переверните строку и полученный результат выведите
#на экран.

'''string = input('Vvedi stroku chelovek:') # hello
for char in range(-1,-len(string)-1,-1): # len() - opredelyaet dlinu stroki (-1 do -6)
    print(string[char],end = '')'''

a = "Hello, World!"
print(a.replace("World", "a"))