'''
print(5//3)# 1
print(5/3)#1.66666
print(-5/3)# -1.6666
print(-5//3)# -2
'''
'''
#4. Напишите программу, которая проверяет, имеет ли дробное число целую часть,
# если да, то проверяем положительное ли это число, если нет целой части
# , то проверяем является ли дробная часть положительной.
# Пример.Если введено 10.34 , здесь 10 - целая часть, 0,34 - дробная
#Если число изначально написано как 0,89 - это значит целой части нет
number = float(input())
celaya =0
if number>0:
    celaya = number//1
    print(celaya)
else:
    celaya = (number//1)+1
    print(celaya)


drobnaya = number - celaya
print(drobnaya)
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
while условие при котором цикл работает:
    инструкции/тело цикла
    while условие при котором цикл работает:
        инструкции / тело цикла
'''

'''
i = 1 #10 - BOCHEK DOLJNO BIT POLNO, NO ZAPOLNENA SEYCHAS 1
j = 1 # 10 - RAZ NUJNO ZAPOLNIT VODOY BOCHKU, CHTOBI ONA ZAPOLNILAS
while i <= 10: # vsego nochek 10(10 povtoreniy)
    while j <= 10: # KAJDUYU bochku chtobi zapolnit nujno 10 raz otrabotat deystvie zapolneniya
        print(i * j, end="\t")
        j += 1
    print("\n")# perexod na novuyu stroku
    j = 1
    i += 1

'''

#число**степень
#
nachalo_diapazona = int(input('Vvedite nachalo diapazona:'))
konec_diapazona = int(input('Vvedite konec diapazona:'))
stepen_nachalo = 1
stepen_konec = 3
while nachalo_diapazona!=konec_diapazona:
    number = nachalo_diapazona
    while stepen_nachalo!=stepen_konec+1:
        print(number,'**',stepen_nachalo,'=',number**stepen_nachalo, end='\t')
        stepen_nachalo+=1
    print('\n')
    stepen_nachalo = 1
    nachalo_diapazona+= 1