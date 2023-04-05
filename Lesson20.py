from pickle import dump,load
file_path = r'C:\Users\Admin\PycharmProjects\pythonProject\anotherFiles\Lesson39.doc'
'''with open(file_path,'wb') as fileHandler:
    dump([1,2,3,4,5],fileHandler)

with open(file_path,'rb') as fileHandler:
    data = load(fileHandler)
    print(data[1])'''

#Поиск и замена слов списка в бинарном файле
'''with open(file_path,'wb') as fileHandler:
    list_el = ['Hello','Goodbye','moment','relax']
    dump(list_el,fileHandler)

with open(file_path,'rb') as fileHandler:
    data = load(fileHandler)
    search = input()
    zamena = input()
    for i in range(len(list_el)):
        if list_el[i] == search:
            list_el[i] = zamena
    with open(file_path, 'wb') as fileHandler:
        dump(list_el, fileHandler)

with open(file_path,'rb') as fileHandler:
    data = load(fileHandler)
    print(data)'''
