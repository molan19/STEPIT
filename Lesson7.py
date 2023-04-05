'''from random import randint
for random_number in range(1, 10):
    print(randint(1, 10)) #без for если нужно одно число
line = "hello"
print(line[-1])'''
'''stroka = input() #hello
for i in range(-1, -len(stroka)-1 , -1):
    print(stroka[i])'''

while True:
    user_text = str(input()).split(' ')
    otvet = len(user_text)
    print(otvet)
