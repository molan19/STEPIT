'''
isalpha(): возвращает True, если строка состоит только из алфавитных символов
islower(): возвращает True, если строка состоит только из символов в нижнем регистре
isupper(): возвращает True, если все символы строки в верхнем регистр
isdigit(): возвращает True, если все символы строки - цифры

lower(): переводит строку в нижний регистр
upper(): переводит строку в вехний регистр
title(): начальные символы всех слов в строке переводятся в верхний регистр
capitalize(): переводит в верхний регистр первую букву только самого первого слова строки

lstrip(): удаляет начальные пробелы из строки
rstrip(): удаляет конечные пробелы из строки
strip(): удаляет начальные и конечные пробелы из строки

find(): возвращает индекс подстроки в строке. Если подстрока не найдена, возвращается число -1
replace(): заменяет в строке одну подстроку на другую
split(): разбивает строку на подстроки в зависимости от разделителя
join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель
len(): определяет длину строки.
'''

# Escape sequences :
'''
\n - perexod na novuyu stroku
\t - ставит табуляцию в строке после себя
\b - удаляет символ до себя
\\ - выводит \
\' - выводит '
\" - выводит "
'''
'''print('hello\nworld')
print('hello\n\tworld')
print('hochu  \bhinkali')
print("\"Мертвые души\"")
print('\'Мертвые души\'')
print('\\Мертвые души\\')
'''

'''
#Сырые строки
# r"" - ключевая буква позволяющая игнорировать все эскейп символы в строке.
path = "C:\python\name.txt"
print(path)

path = r"C:\python\name.txt"
print(path)
'''

'''string = input('Input the sentence')
#1
#print(str.isalpha(string))
#print(string.isalpha())
#2
#print(str.isdigit(string))
#print(string.isdigit())
#3
#print(string.islower())
#print(string.isupper())
#4
#print(string.lower())
#print(string.upper())
#print(string.capitalize())
#print(string.title())
#5
#print(string.strip())
#print(string.lstrip())
#print(string.rstrip())
#6
#print(string.find('q'))
'''
'''
hello = ''
for i in string:
    if i!=' ':
        hello+=i
    else:
        break
print(hello)
print(string.replace(hello,'Slovo'))
print(string.replace('','Slovo'))
'''
'''
#print(string.split())
#print(string.join('-----'))
'''

# Есть некоторый текст. Реализуйте следующую функциональность:
# Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# Посчитайте сколько раз цифры встречаются в тексте;
# Посчитайте сколько раз знаки препинания встречаются в тексте;
# Посчитайте количество восклицательных знаков в тексте

string = input()
text = string.lstrip().capitalize()
print(text)


for i in range(0, len(text)):
    if text[i] == '.' and text[i+1]!= '.':
        text_2 = text.replace(text[i+1], text[i+1].capitalize())
        print(text_2)
#print(f'hello {text} world {string}') - formatirovaniye strok 1 iz 3 sposobov


#Пользователь вводит с клавиатуры строку.
# Посчитайте сколько букв,символов и цифр есть в строке.
# Выведите оба количества на экран
'''
string = input()
symbol = 0
digits = 0
bukvi = 0

#1:
for i in string:
    if 33 <= ord(i) <= 47:
        symbol += 1
    elif 48 <= ord(i) <= 57:
        digits += 1
    elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        bukvi += 1
else:
    print("Всего цифр - ", digits, ";", "Всего символов -", symbol, ";", "Всего букв -", bukvi, ";")

#2:
for i in string:
    if i.isalpha():
        bukvi+=1
    if i.isdigit():
        digits+=1
    if i != ' ' and not i.isdigit() and not i.isalpha() :
        symbol+=1
else:
    print(symbol,digits,bukvi)
    '''