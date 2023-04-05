'''print((lambda element_1,element_2: element_1+element_2)(999,3))
print((lambda element_1,element_2: element_1+element_2 if element_1>element_2 else element_1-element_2)(999,3))
result = (lambda element_1,element_2: element_1+element_2)(999,3)'''
'''list_el = [1,2,3,4,5]
print(list(map(lambda element: element*2,list_el)))
'''
#reduce()- когда требуется обработать список значений таким образом, чтобы свести процесс к единственному результату,
# filter()- определяет нужно ли исключить конкретный элемент из последовательности или нет
# (если да  то фильтрует последовательность, если нет ничего не делает)
#zip()- oбъединяет отдельные элементы из каждой последовательности в итерируемую последовательность

'''def my_map(function,list):
    new_list = []
    for item in list:
        new_list.append(function(item))
    return new_list
list_el = [1,2,3,4,5]
print(my_map(lambda element: element*2,list_el))
''''''
list_el = [1,2,3,4,5]
print(list(filter(lambda element: element%2 == 0,list_el)))

from functools import reduce
print(reduce(lambda elements,element_2:elements+element_2,list_el))


print(list(zip('avcdefe',range(0,4),[4,2,23,True])))#обзединяет элементы по индексу'''
'''def my_filter(function,list):
    new_list = []
    for item in list:
        if function(item):
            new_list.append(item)
    return new_list
list_el = [1,2,4,3,5,6]
print(my_filter(lambda element: element%2 == 0,list_el))'''
#reduce()- когда требуется обработать список значений таким образом, чтобы свести процесс к единственному результату,
'''def my_reduce(function,list,initial=0):
    for i in list:
        initial = function(initial,i)
    return initial
list_el = [1,2,4,3,5,6]
print(my_reduce(lambda element_1,element_2:element_1+element_2,list_el))'''
print(2%0)
