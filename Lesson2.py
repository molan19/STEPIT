

chislo_1 = int(input("Введите число:")) #5178
poslednya = chislo_1%10 #8
pervoye = chislo_1//1000 #5
tretye = chislo_1//10%10 #7
vtoroye = chislo_1//100%10 #1
#print(vtoroye>=poslednya and vtoroye>=tretye and vtoroye>=pervoye)
#print(vtoroye>pervoye and vtoroye>tretye)

#Если второе число будет больше и равно последнему но при этом и одновременно будет меньше первого и третьего будет
print(vtoroye>=poslednya and vtoroye<pervoye and vtoroye<tretye)