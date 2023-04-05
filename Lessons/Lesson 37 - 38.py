# 1.Файлы.
'''
Файл — это именованная область, расположенная во внешней памяти,
и обладающая следующими характеристиками:
■ имя файла (на определенном диске), которое позволяет программам идентифицировать файл
■ длина файла может быть ограничена только объемом диска.
'''
import fileinput

# 1.1Типы файлов, текстовые и бинарные.
'''
Текстовые файлы — это файлы хранящий в себе последовательность символов.
При передаче символов из потока на экран, часть из
них не выводится (например, символ сдвига на табуляцию, перевода строки).
Бинарные файлы - это файлы хранящие в себе  последовательность байтов,
которые однозначно соответствуют тому, что находится на внешнем устройстве
'''
# 1.2.Файловая система, особенности реализации форматов.
'''
Примеры текстовых файлов: (человек способен прочитать в любом текстовом редакторе)
■ web документы, стандарты: html, XML, CSS, JSON etc.
■ файлы исходных кодов: c, app, js, py, java etc.
■ текстовые документы: txt, tex, RTF etc.
■ текстовые представления табличных данных (файлы
с разделителями): csv, tsv etc.
■ файлы настроек и конфигураций: ini, cfg, reg etc
Примеры двоичных файлов:(человек не способен прочитать  в любом текстовом редакторе)
■ документы и электронные таблицы: .pdf, .doc, .xls etc.;
■ изображения: .png, .jpg, .gif, .bmp etc.;
■ видео: .mp4, .3gp, .mkv, .avi etc.;
■ аудио: .mp3, .wav, .mka, .aac etc.;
■ базы данных: .mdb, .accde, .frm, .sqlite etc.;
■ архивы: .zip, .rar, .iso, .7z etc.;
■ исполняемые файлы программ: .exe, .dll, .class etc.
'''
# 1.3.Работа с файлами:

'''
#открытие:
open(путь_к_файлу или переменная хранящая путь, режим открытия файла)
fileObj = open(fileName, mode)
fileName — это имя файла (или путь к нему), который вы хотите открыть.
При этом с именем вы должны указать и расширение. 
#закрытие;
#чтение:
read()
#запись:
write()
#закрытие:
close()
Режимы(моды):
Text file:
r - Открытие текстового файла только для
чтения. Если такого файла не существует, то
будет сгенерировано исключение
(обработка данных начинается с начала файла)
w - Открытие текстового файла только для
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)
a - Открытие текстового файла для добавления текста в конец файла.
Если такой файл не существует, то он будет
создан.
(обработка данных начинается с конца файла)
r+ - Открытие текстового файла для чтения и
записи. Если такого файла не существует, то
будет выведена ошибка.
(обработка данных начинается с начала файла)
w+ - Открытие текстового файла для чтения и
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)
a+ - Открытие текстового файла для чтения и
добавления текста в конец файла. Если такой файл не существует,
то он будет создан.
(обработка данных начинается с конца файла)
Binary file:
rb - Открытие двоичного файла для чтения.
Если такого файла не существует, то будет
выведена ошибка.
(обработка данных начинается с начала файла)
wb - Открытие двоичного файла для записи.
Если такой файл не существует, то он
будет создан. Иначе его содержимое будет
удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)
ab - Открытие двоичного файла для добавления.
Если такой файл не существует, то он будет
создан. Иначе данные из него будут удалены
(обработка данных начинается с конца файла) 
wb+ - Открытие двоичного файла для чтения и
записи. Если такой файл не существует, то
он будет создан. Иначе его содержимое
будет удалено и файл будет перезаписан.
(обработка данных начинается с начала файла)
ab+ - Открытие двоичного файла для чтения и
добавления. Если такой файл не существует,
то он будет создан. Иначе его содержимое
будет удалено
(обработка данных начинается с конца файла)
'''

# 1.4.Менеджер контекста with.
'''
Оператор with используется при обработке исключений, чтобы сделать код более чистым и читабельным.
 Это упрощает управление общими ресурсами, такими как файловые потоки.
Преимущество использования ключевого слова with перед вызовом функции open() в том, что функция file.close() 
 вызовется автоматически и освободит занятые ресурсы после того, как отработает код.
 без with:
try:
    somefile = open("test.txt", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
с with:
with open(file, mode) as file_obj:
    инструкции
#Porblem of coding 
with open(filename, encoding="utf8") as file:
'''

