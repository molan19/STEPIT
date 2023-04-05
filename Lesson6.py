'''
for i in range(1,100+1):
    if i%2 == 0:
        print(i)
'''
'''
a = int(input())
b = int(input())
s = 0
counter = 0
for i in range(a, b+1):
    s += i
    if i == b:
        print(s/counter)
print(s)
'''
'''
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end='\t')
    print('\n')
'''
kurs_dollara = float(input())
while True:
    manat = int(input()) #20 manat
    print(manat/kurs_dollara)

