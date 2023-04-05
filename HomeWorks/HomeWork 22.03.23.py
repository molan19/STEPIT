#reduce()- когда требуется обработать список значений таким образом, чтобы свести процесс к единственному результату,
# filter()- определяет нужно ли исключить конкретный элемент из последовательности или нет
# (если да  то фильтрует последовательность, если нет ничего не делает)
#zip()- oбъединяет отдельные элементы из каждой последовательности в итерируемую последовательность

'''#Функция map с помощью генератора
list_elements = [1, 2, 3, 4, 5]
my_map = [items*2 for items in list_elements]
print(my_map)'''

'''#Функция filter с помощью генератора
list_elements = [1,2,3,5,7,8,9]
my_filter = [item for item in list_elements if item%2 != 0] #Вводим любые условия для фильтра
print(my_filter)'''
#filter без генератора
'''def my_filter(function,list):
    new_list = []
    for item in list:
        if function(item):
            new_list.append(item)
    return new_list
list_el = [1,2,4,3,5,6]
print(my_filter(lambda element: element%2 == 0,list_el))'''
#reduce созданный с помощью функции
'''def my_reduce(function,list,initial=0):
    for i in list:
        initial = function(initial,i)
    return initial
list_el = [1,2,4,3,5,6]
print(my_reduce(lambda element_1,element_2:element_1+element_2,list_el))'''