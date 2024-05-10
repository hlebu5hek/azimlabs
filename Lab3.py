'''Вариант 18
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.
d e
c b
 4
3 1
 2
Формируется матрица F следующим образом:
если в С количество положительных элементов в четных столбцах в области 2 больше,
чем количество отрицательных  элементов в нечетных столбцах в области 4,
то поменять в С симметрично области 1 и 3 местами, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: (F+A)*AT – K * F.
Выводятся по мере формирования А, F и все матричные операции последовательно.
'''
from random import randint as rnd

def printList(z):
    for i in z:
        for j in i:
            print("{:5}".format(j), end=' ')
        print()
    print()

k, n = int(input("k = ")), int(input("n = "))
m = n//2
n = m*2
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(rnd(-10,10))

print("Матрица A : ")
printList(a)

b = []
c = []
d = []
e = []
for i in range(m):
    b.append([])
    c.append([])
    d.append([])
    e.append([])
    for j in range(m):
        b[i].append(a[i+m][j+m])
        c[i].append(a[i+m][j])
        d[i].append(a[i][j])
        e[i].append(a[i][j+m])

print("Матрица B : ")
printList(b)
print("Матрица C : ")
printList(c)
print("Матрица D : ")
printList(d)
print("Матрица E : ")
printList(e)

count_pos = 0
for j in range(m//2):
    if j % 2 != 0: continue
    for i in range(m-j-1, m):
        count_pos += 1 if c[i][j] >= 0 else 0
for j in range(m//2, m):
    if j % 2 != 0: continue
    for i in range(j, m):
        count_pos += 1 if c[i][j] >= 0  else 0
print("В С количество положительных чисел в четных столбцах в области 2 = ", count_pos)

count_neg = 0
for j in range(m//2):
    if j % 2 == 0: continue
    for i in range(0, j+1):
        count_neg += 1 if c[i][j] < 0 else 0
for j in range(m//2, m):
    if j % 2 == 0: continue
    for i in range(0, m-j):
        count_neg += 1 if c[i][j] < 0 else 0
print("В С количество положительных чисел в четных столбцах в области 2 = ", count_neg)

if count_pos > count_neg:
    print("Количество положительных чисел, больше количества отрицательных\n")
    for i in range(0, m//2):
        for j in range(0, i+1):
            c[i][j], c[i][m-j-1] = c[i][m-j-1], c[i][j]
    for i in range(m//2, m):
        for j in range(0, m-i):
            c[i][j], c[i][m-j-1] = c[i][m-j-1], c[i][j]
else:
    print("Количество положительных чисел, меньше количества отрицательных\n")
    for i in range(m):
        for j in range(m):
            c[i][j], e[i][j] = e[i][j], c[i][j]

print("Матрица B : ")
printList(b)
print("Матрица C : ")
printList(c)
print("Матрица D : ")
printList(d)
print("Матрица E : ")
printList(e)

f = []
f.extend(d)
f.extend(c)
for i in range(m):
    f[i].extend(e[i])
for i in range(m, n):
    f[i].extend(b[i-m])

print("Матрица F : ")
printList(f)

at = []
for i in range(n):
    at.append([])
    for j in range(n):
        at[i].append(a[j][i])

print("Матрица A транспон. : ")
printList(at)

fk = []
for i in range(n):
    fk.append([])
    for j in range(n):
        fk[i].append(f[i][j]*k)

print("Матрица F умноженная на K : ")
printList(fk)

fa = []
for i in range(n):
    fa.append([])
    for j in range(n):
        fa[i].append(f[i][j] + a[i][j])

print("Матрица F + A : ")
printList(fa)

faat = []
for i in range(n):
    faat.append([])
    for j in range(n):
        s = 0
        for l in range(n):
             s += fa[i][l]*at[j][l]
        faat[i].append(s)

print("Матрица F + A умноженная на AT : ")
printList(faat)

for i in range(n):
    for j in range(j):
        faat[i][j] -= fk[i][j]

print("(F + A) * AT – K * F = ")
printList(faat)