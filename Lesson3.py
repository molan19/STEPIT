'''
chislo_1 = float(input()) #1,5
chislo_2 = float(input()) #4,7
celaya_1 = chislo_1*10//10 #1
drobnaya_1 = chislo_1*10%10 #5
celaya_2 = chislo_2*10//10 #4
drobnaya_2 = chislo_2*10%10 #7
print(celaya_2+celaya_1)
print(drobnaya_2+drobnaya_1)
'''
'''
dengi = float(input()) #15 манат 30 копеек
manat = dengi*100//100 #15.30= 15.30*100= 1530 = 15 манат
kopeyki = dengi-manat
print(manat , kopeyki)
'''
'''
chislo_1 = int(input("Введите первое число"))
chislo_2 = int(input("Введите второе число"))
if chislo_1 > chislo_2:
    print(chislo_2)
else:
    print(chislo_1)
'''
'''
a = float(input())
b = float(input())
vibor = int(input('Выберите операцию: 1. + , 2. -, 3. * ,4. /'))
if vibor == 1:
    print(a+b)
elif vibor == 2:
    print(a-b)
elif vibor == 3:
    print(a*b)
else:
    print(a/b)
'''
nomer = int(input()) #25467
poslednya = nomer%10 #7
chetvertoya = nomer//10%10 #6
tretye = nomer//100%10 #4
vtoraya = nomer//1000%10 #5
pervaya = nomer//10000 #2
if poslednya == pervaya and chetvertoya == vtoraya:
    print("Число полиандром")
else:
    print("Печально")




