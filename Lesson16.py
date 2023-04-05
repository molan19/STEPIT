'''def bubble_sort(list_el):
    lenght = len(list_el)
    for item in range(0,lenght-1):
        for j in range(lenght-item-1):
            if list_el[j]>list_el[j+1]:
                list_el[j],list_el[j+1] = list_el[j+1],list_el[j]
    return list_el

list_el = [1,3,5,2,12,42,4,23]
print(bubble_sort(list_el))'''

'''def merge(list_el):
    lenght = len(list_el)
    if lenght == 1:
        return list_el
    
    
    middle = lenght//2
    left_list = list_el[:middle]
    right_list = list_el[middle:]
    
    left_list = merge(left_list)
    right_list = merge(right_list)
    
    return merge_sort(left_list,right_list)


def merge_sort(left_array,right_array):
    sorted_list = []
    
    left_index=0
    right_index=0
    while left_index<len(left_array) and right_index<len(right_array):
        if left_array[left_index]<right_array[right_index]:
            sorted_list.append(left_array[left_index])
            left_index+=1
        else:
            sorted_list.append(right_array[right_index])
            right_index+=1
    sorted_list+=left_array[left_index:]
    sorted_list+=right_array[right_index:]
    
    return sorted_list'''

'''def bubble(list_el,initial):
    lenght = len(list_el)
    for i in range(0,lenght-1):
        for j in range(lenght-i-1):
            if initial == True:
                if list_el[j]<list_el[j+1]:
                    list_el[j],list_el[j+1]=list_el[j+1],list_el[j]
            else:
                if list_el[j] > list_el[j + 1]:
                    list_el[j], list_el[j + 1] = list_el[j + 1], list_el[j]
    return list_el'''
'''def linear_search(list_el,target):
    for i in range(len(list_el)):
        if list_el[i] == target:
            return i
list_el = [1,2,43,53,12,32,31,321]
linear_search(list_el,2)'''

'''def binary_search(arr,target):
    low_point = 0
    high_point = len(arr)-1

    while low_point<=high_point:
        middle = (low_point+high_point)//2
        if arr[middle]==target:
            print(arr)
            return middle
        elif arr[middle]<target:
            low_point = middle+1
        else:
            high_point = middle-1

    return -1
list_el = [1,2,43,53,12,32,31,321]
print(binary_search(sorted(list_el),32))'''