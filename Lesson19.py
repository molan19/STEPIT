'''fileHandler = open('Lesson37File.txt','w')
fileHandler.write('Students:') #Обновляет старую информацию перезаписывает ее на новый
fileHandler.write('Amin')
fileHandler.close()

fileHandler = open('Lesson37File.txt','a')
fileHandler.write('Nurlan')
fileHandler.writelines(['Hello','World'])

fileHandler.close()

fileHandler = open('Lesson37File.txt') #r мод стоит по умолчанию
a = (fileHandler.readline()) #мы можем сохранить данные файла в переменную
print(a)
fileHandler.close()
'''
#Позволяет не открывать и закрывать файл
'''try:
    fileHandler = open('Lesson37File.txt','w')
    try:
        fileHandler.write('Just Do It')

    except Exception as e:
        print(e)
    finally:
        fileHandler.close()
except Exception as exc:
    print(exc)'''

#Более удобный способ для автоматического закрытия и открытия файла
'''with open('Lesson37File.txt','w') as fileHandler:
    fileHandler.write('Zavtra d 18:00')
    
with open('Lesson37File.txt','r') as fileHandler:
    print(fileHandler.readline())'''

file_path = r'C:\Users\Admin\PycharmProjects\pythonProject\another Files\Lesson37File.txt'

#1. Поиск и замена слов в содержимом текстового файла(Поиск должен быть реализован следующим образом:
#Вы проходитесь по информации в файле, находите нужную строку с нужным словом и программа
#выдает вам в качестве результата линию на которой находится данное слово)
'''text = 'Hello students how about your dreams'
write_text = "\n".join(text.split(" "))
with open(file_path, "w") as fileHandler:
    fileHandler.write(write_text)
with open(file_path,'r') as file:
    for item in file.readlines():
        if input() in item:
            print(f'Слово {item} найдено')
        else:
            print('Слово не найдено')'''
from string import punctuation
#2. Подсчет количества слов в содержимом текстового файла, которые не являются числами
text = 'Hello 12 students 13 how 14 about 15 your 16 dreams'
write_text = '\n'.join(text.split(' '))
with open(file_path,'w') as fileHandler:
    fileHandler.write(write_text)
with open(file_path,'r') as fileHandler_2:
    counter = 0
    for item in fileHandler_2:
        for word in item.split():
            if type(word) == str :
                counter += 1
print(counter)
#3. Вывести слова содержимого файла в обратном порядке
#4.  Удаление заданной по номеру строки из файла
