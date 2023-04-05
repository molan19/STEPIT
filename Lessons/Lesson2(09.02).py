'''
# Система счисления - INT

#b = 0b1011 # двоичная система счисления
#b = 0o11 # восьмиричная система счисления
#b = 0xFF # шестнадцатеричная  система счисления
#print(b , type(b))
'''

'''
#** , / , // , % , *, +, -
x = 8 + (2*4/2)**3 - 19%10 # 8 + 16 - 9
print(x) #15
'''


'''
# bool = True/False (Да/Нет)

#sdelal_dz = True # 1
#provereno = True # 1

vvod_bool = bool(input())

print(vvod_bool, type(vvod_bool))
#print(type(sdelal_dz + provereno), type(sdelal_dz),type(provereno)) # False? / True?

#proverka= sdelal_dz - provereno
#print(proverka, type(proverka))
'''

'''
# str - строка
stroka_1 = input("Write number:")
stroka_2 = input("Write word")

print(stroka_1, type(stroka_1))
print(stroka_2, stroka_1)

vichisleniya = stroka_2+stroka_1

print(vichisleniya, type(vichisleniya))
'''

# Condition operators
'''
== - равно
!= - не равно
> - больше 
< - меньше
>= - больше или равно
<= - меньше или равно



chislo_1 = int(input())
chislo_2 = int(input())

print(chislo_1>=chislo_2)
'''


'''
# Logic operators

and - и
or - или
not - нет

 
in - в
'''

'''
#chislo = 4  and 'hello'

age = float(input()) # 70
puls = int(input())  #120

koordiogramma = age and puls < 150 # true
#koordiogramma_2 = age > 50 or puls < 150 # true
#koordiogramma_3 = not age > 50




print(koordiogramma)
#print(koordiogramma_2)
#print(koordiogramma_3)
'''


'''
slovo = input()
slovo_2 = input()

print(slovo in slovo_2)
'''

# Напишите программу которая проверит является ли вторая цифра
# четырхзначного числа больше всех других чисел этого числа и больше ли это
# число одновременно двух соседних цифр


'''
chislo = int(input()) # 9876
poslednaya = chislo%10 # 6
tretye = chislo//10%10 #987%10 = 7
vtoroye = chislo//100%10 # 98%10 = 8
pervoye = chislo//1000 # 9

proverka = vtoroye >= pervoye and vtoroye >= tretye and vtoroye >= poslednaya

print(proverka)

proverka_2 = vtoroye > pervoye and vtoroye > tretye

print(proverka_2)
'''

# Conditions

temperatura = int(input())# -1

if temperatura<0 :
    print("Sneg poshel")
elif temperatura>10:
    print()

elif temperatura>100:
    print()

else :
    print("solnishko")