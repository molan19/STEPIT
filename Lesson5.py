'''
chislo_1 = float(input("Введите число")) #10.34
celaya = int(chislo_1) #10
drobnaya = chislo_1-celaya #0.34
if celaya >= 0:
    print("Положительное ли оно?")
    if chislo_1 >= 0:
        print("Положительное")
    else:
        print("Отрицательное")

elif celaya == 0:
     if drobnaya > 0:
         print("Положительное")
'''
'''
#4. Напишите программу, которая проверяет, имеет ли дробное число целую часть,
# если да, то проверяем положительное ли это число, если нет целой части
# , то проверяем является ли дробная часть положительной.
# Пример.Если введено 10.34 , здесь 10 - целая часть, 0,34 - дробная
#Если число изначально написано как 0,89 - это значит целой части нет
number = float(input())
#celaya = number//1 # 5,67686786786 // 1 =  5
celaya = int(number)
drobnaya = number - celaya
if celaya>0 or celaya<0:
    if number>0:
        print('polojitelnoye :]')
    else:
        print('otricatelnoye :[')
elif celaya == 0:
     if drobnaya>0:
         print('polojitelnoye :]')
     else:
         print('otricatelnoye :[')
'''

'''
n1 = int(input())
n2 = int(input())
j = 1
while n1 <= n2:
    while j <= 3:
        print(n1**j, end="\t")
        j += 1
    print("\n")
    j = 1
    n1 += 1
'''
n1 = int(input())
n2 = int(input())
j = 1
while n1 <= n2:
    if n1%2 == 0:
        while j <= 3:
            print(n1**j, end="\t")
            j += 1
        print("\n")
        j = 1
        n1 += 1




