'''#Пользователь вводит с клавиатуры строку. Проверьте
#является ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаково
#слева направо и справа налево. Например, кок; А роза
#упала на лапу Азора; доход; А буду я у дуба.
slovo = input()
for i in range(0,len(slovo)):
    if slovo[0] == slovo[-1]:
        if slovo[1] == slovo[-2]:
            print("Палиндром")
        else:
            print("Не палиндром")
            break'''

'''#Пользователь вводит с клавиатуры некоторый текст,
#после чего пользователь вводит список зарезервированных
#слов. Необходимо найти в тексте все зарезервированные
#слова и изменить их регистр на верхний. Вывести на экран измененный текст.
text = input()
pervoye = 'hello '
vtoroye = 'my '
tretye = 'friend'
if pervoye in text:
    pervoye_1 = pervoye.upper()
if vtoroye in text:
    vtoroye_1 = vtoroye.upper()
if tretye in text:
    tretye_1 = tretye.upper()
    text_1 = pervoye_1+vtoroye_1+tretye_1
    print(text_1)
'''

'''#Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.
text = input()
tochka = '.'
counter = 0
for i in text:
    if i == tochka:
        counter += 1
print(counter)'''