# Example
'''
# записывать введенный пользователем массив строк и считывать его обратно из файла на консоль:
my_file_path = ''
list_strings = list()
for i in range(4):
    str = input("Add line info:\n")
    list_strings.append(str)
with open(my_file_path,"a") as file:
    for i in list_strings:
        file.write(i)
with open(my_file_path,"r") as file:
    print(file.read())
    data = file.read()
    data.isalpha()'''


# https://metanit.com/python/tutorial/4.3.php
# https://metanit.com/python/tutorial/4.6.php
# https://metanit.com/python/tutorial/4.5.php
# https://metanit.com/python/tutorial/4.7.php

# 1.4.1 Функции для чтения файлов
'''
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")
readline(): считывает одну строку из файла
read(): считывает все содержимое файла в виде одной единой строки
readlines(): считывает все строки файла в список
with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
'''

# 1.4.2 Функции для записи файлов
'''
1. write()
2. writelines(набор_элементов)
with open("hello.txt","a") as FileHandler:
    myStrs = ["Appended line 1\n", "Appended line 2\n"]
    FileHandler.writelines(myStrs)
'''

# 1.5.Практические примеры использования.
'''
1. Поиск и замена слов в содержимом текстового файла
2. Подсчет количества слов в содержимом текстового файла, которые не являются числами
3. Вывести слова содержимого файла в обратном порядке
4.  Удаление заданной по номеру строки из файла
'''


'''fileHandler = open('Lesson37File.txt','w')
fileHandler.write('Students:')
fileHandler.write('Amin')
fileHandler.close()
fileHandler = open('Lesson37File.txt', 'a')
fileHandler.write(',Nurlan')
fileHandler.writelines(['HELLO','World','We love Python'])
fileHandler.close()
fileHandler = open('Lesson37File.txt', 'r')
a = fileHandler.readline()
print(a)
fileHandler.close()
'''
'''try:
    fileHandler = open('Lesson37File.txt', 'w')
    try:
        fileHandler.write('Just info')
    except Exception as e:
        print(e)
    finally:
        fileHandler.close()
except Exception as exc:
    print(exc)'''

'''
with open('Lesson37File.txt','w') as fileHandler:
    fileHandler.write('Zavtra V 18:00 jdem vsex!')
with open('Lesson37File.txt','r') as fileHandler:
    print(fileHandler.readlines())
'''
# записывать введенный пользователем массив строк и считывать его обратно из файла на консоль:


#file_path = r'C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\another Files\Lesson37File.txt'
'''string_list = []
for i in range(5):
    string_list.append(input())
with open(file_path, 'w') as fileHandler:
    for i in string_list:
        fileHandler.writelines(i)
with open(file_path) as fileHandler:
    print(fileHandler.readlines())'''


#readline(): считывает одну строку из файла

#read(): считывает все содержимое файла в виде одной единой строки

#readlines(): считывает все строки файла в список
'''with open(file_path, "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)
    print(contents)'''
#with open(file_path,'w') as file:
    #file.write('Hello world\n')
#file_path = r'C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\another Files\Lesson37File.txt'
'''list_el = ['11' , 'hello','1221']
with open(file_path , 'w') as fileHandler:
    for i in range(len(list_el)):
        fileHandler.write(list_el[i]+'\n')
with open(file_path,'r') as fileHandler:
    file_info = fileHandler.read()
    print(file_info)
    with open(file_path, 'w') as fileHandler:
        fileHandler.writelines(file_info)'''



file_path = r'C:\Users\Aghashirinov_r\PycharmProjects\pythonProject\another Files\Lesson37File.txt'
text = 'You will probably pass an exam'

def WriteTextToFile():
    write_text = "\n".join(text.split(" "))
    with open(file_path, "w") as fileHandler:
        fileHandler.write(write_text)

def ReadFile():
    with open(file_path) as fileHandler:
        print(fileHandler.read())

def FileActions(search, replace):
    WriteTextToFile()
    data = []

    with open(file_path, "r") as fileHandler:
        for item in fileHandler.readlines():
            if search in item:
                item = item.replace(search, replace)
            data.append(item)
        ReadFile()
        with open(file_path, "w") as fileHandler:
            fileHandler.write("".join(data))


FileActions('You','I')
ReadFile()