'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие
минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)
и целевую функцию для нахождения оптимального  решения.
Вариант 2. В холодильнике 10 брикетов мороженого разного вида.
Ребенку разрешается взять вечером не более 2 брикетов.
Подготовьте различные варианты поедания мороженного ребенком на неделю.
'''
import itertools
import math

orders = []
counts = []

def shufleOrder(pool, order):
    if len(pool) < 1:
        orders.append(order)
        return
    for i in pool:
        npool = []
        npool.extend(pool)
        npool.remove(i)
        norder = []
        norder.extend(order)
        norder.append(i)
        shufleOrder(npool, norder)

def shufleCounts(summ, count, j):
    if j < 1:
        counts.append(count)
        return
    if summ < 1:
        count.append(0)
        shufleCounts(summ, count, j-1)
    elif summ < 2:
        count.append(1)
        shufleCounts(summ-1, count, j-1)
    else:
        ncount = []
        ncount.extend(count)
        ncount.append(1)
        count.append(2)
        shufleCounts(summ-1, ncount, j-1)
        shufleCounts(summ-2, count, j-1)

bricks = ["Брикет 1", "Брикет 2", "Брикет 3", "Брикет 4", "Брикет 5", "Брикет 6", "Брикет 7", "Брикет 8", "Брикет 9", "Брикет 10"]
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
c = int(input("Количество выводимых вариантов : "))
shufleOrder(bricks, [])
shufleCounts(10, [], 7)

ordersit = list(itertools.permutations(bricks, 10))
countsit = list(itertools.product([1,2], repeat=7))

print('Результат работы алгоритма : ')
i = 0
for order in orders:
    if i >= c: break
    for count in counts:
        if i >= c: break
        print('Случай {:} : '.format(i+1))
        i += 1
        j = 0
        for day, count in enumerate(count):
            print(' | ', days[day], end=' : ')
            for k in range(count):
                print(order[j], end=' ')
                j+=1
        print()

print('\nРезультат работы itertools : ')
i = 0
for order in ordersit:
    if i >= c: break
    for count in countsit:
        if i >= c: break
        if sum(count) > 10: continue
        print('Случай {:} : '.format(i+1))
        i += 1
        j = 0
        for day, count in enumerate(count):
            print(' | ', days[day], end=' : ')
            for k in range(count):
                print(order[j], end=' ')
                j+=1
        print()