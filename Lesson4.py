'''
chislo_1 = float(input("Введите число")) #10.34
celaya = chislo_1//1 #10
drobnaya = chislo_1-celaya #0.34
if celaya > 0:
    print("Положительное ли оно?")
    if chislo_1 > 0:
        print("Положительное")

elif celaya == 0:
     if drobnaya > 0:
         print("Положительное")
'''

'''
while True:
    number = int(input())
    if number >= 100 and number <1000:
        print("Ura " , number)
    else:
        print("Неа")
        break
'''
summa =0
while True:
    number = int(input())
    summa += number
    if summa <=10:
        print(number)
    else:
        break
