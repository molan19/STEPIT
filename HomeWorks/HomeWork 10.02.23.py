# Напишите программу которая проверит является ли вторая цифра
# четырхзначного числа больше всех других чисел этого числа и больше ли это
# число одновременно двух соседних цифр если да,вывести сумму,нет разность

chislo_1 = int(input("Введите число:")) #5178
pervoye = chislo_1//1000 #5
vtoroye = chislo_1//100%10 #1
tretye = chislo_1//10%10 #7
poslednya = chislo_1%10 #8
if vtoroye > pervoye and vtoroye > poslednya and vtoroye > tretye:
    print(pervoye+vtoroye+tretye+poslednya)
else:
    print(pervoye-vtoroye-tretye-poslednya)



