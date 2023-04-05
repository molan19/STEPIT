# Сортировка элементов.
'''
Сортировки в Python используются для упорядочивания элементов в списке и других коллекциях
'''

# Сортировка пузырьком (Bubble Sort)
'''
Сортировка пузырьком (Bubble Sort) - это простой алгоритм, который проходит по списку несколько раз,
сравнивая соседние элементы и меняя их местами, если они находятся в неправильном порядке.
'''
'''def bubble_sort(list_el,reverse):
    length = len(list_el)
    for item in range(0,length-1):
        for j in range(length-item-1):
            if list_el[j]>list_el[j+1]:
                list_el[j],list_el[j+1]= list_el[j+1],  list_el[j]


    return list_el
list_el =[1231,1,3242,213,23,0,91]
bubble_sort(list_el)
print(list_el)
'''
# Сортировка слиянием(Merge sort)
'''Merge sort - использует метод "разделяй и властвуй".Список разделяется
 на две части и каждая из них рекурсивно сортируется.
 Затем две отсортированные части массива сливаются в один'''
'''
def merge_sort(arr):
    # если в списке один элемент, возвращаем его
    if len(arr) <= 1:
        return arr
    # находим середину списка и делим его на два
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    # рекурсивно вызываем функцию сортировки для каждой половины
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # вызываем функцию слияния для отсортированных половин
    return merge(left_half, right_half)
def merge(left_half, right_half):
    # создаем пустой список, который будем заполнять
    sorted_list = []
    # создаем индексы для обеих половин
    left_index = 0
    right_index = 0
    # проходим по обеим половинам, сравниваем элементы и добавляем их в отсортированный список
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1
    # добавляем оставшиеся элементы из левой или правой половины
    sorted_list += left_half[left_index:]
    sorted_list += right_half[right_index:]
    # возвращаем отсортированный список
    return sorted_list
'''

# Практика
'''
1. Напишите функцию сортировки которая принимает два параметра ,список и переменную отвечающую за способ 
сортировки(назовите ее reverse). Функция сортирует элементы списка по возрасатанию если reverse = True
иначе она отсортирует по убыванию. 
'''

# Линейный поиск - это простой алгоритм поиска элемента в списке.
# Он проходится по всем элементам списка по очереди, пока не найдет нужный элемент.
# Реализация может выглядеть так:
'''def linear_search(list_el,target):
    for i in range(len(list_el)):
        if list_el[i] == target:
            return i
list_el =[1231,1,3242,213,23,0,91]
print(linear_search(list_el,0))'''


# Бинарный поиск -  это алгоритм поиска элемента в отсортированном списке.
# Он работает путем деления списка на половины и проверки целевого значения в каждой половине.
# Если значение присутствует в списке, алгоритм вернет его индекс, в противном случае вернет -1

def binary_search(arr, target):
    low_point = 0
    high_point = len(arr) - 1

    while low_point <= high_point:
        middle = (low_point + high_point) // 2
        if arr[middle] == target:
            print(arr)
            return middle
        elif arr[middle] < target:
            low_point = middle + 1
        else:
            high_point = middle - 1

    return -1


list_el = [1231, 1, 3242, 213, 23, 0, 91]

print(binary_search(sorted(list_el), 0))